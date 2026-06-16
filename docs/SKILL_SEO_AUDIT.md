# SKILL: Комплексный SEO-аудит сайта

## Описание

Полный алгоритм проведения технического SEO-аудита любого сайта. Включает сбор данных, анализ, интеграцию с Google Search Console и формирование отчёта. Результат — готовый Markdown-отчёт с приоритизированными рекомендациями.

---

## Входные данные

От пользователя требуется:
- **URL сайта** (домен)
- **Логин/пароль или токен** Google Search Console (опционально, для данных GSC)
- **Токен Яндекс.Вебмастера** (опционально)
- **Целевой рынок / гео** (город, регион)
- **Ниша / вид деятельности** (например: аутсорсинг, ecommerce, SaaS)

---

## Фаза 0: Сбор технических данных с сайта

### Шаг 0.1: Проверка robots.txt

**Цель:** Понять, что закрыто от индексации.

```
GET https://{domain}/robots.txt
```

**Что анализировать:**
- Какие директории заблокированы (`Disallow`)
- Блокируются ли CSS/JS файлы (критическая проблема для рендеринга Googlebot)
- Указан ли `Sitemap` с корректным URL
- Есть ли `Allow` для важных ресурсов
- Есть ли блокировки для User-agent: Googlebot / Yandex

**Типичные проблемы:**
- `Disallow: /*.css$` и `Disallow: /*.js$` — блокируют рендеринг
- Нет `Disallow` для служебных/тестовых страниц
- Нет указания на все sitemap-файлы
- Слишком агрессивные блокировки

### Шаг 0.2: Проверка sitemap.xml

**Цель:** Понять, какие URL сайт отправляет в поисковики.

```
GET https://{domain}/sitemap.xml
GET https://{domain}/sitemap_index.xml
```

**Что анализировать:**
- Содержит ли sitemap главную страницу `/`
- Есть ли все реальные страницы сайта
- Нет ли в sitemap тестовых/служебных URL
- Нет ли в sitemap дублирующих URL
- Структура: один файл или sitemap index с подфайлами
- Количество URL в каждом подфайле
- Соответствие `lastmod` реальности

**Типичные проблемы:**
- Главная страница отсутствует
- Тестовые товары/страницы в sitemap
- Дублирующие URL (с суффиксами)
- Служебные страницы CMS (page*.html у Tilda)
- Устаревшие или несуществующие URL

### Шаг 0.3: Проверка HTTP-статусов ключевых URL

**Цель:** Убедиться, что страницы доступны и не имеют редиректов.

Собрать все URL из sitemap + проверить потенциальные дубли:

```python
import requests

urls = [
    "https://{domain}/",
    "https://{domain}/robots.txt",
    "https://{domain}/sitemap.xml",
    # + все URL из sitemap
    # + потенциальные дубли (с суффиксами, альтернативные пути)
]

for url in urls:
    r = requests.get(url, allow_redirects=True, timeout=10)
    print(f"{r.status_code} | {url} | final: {r.url}")
```

**Что анализировать:**
- Страницы отдают 200, которые должны быть закрыты (дубли, тестовые)
- Страницы отдают 301/302 — цепочки редиректов
- Страницы отдают 404 — битые ссылки
- Страницы отдают 500 — серверные ошибки

### Шаг 0.4: Анализ HTML-разметки

**Цель:** Проверить мета-теги, canonical, OG-теги, schema.

Для каждой ключевой страницы скачать HTML и извлечь:

```python
from bs4 import BeautifulSoup
import requests

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# Title
title = soup.find('title').text if soup.find('title') else 'НЕТ'

# Description
desc_tag = soup.find('meta', attrs={'name': 'description'})
description = desc_tag['content'] if desc_tag else 'НЕТ'

# Canonical
canonical_tag = soup.find('link', attrs={'rel': 'canonical'})
canonical = canonical_tag['href'] if canonical_tag else 'НЕТ'

# H1
h1_tags = [h1.text.strip() for h1 in soup.find_all('h1')]

# OG-теги
og_tags = {}
for og in soup.find_all('meta', attrs={'property': lambda x: x and x.startswith('og:')}):
    og_tags[og['property']] = og.get('content', '')

# Schema.org (JSON-LD)
import json
schemas = []
for script in soup.find_all('script', type='application/ld+json'):
    try:
        schemas.append(json.loads(script.string))
    except:
        pass

# Robots meta
robots_tag = soup.find('meta', attrs={'name': 'robots'})
robots = robots_tag['content'] if robots_tag else 'НЕТ'

# Hreflang
hreflangs = soup.find_all('link', attrs={'rel': 'alternate', 'hreflang': True})

# Изображения без alt
images_no_alt = [img for img in soup.find_all('img') if not img.get('alt')]
```

**Что сохранять для каждой страницы:**
| Поле | Пример |
|---|---|
| URL | /proizvodstvo |
| HTTP статус | 200 |
| Title | Аутсорсинг персонала — Sequoia Service |
| Description | ... |
| Canonical | https://domain/page |
| H1 | Аутсорсинг персонала |
| Noindex | Да/Нет |
| OG:url | ... |
| Schema.org | Нет / Organization / ... |
| Hreflang | Нет |
| Изображений без alt | 5 |

### Шаг 0.5: Поиск дублей и потенциальных дублей

**Цель:** Найти страницы-дубли, которые размывают индекс.

**Методология:**
1. Проверить типичные паттерны дублей платформы (для Tilda: суффиксы "2", "3", page*.html)
2. Сравнить title + description дублирующих пар
3. Проверить canonical на каждой странице дубля
4. Найти внутренние ссылки, ведущие на дубли вместо оригиналов

**Паттерны для проверки (платформо-зависимые):**

| Платформа | Типичные дубли |
|---|---|
| Tilda | page*.html, URL с суффиксами 2/3, tproduct/*, /blog/3192789.html |
| WordPress | /category/page, /tag/page, ?replytocom=, feed URLs |
| Bitrix | /bitrix/, /index.php, параметры сессий |
| 1С-Битрикс | /catalog/, дубли через компоненты |
| Shopify | /collections/, /products/ дубли |
| Кастомная | Проверить sitemap vs реальные ссылки |

### Шаг 0.6: Проверка внутренней перелинковки

**Цель:** Оценить структуру внутренних ссылок.

Для главной страницы и ключевых страниц:
1. Извлечь все внутренние ссылки (`<a href>`)
2. Проверить, ведут ли ссылки на дубли
3. Оценить наличие ссылок на важные страницы (блог, контакты, услуги)
4. Проверить наличие «хлебных крошек»
5. Найти «сиротские» страницы (без входящих ссылок)

### Шаг 0.7: Проверка PageSpeed (опционально)

```
GET https://pagespeed.web.dev/analysis?url=https://{domain}/
```

Или через API:
```
GET https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://{domain}/&strategy=mobile
```

**Что анализировать:**
- LCP (Largest Contentful Paint) — < 2.5с
- FID/INP (First Input Delay / Interaction to Next Paint) — < 100мс / < 200мс
- CLS (Cumulative Layout Shift) — < 0.1
- TTFB (Time to First Byte) — < 800мс
- Оптимизация изображений
- Минификация CSS/JS

---

## Фаза 1: Сбор данных Google Search Console

### Шаг 1.1: Настройка доступа к GSC

**Вариант A: OAuth 2.0 (ручной токен)**

1. Создать проект в Google Cloud Console
2. Включить Google Search Console API
3. Создать OAuth 2.0 Client ID (тип: Web application)
4. Получить authorization code через OAuth Playground или вручную
5. Обменять code на access_token + refresh_token
6. Сохранить refresh_token для повторного использования

**Вариант B: Service Account**

1. Создать Service Account в Google Cloud
2. Скачать JSON-ключ
3. Добавить email сервис-аккаунта как пользователя GSC
4. Использовать JWT для получения access_token

**Scopes:**
- `https://www.googleapis.com/auth/webmasters.readonly` — для чтения данных
- `https://www.googleapis.com/auth/webmasters` — для отправки sitemap

### Шаг 1.2: Определить свойство в GSC

```python
import requests

# Список доступных сайтов
r = requests.get(
    "https://www.googleapis.com/webmasters/v3/sites",
    headers={"Authorization": f"Bearer {access_token}"}
)
sites = r.json()

# Свойство может быть:
# - sc-domain:domain.com (domain property)
# - https://domain.com/ (URL prefix)
# - http://domain.com/ (URL prefix)
```

### Шаг 1.3: Сбор данных по запросам (queries)

```python
# Общая статистика (90 дней)
payload = {
    "startDate": "2026-02-13",
    "endDate": "2026-05-13",
    "dimensions": ["query"],
    "rowLimit": 1000,
    "dataState": "final"
}

r = requests.post(
    f"https://www.googleapis.com/webmasters/v3/sites/{site_url}/searchAnalytics/query",
    headers={"Authorization": f"Bearer {access_token}"},
    json=payload
)
queries = r.json()
```

**Что сохранять:**
- Запрос, клики, показы, CTR, позиция
- Отсортировать по кликам (DESC)
- Выделить: брендовые, информационные, коммерческие запросы

### Шаг 1.4: Сбор данных по страницам

```python
payload = {
    "startDate": "2026-02-13",
    "endDate": "2026-05-13",
    "dimensions": ["page"],
    "rowLimit": 1000,
    "dataState": "final"
}
```

**Что сохранять:**
- Страница, клики, показы, CTR, позиция
- Определить, какие страницы получают трафик, а какие нет
- Найти страницы с высокими показами, но низким CTR (потенциал роста)

### Шаг 1.5: Сбор данных «запрос + страница» (каннибализация)

```python
payload = {
    "startDate": "2026-02-13",
    "endDate": "2026-05-13",
    "dimensions": ["query", "page"],
    "rowLimit": 5000,
    "dataState": "final"
}
```

**Что анализировать:**
- Один запрос → несколько страниц = каннибализация
- Страница, которая ранжируется не по назначению (главная вместо страницы услуги)

### Шаг 1.6: Сбор данных по датам (динамика)

```python
payload = {
    "startDate": "2026-02-13",
    "endDate": "2026-05-13",
    "dimensions": ["date"],
    "dataState": "final"
}
```

**Что анализировать:**
- Тренды: рост/падение кликов
- Сезонность
- Влияние обновлений (Google Core Updates)

### Шаг 1.7: Сбор данных по устройствам

```python
payload = {
    "startDate": "2026-02-13",
    "endDate": "2026-05-13",
    "dimensions": ["device"],
    "dataState": "final"
}
```

**Что анализировать:**
- Разница CTR между mobile и desktop
- Разница позиций между устройствами

### Шаг 1.8: Проверка sitemap в GSC

```python
# Список sitemap
r = requests.get(
    f"https://www.googleapis.com/webmasters/v3/sites/{site_url}/sitemaps",
    headers={"Authorization": f"Bearer {access_token}"}
)
sitemaps = r.json()
```

**Что анализировать:**
- Сколько URL отправлено vs индексировано
- Дата последнего сканирования
- Ошибки в sitemap

### Шаг 1.9: Проверка ошибок сканирования (Inspect URL)

```python
# Инспекция конкретного URL
payload = {
    "inspectionUrl": "https://domain.com/page",
    "siteUrl": "sc-domain:domain.com"
}

r = requests.post(
    "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect",
    headers={"Authorization": f"Bearer {access_token}"},
    json=payload
)
```

**Что анализировать:**
- Статус индексации (indexed, not indexed, crawled)
- Последнее сканирование
- Статус мобильной версии
- Наличие canonical, noindex

---

## Фаза 2: Анализ и формирование отчёта

### Структура отчёта

Отчёт формируется в Markdown и содержит:

```
# SEO-АУДИТ САЙТА {DOMAIN}

**Дата аудита:** {DATE}
**Домен:** {DOMAIN}
**Платформа:** {PLATFORM}
**Целевой рынок:** {GEO}
**Ниша:** {NICHE}

---

## ОГЛАВЛЕНИЕ
1. Резюме (Executive Summary)
2. Данные Google Search Console
3. Индексация и Crawl Budget
4. Дублирование контента и каннибализация
5. Sitemap.xml — ошибки
6. Robots.txt — анализ
7. Мета-теги и on-page SEO
8. Структурированные данные (Schema.org)
9. Hreflang и мультиязычность
10. Внутренняя перелинковка
11. Технические проблемы
12. Контент-анализ страниц
13. План исправлений (приоритизированный)
14. Чек-лист для реализации

ПРИЛОЖЕНИЕ A: Список всех найденных URL
ПРИЛОЖЕНИЕ B: Техническая информация
```

### Раздел 1: Резюме

**Что включать:**
- Общая оценка: 🟢 / 🟡 / 🔴 (по шкале критичности)
- 1-2 предложения о главной проблеме
- Таблица «Ключевые метрики» с оценкой каждого параметра

**Шкала оценок:**
- 🟢 НОРМА — нет критических проблем
- 🟡 ТРЕБУЕТ ВНИМАНИЯ — есть проблемы средней серьёзности
- 🔴 КРИТИЧНО — требует немедленного исправления

### Раздел 2: Данные Google Search Console

**Подразделы:**
1. Общая статистика (клики, показы, CTR, позиция)
2. Топ-20 запросов по кликам (таблица)
3. Ключевые наблюдения по запросам (брендовые / информационные / коммерческие)
4. Топ-15 страниц по кликам (таблица)
5. Ключевые наблюдения по страницам
6. Динамика по месяцам (таблица)
7. Разбивка по устройствам (таблица)
8. Sitemap в GSC
9. Каннибализация по данным GSC

### Раздел 3: Индексация и Crawl Budget

**Что включать:**
- Список мусорных/тестовых URL в индексе
- Список дублей в индексе
- Служебные страницы CMS
- Подсчёт «лишних» URL
- Влияние на crawl budget

### Раздел 4: Дублирование контента и каннибализация

**Что включать:**
- Таблица сравнения оригинала и дубля (HTTP, Title, Description, Canonical, Noindex)
- Список всех найденных пар дублей
- Подтверждение каннибализации (из GSC и внутренних ссылок)

### Раздел 5: Sitemap.xml

**Что включать:**
- Список URL в sitemap
- Отсутствующие URL
- Тестовые/мусорные URL в sitemap
- Рекомендации по исправлению

### Раздел 6: Robots.txt

**Что включать:**
- Текущее содержимое (ключевые строки)
- Таблица проблем с серьёзностью
- Подробное объяснение критических проблем
- Рекомендуемое содержимое robots.txt

### Раздел 7: Мета-теги и on-page SEO

**Что включать:**
- Таблица дублированных Title
- Проблемы Title (слишком короткие/длинные, без гео, без ключевых слов)
- Проблемы Description
- OG-теги
- Canonical
- Рекомендации по Title (таблица: текущий → рекомендуемый)

### Раздел 8: Schema.org

**Что включать:**
- Текущее состояние (отсутствует / частично)
- Что необходимо внедрить (с примерами JSON-LD):
  - Organization / LocalBusiness
  - Service (для страниц услуг)
  - Product (для ecommerce)
  - FAQPage
  - BreadcrumbList
  - Article (для блога)

### Раздел 9: Hreflang

**Что включать:**
- Есть/нет hreflang
- Нужен ли (только для мультиязычных сайтов)
- Рекомендации по реализации

### Раздел 10: Внутренняя перелинковка

**Что включать:**
- Список ссылок с главной страницы
- Проблемы (ссылки на дубли, отсутствие ссылок на ключевые страницы)
- Рекомендации

### Раздел 11: Технические проблемы

**Что включать:**
- Каждая проблема как отдельный подраздел
- Описание проблемы + влияние + решение
- Типичные проблемы:
  - Блокировка CSS/JS в robots.txt
  - Большие HTML-страницы
  - Служебные страницы в индексе
  - Redirect chains
  - Отсутствие 404
  - Mixed content
  - Медленная загрузка

### Раздел 12: Контент-анализ

**Что включать:**
- Анализ каждой ключевой страницы:
  - Title, H1, контент
  - Проблемы (нет текста, нет гео, нет ключевых слов)
  - Рекомендации

### Раздел 13: План исправлений

**Структура приоритетов:**

| Приоритет | Срок | Примеры |
|---|---|---|
| 🔴 Критический | Неделя 1 | Дубли, robots.txt, тестовые страницы |
| 🟡 Высокий | Неделя 2 | Sitemap, canonical, Schema.org |
| 🟢 Средний | Недели 3-4 | Title, перелинковка, alt-теги |
| ⚪ Низкий | Месяц 2+ | Новый контент, расширение гео |

### Раздел 14: Чек-лист

**Группировка по срокам:**
- Немедленные действия (неделя 1)
- В течение 2 недель
- В течение месяца
- Мониторинг (постоянно)

### Приложения

**Приложение A: Список URL**
- Основные страницы (таблица: URL, sitemap, HTTP, примечание)
- Дублирующие страницы
- Тестовые/мусорные страницы

**Приложение B: Техническая информация**
- Платформа, CDN
- Верификация Яндекс/Google
- GSC-доступ
- Sitemap в GSC

---

## Фаза 3: Специфика по платформам

### Tilda

**Типичные проблемы:**
- Страницы-дубли с суффиксами (2, 3, 4...)
- page*.html внутренние страницы
- tproduct/* тестовые товары из Tilda Store
- /blog/3192789.html — redirect с /blog
- robots.txt блокирует CSS/JS
- Нет Schema.org из коробки
- og:url не обновляется при дублировании
- Canonical на себя даже у дублей

**Что проверять дополнительно:**
- /tproduct/* в sitemap-store.xml
- page*.html страницы
- Наличие tilda-hreflang скрипта (установлен, но не работает)

### WordPress

**Типичные проблемы:**
- Дубли через /category/ и /tag/
- ?replytocom= параметры
- /feed/ URL
- /wp-json/ API endpoints в индексе
- Дубли пагинации (/page/2/, /page/3/)
- Attachment pages (/attachment_id/)
- Авторские архивы

**Что проверять дополнительно:**
- Yoast/RankMath настройки noindex
- robots.txt (Disallow: /wp-admin/, Allow: /wp-admin/admin-ajax.php)
- XML Sitemap плагина

### 1С-Битрикс

**Типичные проблемы:**
- Дубли через SEO-фильтры
- Параметры сессий в URL (/bitrix/)
- Дубли через компоненты каталога
- /index.php vs /

### Shopify

**Типичные проблемы:**
- /collections/all
- Дубли /products/ через коллекции
- Параметры ?variant=
- /pages/ vs /

### Кастомная разработка

**Что проверять:**
- htaccess/nginx конфигурацию
- Параметры (?sort=, ?filter=, ?page=)
- API endpoints
- Служебные пути (/admin/, /api/, /debug/)

---

## Фаза 4: Генерация Schema.org (примеры)

### Organization (для всех страниц)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Название компании",
  "url": "https://domain.com",
  "logo": "https://domain.com/logo.png",
  "sameAs": [
    "https://vk.com/company",
    "https://t.me/company"
  ],
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Москва",
    "addressCountry": "RU",
    "streetAddress": "ул. Примерная, д. 1"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+7-XXX-XXX-XX-XX",
    "contactType": "customer service",
    "availableLanguage": "Russian"
  }
}
```

### LocalBusiness (для бизнеса с физическим адресом)

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Название",
  "image": "https://domain.com/photo.jpg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "ул. Примерная, д. 1",
    "addressLocality": "Москва",
    "postalCode": "123456",
    "addressCountry": "RU"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 55.7558,
    "longitude": 37.6173
  },
  "telephone": "+7-XXX-XXX-XX-XX",
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "09:00",
    "closes": "18:00"
  },
  "priceRange": "$$"
}
```

### Service (для страниц услуг)

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Аутсорсинг персонала на производство",
  "provider": {
    "@type": "Organization",
    "name": "Название компании"
  },
  "areaServed": {
    "@type": "Country",
    "name": "RU"
  },
  "description": "Описание услуги",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "RUB",
    "description": "Цена по запросу"
  }
}
```

### Product (для ecommerce)

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Название товара",
  "image": "https://domain.com/product.jpg",
  "description": "Описание",
  "brand": {
    "@type": "Brand",
    "name": "Бренд"
  },
  "offers": {
    "@type": "Offer",
    "priceCurrency": "RUB",
    "price": "1000",
    "availability": "https://schema.org/InStock",
    "seller": {
      "@type": "Organization",
      "name": "Название магазина"
    }
  }
}
```

### FAQPage (для FAQ-блоков)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Вопрос 1?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ответ 1."
      }
    },
    {
      "@type": "Question",
      "name": "Вопрос 2?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ответ 2."
      }
    }
  ]
}
```

### BreadcrumbList

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Главная",
      "item": "https://domain.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Услуги",
      "item": "https://domain.com/services"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Аутсорсинг на производство"
    }
  ]
}
```

### Article (для блога)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Заголовок статьи",
  "image": "https://domain.com/article-image.jpg",
  "author": {
    "@type": "Person",
    "name": "Имя автора"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Название компании",
    "logo": {
      "@type": "ImageObject",
      "url": "https://domain.com/logo.png"
    }
  },
  "datePublished": "2026-01-15",
  "dateModified": "2026-05-01",
  "description": "Краткое описание статьи"
}
```

---

## Фаза 5: Рекомендации по robots.txt (шаблоны)

### Базовый шаблон

```
User-agent: *
Allow: /

# Служебные директории
Disallow: /admin/
Disallow: /wp-admin/
Disallow: /bitrix/

# Тестовые/служебные страницы
Disallow: /tproduct/
Disallow: /page*.html$
Disallow: /*3$

# Служебные файлы
Disallow: /*.css$   # НЕ ДЕЛАТЬ ЭТОГО для Tilda!
Disallow: /*.js$    # НЕ ДЕЛАТЬ ЭТОГО для Tilda!

# Sitemap
Sitemap: https://domain.com/sitemap.xml
Sitemap: https://domain.com/sitemap-posts.xml
Sitemap: https://domain.com/sitemap-pages.xml
```

### Для Tilda

```
User-agent: *
Allow: /
Disallow: /tproduct/
Disallow: /page*.html$
Disallow: /*3$
Disallow: /nizhnij-novgorod2$
Disallow: /tilda/
Allow: /tildaspec.js

Sitemap: https://domain.com/sitemap.xml
Sitemap: https://domain.com/sitemap-store.xml
Sitemap: https://domain.com/sitemap-feeds.xml
```

### Для WordPress

```
User-agent: *
Allow: /
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
Disallow: /wp-includes/
Disallow: /?s=
Disallow: /search/
Disallow: /tag/
Disallow: /category/
Disallow: /author/
Disallow: /feed/
Disallow: */trackback/
Disallow: */embed/
Disallow: /xmlrpc.php

Sitemap: https://domain.com/sitemap_index.xml
```

---

## Фаза 6: Рекомендации по Title и Description

### Формулы Title

**Для услуг:**
```
{Тип услуги} в {Гео} — {Бренд}
```
Пример: `Аутсорсинг персонала на производство в Москве — Sequoia Service`

**Для ecommerce:**
```
{Категория товаров} — купить в {Гео} | {Бренд}
```
Пример: `Спортивная обувь — купить в Москве | SportShop`

**Для блога:**
```
{Заголовок статьи} | Блог {Бренд}
```
Пример: `Что такое индекс Хедхантера | Блог Sequoia Service`

**Для гео-страниц:**
```
{Услуга} в {Гео} — {Бренд}
```
Пример: `Аутсорсинг персонала в Нижнем Новгороде — Sequoia Service`

### Формулы Description

```
{Услуга/Товар} в {Гео}. {Краткое описание с УТП}. {Призыв к действию}. ☎ {Телефон}
```
Пример: `Аутсорсинг персонала на производство в Москве. Подбор и обучение сотрудников за 5 дней. Оставьте заявку на сайте. ☎ +7-XXX-XXX-XX-XX`

### Длина

| Элемент | Минимум | Рекомендуется | Максимум |
|---|---|---|---|
| Title | 30 символов | 50-60 символов | 70 символов |
| Description | 70 символов | 120-155 символов | 160 символов |

---

## Чек-лист: что проверять в каждом аудите

### Техническое SEO
- [ ] robots.txt — нет блокировок CSS/JS
- [ ] robots.txt — заблокированы служебные/тестовые страницы
- [ ] robots.txt — указаны все sitemap
- [ ] sitemap.xml — содержит все реальные страницы
- [ ] sitemap.xml — НЕ содержит тестовые/дублирующие страницы
- [ ] HTTP 200 — только для реальных страниц
- [ ] 301 редиректы — настроены для дублей
- [ ] 404 — кастомная страница существует
- [ ] HTTPS — работает на всех страницах
- [ ] Mixed content — нет HTTP-ресурсов на HTTPS-страницах
- [ ] Redirect chains — нет цепочек > 2 редиректов
- [ ] PageSpeed — LCP < 2.5с, CLS < 0.1, INP < 200мс

### On-page SEO
- [ ] Title — уникален на каждой странице
- [ ] Title — содержит ключевое слово + гео
- [ ] Title — 50-60 символов
- [ ] Description — уникален на каждой странице
- [ ] Description — содержит УТП + призыв
- [ ] Description — 120-155 символов
- [ ] H1 — один на страницу
- [ ] H1 — соответствует Title
- [ ] Canonical — указан на каждой странице
- [ ] Canonical — дубли указывают на оригинал
- [ ] OG-теги — заполнены (title, description, image, url)
- [ ] Alt-теги — на всех изображениях
- [ ] Schema.org — JSON-LD на каждой странице
- [ ] Hreflang — если мультиязычный сайт

### Контент
- [ ] Уникальный текст на каждой странице
- [ ] Ключевые слова в тексте (натурально)
- [ ] Нет «пустых» страниц в индексе
- [ ] Блог перелинкован со страницами услуг
- [ ] Есть FAQ-блоки на коммерческих страницах

### Перелинковка
- [ ] Главная ссылается на все ключевые страницы
- [ ] Нет ссылок на дубли
- [ ] Хлебные крошки (Breadcrumbs)
- [ ] Блог → Услуги (перелинковка)
- [ ] Нет «сиротских» страниц

### GSC
- [ ] Sitemap отправлен и обработан
- [ ] Нет ошибок сканирования
- [ ] Нет ручных санкций
- [ ] Каннибализация запросов устранена
- [ ] CTR оптимизирован (Title/Description привлекательны)

---

## Скрипт: Сбор данных с сайта (Python)

```python
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
            self.results['robots_txt'] = {
                'url': url,
                'status': r.status_code,
                'content': r.text if r.status_code == 200 else None,
                'blocks_css': '/*.css$' in r.text if r.status_code == 200 else False,
                'blocks_js': '/*.js$' in r.text if r.status_code == 200 else False,
                'sitemap_urls': [
                    line.split(': ', 1)[1].strip()
                    for line in r.text.split('\n')
                    if line.lower().startswith('sitemap:')
                ] if r.status_code == 200 else []
            }
        except Exception as e:
            self.results['robots_txt'] = {'error': str(e)}

    def collect_sitemap_urls(self, sitemap_url, depth=0):
        """Рекурсивно собирает URL из sitemap"""
        if depth > 5:
            return []
        urls = []
        try:
            r = self.session.get(sitemap_url, timeout=15)
            if r.status_code != 200:
                return urls
            root = ET.fromstring(r.content)
            ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            # Sitemap index
            for sitemap in root.findall('.//sm:sitemap/sm:loc', ns):
                urls.extend(self.collect_sitemap_urls(sitemap.text, depth + 1))
            # URL entries
            for loc in root.findall('.//sm:url/sm:loc', ns):
                urls.append(loc.text)
        except Exception as e:
            self.results['issues'].append(f"Sitemap error ({sitemap_url}): {e}")
        return urls

    def collect_all_sitemaps(self):
        """Собирает все URL из всех sitemap"""
        sitemap_urls = self.results['robots_txt'].get('sitemap_urls', [])
        if not sitemap_urls:
            sitemap_urls = [f"{self.base}/sitemap.xml"]
        all_urls = []
        for surl in sitemap_urls:
            urls = self.collect_sitemap_urls(surl)
            self.results['sitemaps'].append({
                'url': surl,
                'urls_count': len(urls),
                'urls': urls
            })
            all_urls.extend(urls)
        return all_urls

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
            # Robots
            robots_tag = soup.find('meta', attrs={'name': 'robots'})
            if robots_tag:
                robots_content = robots_tag.get('content', '').lower()
                page_data['noindex'] = 'noindex' in robots_content
                page_data['nofollow'] = 'nofollow' in robots_content
            # OG tags
            for og in soup.find_all('meta', attrs={'property': lambda x: x and x.startswith('og:')}):
                page_data['og'][og['property']] = og.get('content', '')
            # Schema.org
            for script in soup.find_all('script', type='application/ld+json'):
                try:
                    schema = json.loads(script.string)
                    page_data['schema'].append(
                        schema.get('@type', 'unknown') if isinstance(schema, dict) else 'array'
                    )
                except:
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
            # Issues
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
        except Exception as e:
            page_data['issues'].append(f'FETCH_ERROR: {e}')
        return page_data

    def check_duplicate_candidates(self):
        """Проверяет потенциальные дубли (платформо-зависимые паттерны)"""
        candidates = [
            f"{self.base}/page1.html",
            f"{self.base}/page2.html",
            f"{self.base}/page12345678.html",
        ]
        # Для Tilda: проверяем суффиксы
        for page in self.results['pages']:
            url = page['url']
            if url.endswith('3') or url.endswith('2'):
                continue
            # Проверяем с суффиксами 2 и 3
            for suffix in ['2', '3']:
                candidate = url + suffix
                if candidate not in [p['url'] for p in self.results['pages']]:
                    candidates.append(candidate)
        # Проверяем каждый кандидат
        duplicates = []
        for url in candidates:
            try:
                r = self.session.get(url, timeout=10, allow_redirects=True)
                if r.status_code == 200:
                    duplicates.append({
                        'url': url,
                        'status': r.status_code,
                        'title': BeautifulSoup(r.text, 'html.parser').find('title').text if BeautifulSoup(r.text, 'html.parser').find('title') else None
                    })
            except:
                pass
        return duplicates

    def run_full_audit(self):
        """Запуск полного аудита"""
        print(f"[1/6] Сбор robots.txt для {self.domain}...")
        self.collect_robots_txt()
        print(f"[2/6] Сбор sitemap...")
        sitemap_urls = self.collect_all_sitemaps()
        print(f"  Найдено {len(sitemap_urls)} URL в sitemap")
        # Берём первые 50 URL для анализа
        urls_to_check = sitemap_urls[:50]
        print(f"[3/6] Анализ {len(urls_to_check)} страниц...")
        for i, url in enumerate(urls_to_check):
            print(f"  [{i+1}/{len(urls_to_check)}] {url}")
            page = self.analyze_page(url)
            self.results['pages'].append(page)
            time.sleep(0.5)  # Пауза между запросами
        print(f"[4/6] Проверка дублей...")
        duplicates = self.check_duplicate_candidates()
        self.results['duplicates_found'] = duplicates
        print(f"  Найдено {len(duplicates)} потенциальных дублей")
        print(f"[5/6] Сохранение результатов...")
        output_file = f"seo_audit_{urlparse(self.domain).netloc.replace('.', '_')}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=2)
        print(f"[6/6] Готово! Результаты в {output_file}")
        return self.results

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Использование: python seo_audit_collector.py https://domain.com")
        sys.exit(1)
    collector = SEOAuditCollector(sys.argv[1])
    collector.run_full_audit()
```

---

## Скрипт: Сбор данных GSC (Python)

```python
"""
GSC Data Collector
Собирает данные из Google Search Console через OAuth.

Использование:
    python gsc_collect_data.py

Зависимости:
    pip install requests
"""

import requests
import json
from datetime import datetime, timedelta

class GSCCollector:
    BASE_URL = "https://www.googleapis.com/webmasters/v3"
    INSPECT_URL = "https://searchconsole.googleapis.com/v1"

    def __init__(self, access_token):
        self.access_token = access_token
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

    def get_sites(self):
        """Получить список доступных сайтов"""
        r = requests.get(f"{self.BASE_URL}/sites", headers=self.headers)
        r.raise_for_status()
        return r.json().get('siteEntry', [])

    def search_analytics(self, site_url, start_date, end_date,
                         dimensions=None, row_limit=1000,
                         search_type='web', aggregation_type='auto'):
        """Запрос аналитики поиска"""
        payload = {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": dimensions or [],
            "rowLimit": row_limit,
            "searchType": search_type,
            "dataState": "final"
        }
        if aggregation_type != 'auto':
            payload["aggregationType"] = aggregation_type
        r = requests.post(
            f"{self.BASE_URL}/sites/{site_url}/searchAnalytics/query",
            headers=self.headers,
            json=payload
        )
        r.raise_for_status()
        return r.json().get('rows', [])

    def get_queries(self, site_url, start_date, end_date, limit=1000):
        """Топ запросов"""
        return self.search_analytics(
            site_url, start_date, end_date,
            dimensions=["query"], row_limit=limit
        )

    def get_pages(self, site_url, start_date, end_date, limit=1000):
        """Топ страниц"""
        return self.search_analytics(
            site_url, start_date, end_date,
            dimensions=["page"], row_limit=limit
        )

    def get_queries_pages(self, site_url, start_date, end_date, limit=5000):
        """Запросы + страницы (для каннибализации)"""
        return self.search_analytics(
            site_url, start_date, end_date,
            dimensions=["query", "page"], row_limit=limit
        )

    def get_dates(self, site_url, start_date, end_date):
        """Данные по датам"""
        return self.search_analytics(
            site_url, start_date, end_date,
            dimensions=["date"]
        )

    def get_devices(self, site_url, start_date, end_date):
        """Данные по устройствам"""
        return self.search_analytics(
            site_url, start_date, end_date,
            dimensions=["device"]
        )

    def get_sitemaps(self, site_url):
        """Список sitemap"""
        r = requests.get(
            f"{self.BASE_URL}/sites/{site_url}/sitemaps",
            headers=self.headers
        )
        r.raise_for_status()
        return r.json().get('sitemap', [])

    def collect_all(self, site_url, days=90):
        """Сбор всех данных за период"""
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        data = {
            'site': site_url,
            'period': {'start': start_date, 'end': end_date},
            'queries': self.get_queries(site_url, start_date, end_date),
            'pages': self.get_pages(site_url, start_date, end_date),
            'queries_pages': self.get_queries_pages(site_url, start_date, end_date),
            'dates': self.get_dates(site_url, start_date, end_date),
            'devices': self.get_devices(site_url, start_date, end_date),
            'sitemaps': self.get_sitemaps(site_url)
        }
        return data

if __name__ == '__main__':
    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN_HERE"
    SITE_URL = "sc-domain:your-domain.com"
    collector = GSCCollector(ACCESS_TOKEN)
    data = collector.collect_all(SITE_URL, days=90)
    with open('gsc_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Собрано: {len(data['queries'])} запросов, {len(data['pages'])} страниц")
```

---

## Итоговый чек-лист перед сдачей отчёта

- [ ] Все URL из sitemap проверены на HTTP-статус
- [ ] robots.txt проанализирован
- [ ] sitemap.xml проверен на ошибки
- [ ] Дубли найдены и описаны
- [ ] Title/Description проверены на всех страницах
- [ ] Canonical проверен (особенно на дублях)
- [ ] Schema.org оценён
- [ ] OG-теги проверены
- [ ] Внутренняя перелинковка оценена
- [ ] Данные GSC собраны (если доступны)
- [ ] Каннибализация выявлена (из GSC)
- [ ] План исправлений приоритизирован
- [ ] Чек-лист составлен
- [ ] Приложения заполнены
- [ ] Отчёт в Markdown формате

---

*Skill создан 13.05.2026 на основе аудита sequoia-service.ru*
*Версия: 1.0*