"""
SEO Audit Data Collector
Собирает данные для SEO-аудита с любого сайта.

Использование:
    python seo_audit_collector.py https://domain.com

Зависимости:
    pip install requests beautifulsoup4
"""

import requests
from bs4 import BeautifulSoup
import json
import sys
from urllib.parse import urljoin, urlparse
import xml.etree.ElementTree as ET
from datetime import datetime
import time


class SEOAuditCollector:
    def __init__(self, domain):
        self.domain = domain.rstrip('/')
        self.parsed = urlparse(self.domain)
        self.base = f"{self.parsed.scheme}://{self.parsed.netloc}"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (compatible; SEOAuditBot/1.0)'
        })
        self.results = {
            'domain': self.domain,
            'timestamp': datetime.now().isoformat(),
            'robots_txt': None,
            'sitemaps': [],
            'pages': [],
            'issues': []
        }

    def collect_robots_txt(self):
        """Собирает и анализирует robots.txt"""
        url = f"{self.base}/robots.txt"
        try:
            r = self.session.get(url, timeout=10)
            content = r.text if r.status_code == 200 else None
            self.results['robots_txt'] = {
                'url': url,
                'status': r.status_code,
                'content': content,
                'blocks_css': '/*.css$' in content if content else False,
                'blocks_js': '/*.js$' in content if content else False,
                'sitemap_urls': [
                    line.split(': ', 1)[1].strip()
                    for line in content.split('\n')
                    if line.lower().strip().startswith('sitemap:')
                ] if content else []
            }
            print(f"  robots.txt: HTTP {r.status_code}")
            if self.results['robots_txt']['blocks_css']:
                print("  ⚠️  robots.txt блокирует CSS!")
            if self.results['robots_txt']['blocks_js']:
                print("  ⚠️  robots.txt блокирует JS!")
        except Exception as e:
            self.results['robots_txt'] = {'error': str(e)}
            print(f"  Ошибка robots.txt: {e}")

    def collect_sitemap_urls(self, sitemap_url, depth=0):
        """Рекурсивно собирает URL из sitemap"""
        if depth > 5:
            return []
        urls = []
        try:
            r = self.session.get(sitemap_url, timeout=15)
            if r.status_code != 200:
                print(f"  Sitemap {sitemap_url}: HTTP {r.status_code}")
                return urls
            root = ET.fromstring(r.content)
            ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            # Sitemap index
            for sitemap in root.findall('.//sm:sitemap/sm:loc', ns):
                print(f"  Подsitemap: {sitemap.text}")
                urls.extend(self.collect_sitemap_urls(sitemap.text, depth + 1))
            # URL entries
            for loc in root.findall('.//sm:url/sm:loc', ns):
                urls.append(loc.text)
        except ET.ParseError:
            print(f"  Ошибка парсинга XML: {sitemap_url}")
        except Exception as e:
            self.results['issues'].append(f"Sitemap error ({sitemap_url}): {e}")
            print(f"  Ошибка sitemap: {e}")
        return urls

    def collect_all_sitemaps(self):
        """Собирает все URL из всех sitemap"""
        sitemap_urls = self.results['robots_txt'].get('sitemap_urls', [])
        if not sitemap_urls:
            sitemap_urls = [f"{self.base}/sitemap.xml"]
            print("  Sitemap не указан в robots.txt, пробуем /sitemap.xml")
        all_urls = []
        for surl in sitemap_urls:
            print(f"  Загрузка: {surl}")
            urls = self.collect_sitemap_urls(surl)
            self.results['sitemaps'].append({
                'url': surl,
                'urls_count': len(urls),
                'urls': urls
            })
            all_urls.extend(urls)
            print(f"  → {len(urls)} URL")
        return list(set(all_urls))  # Убираем дубли

    def analyze_page(self, url):
        """Анализирует одну страницу"""
        page_data = {
            'url': url,
            'status': None,
            'final_url': None,
            'title': None,
            'description': None,
            'canonical': None,
            'h1': [],
            'h2': [],
            'noindex': False,
            'nofollow': False,
            'og': {},
            'schema': [],
            'hreflang': [],
            'images_total': 0,
            'images_no_alt': 0,
            'internal_links': 0,
            'external_links': 0,
            'issues': []
        }
        try:
            r = self.session.get(url, timeout=15, allow_redirects=True)
            page_data['status'] = r.status_code
            page_data['final_url'] = r.url

            if r.status_code != 200:
                page_data['issues'].append(f'HTTP_{r.status_code}')
                return page_data

            soup = BeautifulSoup(r.text, 'html.parser')

            # Title
            title_tag = soup.find('title')
            page_data['title'] = title_tag.text.strip() if title_tag else None

            # Description
            desc_tag = soup.find('meta', attrs={'name': 'description'})
            page_data['description'] = desc_tag.get('content', '').strip() if desc_tag else None

            # Canonical
            can_tag = soup.find('link', attrs={'rel': 'canonical'})
            page_data['canonical'] = can_tag.get('href', '').strip() if can_tag else None

            # H1, H2
            page_data['h1'] = [h.text.strip() for h in soup.find_all('h1')]
            page_data['h2'] = [h.text.strip() for h in soup.find_all('h2')]

            # Robots meta
            robots_tag = soup.find('meta', attrs={'name': 'robots'})
            if robots_tag:
                robots_content = robots_tag.get('content', '').lower()
                page_data['noindex'] = 'noindex' in robots_content
                page_data['nofollow'] = 'nofollow' in robots_content

            # OG tags
            for og in soup.find_all('meta', attrs={'property': lambda x: x and x.startswith('og:')}):
                page_data['og'][og['property']] = og.get('content', '')

            # Schema.org (JSON-LD)
            for script in soup.find_all('script', type='application/ld+json'):
                try:
                    schema = json.loads(script.string)
                    if isinstance(schema, dict):
                        page_data['schema'].append(schema.get('@type', 'unknown'))
                    elif isinstance(schema, list):
                        for item in schema:
                            if isinstance(item, dict):
                                page_data['schema'].append(item.get('@type', 'unknown'))
                except (json.JSONDecodeError, TypeError):
                    pass

            # Hreflang
            for hl in soup.find_all('link', attrs={'rel': 'alternate', 'hreflang': True}):
                page_data['hreflang'].append({
                    'lang': hl['hreflang'],
                    'href': hl.get('href', '')
                })

            # Images
            images = soup.find_all('img')
            page_data['images_total'] = len(images)
            page_data['images_no_alt'] = len([i for i in images if not i.get('alt', '').strip()])

            # Links
            base_domain = urlparse(self.base).netloc
            for a in soup.find_all('a', href=True):
                href = urljoin(url, a['href'])
                link_domain = urlparse(href).netloc
                if link_domain == base_domain:
                    page_data['internal_links'] += 1
                else:
                    page_data['external_links'] += 1

            # Issues detection
            if not page_data['title']:
                page_data['issues'].append('NO_TITLE')
            if not page_data['description']:
                page_data['issues'].append('NO_DESCRIPTION')
            if not page_data['h1']:
                page_data['issues'].append('NO_H1')
            elif len(page_data['h1']) > 1:
                page_data['issues'].append(f'MULTIPLE_H1 ({len(page_data["h1"])})')
            if not page_data['canonical']:
                page_data['issues'].append('NO_CANONICAL')
            if not page_data['schema']:
                page_data['issues'].append('NO_SCHEMA')
            if page_data['images_no_alt'] > 0:
                page_data['issues'].append(f'IMAGES_NO_ALT ({page_data["images_no_alt"]})')
            if page_data['noindex']:
                page_data['issues'].append('NOINDEX')

        except requests.exceptions.Timeout:
            page_data['issues'].append('TIMEOUT')
        except requests.exceptions.ConnectionError:
            page_data['issues'].append('CONNECTION_ERROR')
        except Exception as e:
            page_data['issues'].append(f'FETCH_ERROR: {str(e)[:100]}')

        return page_data

    def check_duplicate_candidates(self, max_checks=50):
        """Проверяет потенциальные дубли"""
        candidates = []
        
        # Паттерны для Tilda
        for page in self.results['pages'][:20]:  # Проверяем первые 20 страниц
            url = page['url']
            # Убираем trailing slash для генерации кандидатов
            clean_url = url.rstrip('/')
            if clean_url.endswith(('3', '2')):
                continue
            for suffix in ['2', '3']:
                candidate = clean_url + suffix
                if candidate not in [p['url'] for p in self.results['pages']]:
                    candidates.append(candidate)

        # Общие паттерны
        candidates.extend([
            f"{self.base}/page1.html",
            f"{self.base}/page63012251.html",
            f"{self.base}/index.php",
        ])

        duplicates = []
        checked = 0
        for url in candidates:
            if checked >= max_checks:
                break
            try:
                r = self.session.get(url, timeout=10, allow_redirects=True)
                checked += 1
                if r.status_code == 200:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    title_tag = soup.find('title')
                    duplicates.append({
                        'url': url,
                        'status': r.status_code,
                        'title': title_tag.text.strip() if title_tag else None
                    })
                time.sleep(0.3)
            except:
                pass

        return duplicates

    def generate_summary(self):
        """Генерирует краткую сводку"""
        total = len(self.results['pages'])
        ok = len([p for p in self.results['pages'] if p['status'] == 200])
        with_issues = len([p for p in self.results['pages'] if p['issues']])
        no_title = len([p for p in self.results['pages'] if 'NO_TITLE' in p.get('issues', [])])
        no_desc = len([p for p in self.results['pages'] if 'NO_DESCRIPTION' in p.get('issues', [])])
        no_schema = len([p for p in self.results['pages'] if 'NO_SCHEMA' in p.get('issues', [])])
        no_canonical = len([p for p in self.results['pages'] if 'NO_CANONICAL' in p.get('issues', [])])
        no_alt = sum(p.get('images_no_alt', 0) for p in self.results['pages'])

        summary = {
            'total_pages': total,
            'http_200': ok,
            'pages_with_issues': with_issues,
            'no_title': no_title,
            'no_description': no_desc,
            'no_schema': no_schema,
            'no_canonical': no_canonical,
            'total_images_no_alt': no_alt,
            'duplicates_found': len(self.results.get('duplicates_found', [])),
            'robots_blocks_css': self.results.get('robots_txt', {}).get('blocks_css', False),
            'robots_blocks_js': self.results.get('robots_txt', {}).get('blocks_js', False),
        }

        self.results['summary'] = summary
        return summary

    def run_full_audit(self, max_pages=50):
        """Запуск полного аудита"""
        print(f"\n{'='*60}")
        print(f"SEO-АУДИТ: {self.domain}")
        print(f"Дата: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"{'='*60}\n")

        # 1. Robots.txt
        print("[1/6] Анализ robots.txt...")
        self.collect_robots_txt()

        # 2. Sitemap
        print("\n[2/6] Сбор sitemap...")
        sitemap_urls = self.collect_all_sitemaps()
        print(f"  Итого: {len(sitemap_urls)} уникальных URL")

        # 3. Анализ страниц
        urls_to_check = sitemap_urls[:max_pages]
        print(f"\n[3/6] Анализ {len(urls_to_check)} страниц (лимит: {max_pages})...")
        for i, url in enumerate(urls_to_check):
            progress = f"[{i+1}/{len(urls_to_check)}]"
            short_url = url.replace(self.base, '')
            print(f"  {progress} {short_url}")
            page = self.analyze_page(url)
            self.results['pages'].append(page)
            time.sleep(0.5)

        # 4. Проверка дублей
        print(f"\n[4/6] Проверка потенциальных дублей...")
        duplicates = self.check_duplicate_candidates()
        self.results['duplicates_found'] = duplicates
        print(f"  Найдено: {len(duplicates)} потенциальных дублей")
        for d in duplicates:
            print(f"    {d['url']} — {d.get('title', '?')[:50]}")

        # 5. Сводка
        print(f"\n[5/6] Формирование сводки...")
        summary = self.generate_summary()

        # 6. Сохранение
        hostname = urlparse(self.domain).netloc.replace('.', '_')
        output_file = f"seo_audit_{hostname}.json"
        print(f"\n[6/6] Сохранение в {output_file}...")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=2)

        # Вывод сводки
        print(f"\n{'='*60}")
        print("СВОДКА АУДИТА")
        print(f"{'='*60}")
        print(f"  Страниц проверено:      {summary['total_pages']}")
        print(f"  HTTP 200:               {summary['http_200']}")
        print(f"  С проблемами:           {summary['pages_with_issues']}")
        print(f"  Без Title:              {summary['no_title']}")
        print(f"  Без Description:        {summary['no_description']}")
        print(f"  Без Schema.org:         {summary['no_schema']}")
        print(f"  Без Canonical:          {summary['no_canonical']}")
        print(f"  Изображений без alt:    {summary['total_images_no_alt']}")
        print(f"  Потенциальных дублей:   {summary['duplicates_found']}")
        print(f"  robots.txt блок CSS:    {'⚠️ ДА' if summary['robots_blocks_css'] else '✅ Нет'}")
        print(f"  robots.txt блок JS:     {'⚠️ ДА' if summary['robots_blocks_js'] else '✅ Нет'}")
        print(f"{'='*60}")
        print(f"Результат: {output_file}\n")

        return self.results


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Использование: python seo_audit_collector.py https://domain.com [max_pages]")
        print("Пример:        python seo_audit_collector.py https://example.com 30")
        sys.exit(1)

    domain = sys.argv[1]
    max_pages = int(sys.argv[2]) if len(sys.argv) > 2 else 50

    collector = SEOAuditCollector(domain)
    collector.run_full_audit(max_pages=max_pages)