"""
GSC Data Collector
Собирает данные из Google Search Console через OAuth.

Использование:
    python gsc_collect_data.py --token YOUR_ACCESS_TOKEN --site sc-domain:domain.com

Зависимости:
    pip install requests
"""

import requests
import json
import argparse
from datetime import datetime, timedelta


class GSCCollector:
    """Сборщик данных из Google Search Console API v3"""
    
    BASE_URL = "https://www.googleapis.com/webmasters/v3"
    INSPECT_URL = "https://searchconsole.googleapis.com/v1"

    def __init__(self, access_token):
        self.access_token = access_token
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

    def _get(self, url, params=None):
        """GET запрос с обработкой ошибок"""
        r = requests.get(url, headers=self.headers, params=params)
        if r.status_code == 401:
            raise Exception("Токен истёк или невалиден. Обновите access_token.")
        r.raise_for_status()
        return r.json()

    def _post(self, url, payload):
        """POST запрос с обработкой ошибок"""
        r = requests.post(url, headers=self.headers, json=payload)
        if r.status_code == 401:
            raise Exception("Токен истёк или невалиден. Обновите access_token.")
        if r.status_code == 403:
            raise Exception("Нет доступа к свойству. Добавьте аккаунт в GSC.")
        r.raise_for_status()
        return r.json()

    def get_sites(self):
        """Получить список доступных сайтов"""
        data = self._get(f"{self.BASE_URL}/sites")
        return data.get('siteEntry', [])

    def search_analytics(self, site_url, start_date, end_date,
                         dimensions=None, row_limit=1000,
                         search_type='web', start_row=0):
        """Запрос аналитики поиска"""
        payload = {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": dimensions or [],
            "rowLimit": row_limit,
            "startRow": start_row,
            "searchType": search_type,
            "dataState": "final"
        }
        data = self._post(
            f"{self.BASE_URL}/sites/{site_url}/searchAnalytics/query",
            payload
        )
        return data.get('rows', [])

    def get_queries(self, site_url, start_date, end_date, limit=1000):
        """Топ поисковых запросов"""
        print(f"  Загрузка запросов ({start_date} — {end_date})...")
        rows = self.search_analytics(
            site_url, start_date, end_date,
            dimensions=["query"], row_limit=limit
        )
        print(f"  → {len(rows)} запросов")
        return rows

    def get_pages(self, site_url, start_date, end_date, limit=1000):
        """Топ страниц"""
        print(f"  Загрузка страниц...")
        rows = self.search_analytics(
            site_url, start_date, end_date,
            dimensions=["page"], row_limit=limit
        )
        print(f"  → {len(rows)} страниц")
        return rows

    def get_queries_pages(self, site_url, start_date, end_date, limit=5000):
        """Запросы + страницы (для каннибализации)"""
        print(f"  Загрузка запрос+страница...")
        rows = self.search_analytics(
            site_url, start_date, end_date,
            dimensions=["query", "page"], row_limit=limit
        )
        print(f"  → {len(rows)} комбинаций")
        return rows

    def get_dates(self, site_url, start_date, end_date):
        """Данные по датам (динамика)"""
        print(f"  Загрузка динамики по дням...")
        rows = self.search_analytics(
            site_url, start_date, end_date,
            dimensions=["date"]
        )
        print(f"  → {len(rows)} дней")
        return rows

    def get_devices(self, site_url, start_date, end_date):
        """Данные по устройствам"""
        print(f"  Загрузка данных по устройствам...")
        rows = self.search_analytics(
            site_url, start_date, end_date,
            dimensions=["device"]
        )
        print(f"  → {len(rows)} типов устройств")
        return rows

    def get_search_appearance(self, site_url, start_date, end_date):
        """Данные по типу выдачи (AMP, рич-результаты и т.д.)"""
        print(f"  Загрузка данных по типу выдачи...")
        rows = self.search_analytics(
            site_url, start_date, end_date,
            dimensions=["searchAppearance"]
        )
        print(f"  → {len(rows)} типов")
        return rows

    def get_sitemaps(self, site_url):
        """Список sitemap и их статус"""
        print(f"  Загрузка sitemap...")
        data = self._get(f"{self.BASE_URL}/sites/{site_url}/sitemaps")
        sitemaps = data.get('sitemap', [])
        print(f"  → {len(sitemaps)} sitemap")
        return sitemaps

    def inspect_url(self, site_url, inspection_url):
        """Инспекция конкретного URL"""
        payload = {
            "inspectionUrl": inspection_url,
            "siteUrl": site_url
        }
        try:
            data = self._post(
                f"{self.INSPECT_URL}/urlInspection/index:inspect",
                payload
            )
            return data
        except Exception as e:
            return {"error": str(e)}

    def collect_all(self, site_url, days=90):
        """Сбор всех данных за период"""
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        
        print(f"\n{'='*60}")
        print(f"GSC Data Collector")
        print(f"Свойство: {site_url}")
        print(f"Период: {start_date} — {end_date} ({days} дней)")
        print(f"{'='*60}\n")

        data = {
            'site': site_url,
            'period': {'start': start_date, 'end': end_date},
            'collected_at': datetime.now().isoformat()
        }

        print("[1/7] Список сайтов...")
        try:
            sites = self.get_sites()
            data['sites'] = sites
            for s in sites:
                print(f"  {s.get('siteUrl', '?')} — {s.get('permissionLevel', '?')}")
        except Exception as e:
            print(f"  Ошибка: {e}")
            data['sites'] = []

        print(f"\n[2/7] Запросы...")
        data['queries'] = self.get_queries(site_url, start_date, end_date)

        print(f"\n[3/7] Страницы...")
        data['pages'] = self.get_pages(site_url, start_date, end_date)

        print(f"\n[4/7] Каннибализация (запрос + страница)...")
        data['queries_pages'] = self.get_queries_pages(site_url, start_date, end_date)

        print(f"\n[5/7] Динамика по дням...")
        data['dates'] = self.get_dates(site_url, start_date, end_date)

        print(f"\n[6/7] Устройства...")
        data['devices'] = self.get_devices(site_url, start_date, end_date)

        print(f"\n[7/7] Sitemap...")
        data['sitemaps'] = self.get_sitemaps(site_url)

        # Сводка
        total_clicks = sum(r.get('clicks', 0) for r in data['queries'])
        total_impressions = sum(r.get('impressions', 0) for r in data['queries'])
        avg_ctr = (total_clicks / total_impressions * 100) if total_impressions > 0 else 0
        avg_position = (
            sum(r.get('position', 0) * r.get('impressions', 0) for r in data['queries']) 
            / total_impressions
        ) if total_impressions > 0 else 0

        data['summary'] = {
            'total_clicks': total_clicks,
            'total_impressions': total_impressions,
            'avg_ctr': round(avg_ctr, 2),
            'avg_position': round(avg_position, 1),
            'unique_queries': len(data['queries']),
            'unique_pages': len(data['pages']),
            'cannibalization_pairs': len(data['queries_pages'])
        }

        print(f"\n{'='*60}")
        print("СВОДКА GSC")
        print(f"{'='*60}")
        print(f"  Кликов:          {data['summary']['total_clicks']}")
        print(f"  Показов:         {data['summary']['total_impressions']}")
        print(f"  Средний CTR:     {data['summary']['avg_ctr']}%")
        print(f"  Средняя позиция: {data['summary']['avg_position']}")
        print(f"  Запросов:        {data['summary']['unique_queries']}")
        print(f"  Страниц:         {data['summary']['unique_pages']}")
        print(f"{'='*60}\n")

        return data

    def format_queries_table(self, queries, limit=20):
        """Форматирует запросы в Markdown-таблицу"""
        lines = [
            "| # | Запрос | Клики | Показы | CTR | Позиция |",
            "|---|---|---|---|---|---|"
        ]
        for i, q in enumerate(queries[:limit], 1):
            query = q['keys'][0] if q.get('keys') else '?'
            clicks = q.get('clicks', 0)
            impressions = q.get('impressions', 0)
            ctr = q.get('ctr', 0) * 100
            position = q.get('position', 0)
            lines.append(
                f"| {i} | {query} | {clicks} | {impressions:,} | {ctr:.1f}% | {position:.1f} |"
            )
        return '\n'.join(lines)

    def format_pages_table(self, pages, limit=15):
        """Форматирует страницы в Markdown-таблицу"""
        lines = [
            "| # | Страница | Клики | Показы | CTR | Позиция |",
            "|---|---|---|---|---|---|"
        ]
        for i, p in enumerate(pages[:limit], 1):
            page = p['keys'][0] if p.get('keys') else '?'
            # Сокращаем URL
            page = page.replace('https://', '').replace('http://', '')
            if len(page) > 60:
                page = page[:57] + '...'
            clicks = p.get('clicks', 0)
            impressions = p.get('impressions', 0)
            ctr = p.get('ctr', 0) * 100
            position = p.get('position', 0)
            lines.append(
                f"| {i} | {page} | {clicks} | {impressions:,} | {ctr:.1f}% | {position:.1f} |"
            )
        return '\n'.join(lines)

    def format_devices_table(self, devices):
        """Форматирует устройства в Markdown-таблицу"""
        lines = [
            "| Устройство | Клики | Показы | CTR | Позиция |",
            "|---|---|---|---|---|"
        ]
        for d in devices:
            device = d['keys'][0] if d.get('keys') else '?'
            clicks = d.get('clicks', 0)
            impressions = d.get('impressions', 0)
            ctr = d.get('ctr', 0) * 100
            position = d.get('position', 0)
            lines.append(
                f"| {device} | {clicks} | {impressions:,} | {ctr:.1f}% | {position:.1f} |"
            )
        return '\n'.join(lines)

    def find_cannibalization(self, queries_pages, min_impressions=10):
        """Находит каннибализацию: один запрос → несколько страниц"""
        from collections import defaultdict
        
        query_pages = defaultdict(list)
        for row in queries_pages:
            keys = row.get('keys', [])
            if len(keys) >= 2:
                query = keys[0]
                page = keys[1]
                impressions = row.get('impressions', 0)
                if impressions >= min_impressions:
                    query_pages[query].append({
                        'page': page,
                        'clicks': row.get('clicks', 0),
                        'impressions': impressions,
                        'position': row.get('position', 0)
                    })
        
        # Оставляем только запросы с несколькими страницами
        cannibalization = {
            q: pages for q, pages in query_pages.items()
            if len(pages) > 1
        }
        
        return cannibalization


def main():
    parser = argparse.ArgumentParser(description='Сбор данных из Google Search Console')
    parser.add_argument('--token', required=True, help='Access Token OAuth 2.0')
    parser.add_argument('--site', required=True, help='Свойство GSC (например: sc-domain:domain.com)')
    parser.add_argument('--days', type=int, default=90, help='Количество дней для анализа (по умолчанию: 90)')
    parser.add_argument('--output', default=None, help='Файл для сохранения JSON (по умолчанию: gsc_data_{domain}.json)')
    args = parser.parse_args()

    collector = GSCCollector(args.token)
    data = collector.collect_all(args.site, days=args.days)

    # Определяем имя файла
    if args.output:
        output_file = args.output
    else:
        domain = args.site.replace('sc-domain:', '').replace('https://', '').replace('http://', '').replace('/', '').replace('.', '_')
        output_file = f"gsc_data_{domain}.json"

    # Сохраняем
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Результат сохранён: {output_file}")

    # Каннибализация
    cannibalization = collector.find_cannibalization(data.get('queries_pages', []))
    if cannibalization:
        print(f"\n⚠️  Найдена каннибализация: {len(cannibalization)} запросов")
        for query, pages in list(cannibalization.items())[:5]:
            print(f"  «{query}»:")
            for p in pages:
                print(f"    → {p['page'][:60]} (позиция {p['position']:.1f})")
    
    return data


if __name__ == '__main__':
    main()