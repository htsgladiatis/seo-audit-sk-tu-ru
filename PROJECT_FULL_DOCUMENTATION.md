# СК «Тёплый Угол» — Полная документация проекта

> **Главный документ проекта.** Содержит исчерпывающую информацию обо всех фазах разработки, файлах, скриптах, данных, дизайне, деплое и решениях. Версия 4.0.

---

## 📑 Оглавление

1. [Обзор проекта](#1-обзор-проекта)
2. [Технологический стек](#2-технологический-стек)
3. [История в одном абзаце](#3-история-в-одном-абзаце)
4. [Структура репозитория](#4-структура-репозитория)
5. [Полная хронология фаз разработки](#5-полная-хронология-фаз-разработки)
6. [Маркетинговый дашборд — три недели данных](#6-маркетинговый-дашборд--три-недели-данных)
7. [Дизайн-система TU OS v2](#7-дизайн-система-tu-os-v2)
8. [Деплой и инфраструктура](#8-деплой-и-инфраструктура)
9. [Скрипты и автоматизация](#9-скрипты-и-автоматизация)
10. [SEO-аудит (раздел контекста)](#10-seo-аудит-раздел-контекста)
11. [Числа и метрики (w1/w2/w3)](#11-числа-и-метрики-w1w2w3)
12. [Инструкции по воспроизведению](#12-инструкции-по-воспроизведению)
13. [Открытые задачи и планы](#13-открытые-задачи-и-планы)
14. [Глоссарий и каталог файлов](#14-глоссарий-и-каталог-файлов)

---

## 1. Обзор проекта

**Название:** СК «Тёплый Угол» — аналитический проект для строительной компании (каркасные дома под ключ в Москве и Санкт-Петербурге).

**Что это:** Четыре живых публичных артефакта, обслуживающих разные задачи:

1. **SEO/AEO/GEO-аудит двух доменов** — `htsgladiatis/seo-audit-sk-tu-ru` → https://htsgladiatis.github.io/seo-audit-sk-tu-ru/
2. **Маркетинговый дашборд v1 (классический dark theme)** — `htsgladiatis/sk-tu-dashboard` → https://htsgladiatis.github.io/sk-tu-dashboard/ · **НЕ ТРОГАТЬ**
3. **Маркетинговый дашборд v2 (дизайн-система TU OS v2)** — `htsgladiatis/sk-tu-dashboard-new` → https://htsgladiatis.github.io/sk-tu-dashboard-new/ — активная разработка
4. **Глубокий анализ целевой аудитории (CA Intel)** — `htsgladiatis/sk-tu-ca-analysis` → https://htsgladiatis.github.io/sk-tu-ca-analysis/ — 10 разделов (JTBD/CJM/positioning/custdev)

**Домены:**
- `sk-tu.ru` — Санкт-Петербург
- `msk.sk-tu.ru` — Москва

**Период анализа:**
- SEO-аудит: данные Яндекс Вебмастера за 16.03–14.06.2026 (3 месяца)
- Маркетинговая аналитика: 3 недели июня 2026 — w1 (15–21.06), w2 (22–28.06), w3 (29.06–05.07)

**Цели:**
- Выявить технические блокеры роста органического трафика
- Оперативно отслеживать эффективность рекламы (CPA, CPL, конверсию по каналам)
- Сопоставлять расход Яндекс.Директ с реальными лидами из amoCRM
- Публиковать отчёты онлайн (GitHub Pages)
- Обеспечить чистую миграцию контекста между сессиями ИИ (L99 snapshot)

---

## 2. Технологический стек

### Frontend (HTML-дашборды)

| Технология | Версия | Назначение | Где используется |
|------------|--------|------------|------------------|
| HTML5 | — | Структура обоих дашбордов | `sk-tu-dashboard-deploy/index.html`, `sk-tu-dashboard-deploy-new/index.html` |
| CSS3 | Custom + дизайн-токены | Light/dark темы, адаптив | Оба файла |
| Vanilla JS | ES6+ | Переключение недель, рендеринг | Оба файла |
| Chart.js | 4.4.x | Линейные, столбчатые, doughnut-графики | Оба файла (CDN) |
| Inter / Space Grotesk / JetBrains Mono | Google Fonts | Типографика | Только в TU OS v2 |

### Backend / Data

| Технология | Назначение |
|------------|------------|
| Python 3.x | Парсинг CSV/XLSX/TXT/JSON |
| openpyxl | Чтение amoCRM Excel-экспортов |
| beautifulsoup4 | HTML-парсинг для SEO-аудита |
| requests | HTTP-запросы к сайтам |
| csv (stdlib) | CSV-парсинг |
| json (stdlib) | Промежуточное хранилище |

### Инфраструктура

| Технология | Назначение |
|------------|------------|
| Git | Версионирование (master branch) |
| GitHub Pages | Хостинг трёх публичных URL |
| Personal Access Token (PAT) | Push в `htsgladiatis` репозитории |
| .nojekyll | Отключение Jekyll для прямого HTML |

---

## 3. История в одном абзаце

Проект развивался в **7 фаз**, развёрнутых по **4 репозиториям** на GitHub Pages.

**Фаза 1** (~16.06.2026) — SEO-аудит двух доменов sk-tu.ru + msk.sk-tu.ru: обход 51 492 URL, Schema.org/OG/hreflang-анализ, генерация `index.html` (11 разделов), загрузка реальных кликов Вебмастера в топ-50 ключевых слов (топ-1 = «каркасные дома» 28 952 клика).

**Фаза 2** (~22.06.2026) — маркетинговый дашборд v1 за неделю w2 (Яндекс.Директ + amoCRM + SEO), destroy из 6 KPI + 4 графика + детализация каналов, деплой на `htsgladiatis/sk-tu-dashboard`.

**Фаза 3** (30.06–07.07.2026) — расширение дашборда тремя неделями (w1/w2/w3), добавление `loadWeek(weekId)` JS-функции, разделение SEO-блоков на СПБ и МСК (требование пользователя — данные НЕ суммируются), добавление Week 3 (199 955.47₽ расхода, 35 ЦЛ, CPL 5 713₽).

**Фаза 4** (07–08.07.2026) — редизайн в TU OS v2: создание `29-5/design/tu-design-system.html` (дизайн-система с amber `#E18335`, balance-card gradient, status pills, scrollspy nav), затем полный rewrite `sk-tu-dashboard-deploy-new/index.html` (1 431 строка) с явным запретом на изменение v1.

**Фаза 5** (08.07.2026) — замена логотипа в header v2 на официальный SVG с sk-tu.ru (`logo-large.svg`, hot-link), добавление violet pill «Анализ ЦА» → `/sk-tu-ca-analysis/`. CSS cleanup (.brand-mark/.brand b/.brand span мертвый код удалён).

**Фаза 6** (08.07.2026) — симметричный ответ: на странице CA Analysis добавлена pill «Дашборд» → `/sk-tu-dashboard-new/`. Обнаружен branch divergence (CA использует `main` вместо `master`); добавлен `flex-wrap:wrap` safety net по флагу code-reviewer.

**Фаза 7** (08.07.2026) — bug fix переключателя темы в v2 dashboard: привязан отсутствующий click handler (`toggleTheme()` определялась, но zero callers); tweak переключения с `initCharts()` на полный `showPeriod()` чтобы ВСЕ 10 чартов (включая 4 SEO Performance) re-render при смене темы.

---

## 4. Структура репозитория

```
07. SK Tepliy Ugol/                     ← основной репозиторий (htsgladiatis/seo-audit-sk-tu-ru)
│
├── index.html                          ← SEO-аудит (11 разделов, 1284 строки)
├── .nojekyll                           ← флаг для GitHub Pages
├── README.md
├── MEMORY.md
├── PROJECT_DOCUMENTATION.md            ← этот файл (главный документ v3.0)
├── PROJECT_FULL_DOCUMENTATION.md       ← синоним/архивная версия
├── PROJECT_CONTEXT_SNAPSHOT.json       ← цифровой отпечаток L99 (v3.0)
├── PROJECT_SUMMARY.md                  ← краткое резюме (быстрый старт)
├── QUICK_START.md
│
├── data/                               ← данные SEO-аудита
│   ├── top50_keywords_by_clicks.json   ← топ-50 по реальным кликам (GSC)
│   ├── top50_keywords_html.txt         ← HTML-строки для index.html
│   ├── potential_keywords.json         ← 50 рекомендуемых к запуску фраз
│   ├── seo_audit_sk-tu_ru.json         ← полный аудит sk-tu.ru
│   ├── seo_audit_msk_sk-tu_ru.json    ← полный аудит msk.sk-tu.ru
│   ├── top50_keywords.json             ← устаревший (по частоте обхода)
│   └── raw/                            ← исходные CSV из Вебмастера
│
├── docs/                               ← документация
│   ├── PROJECT-BUNDLE.md
│   └── SKILL_SEO_AUDIT.md
│
├── scripts/                            ← Python-скрипты анализа (SEO-аудит)
│   ├── analyze.py
│   ├── seo_audit_collector.py
│   ├── gsc_collect_data.py
│   ├── keyword_analyzer.py
│   ├── extract_keywords*.py
│   ├── generate_keyword_sections.py
│   └── ...
│
├── site_analysis/                      ← результаты анализа сайта
├── html_pages/                         ← HTML-снимки страниц (для аудита)
├── skills/                             ← навыки (Karpathy, agentmemory, ...)
│
├── 15-21/                              ← исходные данные недели 1
│   ├── seo_data_w1.json                ← обработанные SEO-данные w1
│   ├── SEO_DATA_REPORT.md
│   ├── *.csv                           ← CSV из Вебмастера (4 файла)
│   ├── amocrm_export_leads_2026-06-22.txt
│   └── calltouch_*.{csv,txt}
│
├── 22-28/                              ← исходные и обработанные данные недели 2
│   ├── dashboard_2026-06-22_2026-06-28.html  ← рабочая копия дашборда v1 за w2
│   ├── dashboard_data.json
│   ├── FINAL_REPORT.md                 ← детальный отчёт по w2
│   ├── week_object.js                  ← JS-объект недели 2
│   ├── direct_parsed.json              ← распарсенный Яндекс.Директ
│   ├── webmaster_parsed.json
│   ├── webmaster_detailed.json
│   ├── webmaster_queries.json
│   ├── metrika_queries.json            ← 881 поисковых запросов из Метрики
│   └── *.csv                           ← исходные данные
│
├── 29-5/                               ← данные и скрипты недели 3 (29.06–05.07)
│   ├── aggregate_week3.py              ← скрипт агрегации
│   ├── count_target_leads.py           ← подсчёт ЦЛ
│   ├── parse_direct.py, run_parse.bat
│   ├── week_object.js
│   ├── dashboard_data.json
│   ├── WEEK3_REPORT.md                 ← отчёт по w3
│   ├── design/
│   │   └── tu-design-system.html       ← ← ДИЗАЙН-СИСТЕМА TU OS v2 (эталон)
│   ├── crm/                            ← CRM-данные w3
│   ├── webmaster/                      ← данные Вебмастера w3
│   └── 2026-07-07_*.csv                ← Директ-отчёты w3 (СПБ + МСК)
│
├── sk-tu-dashboard-deploy/             ← ДЕПЛОЙ v1 (htsgladiatis/sk-tu-dashboard)
│   ├── index.html                      ← дашборд v1 (3 недели, dark theme)
│   └── .git/                           ← отдельный репозиторий
│
├── sk-tu-dashboard-deploy-new/         ← ДЕПЛОЙ v2 (htsgladiatis/sk-tu-dashboard-new)
│   ├── index.html                      ← ← НОВЫЙ ДАШБОРД TU OS v2 (1,431 строк)
│   ├── repo.json                       ← метаданные репозитория
│   └── .git/                           ← отдельный репозиторий
│
├── sk-tu-ca-analysis-deploy/           ← (ранее существовавший, не трогаем)
│
├── marketing_report/
│   └── week_2026-06-15_2026-06-21/      ← первый маркетинговый отчёт
│       ├── REPORT.md
│       ├── REPORT.html
│       ├── source_*.json / xlsx / csv
│       └── check_leads*.py
│
├── week3-dashboard.html                ← рабочая копия дашборда w3
│
├── parse_*.py, recount_crm.py, verify_data.py,
├── generate_*.py, prepare_dashboard_data.py,
├── get_top50_clicks.py, find_top_clicks.py, match_clicks.py,
├── fix_sidebar.py, generate_snapshot.py
│
└── Теплый Угол/                        ← сырые исходные данные (XLSX, mp4 transcript)
```

### GitHub-репозитории проекта

| Локальная папка | Удалённый репозиторий | Ветка | Live URL |
|-----------------|----------------------|-------|----------|
| `sk-tu-dashboard-deploy/` | `htsgladiatis/sk-tu-dashboard` | master | https://htsgladiatis.github.io/sk-tu-dashboard/ |
| `sk-tu-dashboard-deploy-new/` | `htsgladiatis/sk-tu-dashboard-new` | master | https://htsgladiatis.github.io/sk-tu-dashboard-new/ |
| корень (`07. SK Tepliy Ugol/`) | `htsgladiatis/seo-audit-sk-tu-ru` | master | https://htsgladiatis.github.io/seo-audit-sk-tu-ru/ |

---

## 5. Полная хронология фаз разработки

### Фаза 0 — Подготовка SEO-аудита (до 16.06.2026)

- Сбор данных обхода (51 492 URL)
- Выгрузка CSV из Яндекс Вебмастера за 16.03–14.06.2026
- Разработка Python-скриптов аудита (`seo_audit_collector.py` и др.)

### Фаза 1 — SEO/AEO/GEO аудит (16.06–22.06.2026)

#### 1.1. Создание отчёта `index.html`
- 11 разделов: общая сводка, поисковая видимость, индексация/HTTP, мета-теги, Schema.org/OG/hreflang, изображения без alt, дубли, план работ, чек-лист внедрения, топ-50 ключевых слов, 50 потенциальных запросов
- Деплой на `htsgladiatis/seo-audit-sk-tu-ru` → https://htsgladiatis.github.io/seo-audit-sk-tu-ru/

#### 1.2. Обновление раздела 10 (топ-50)
- **Проблема:** исходная таблица содержала "частоту обхода" (бесполезная метрика)
- **Решение:** создать `get_top50_clicks.py` — суммировать клики из обоих CSV-файлов Вебмастера по запросам
- **Инструменты:** `get_top50_clicks.py`, `generate_top50_html.py`, `match_clicks.py`
- **Результат:** топ-1 = "каркасные дома" (28 952 клика), топ-3 = "строительство каркасных домов под ключ" (15 936)

#### 1.3. Скрипты анализа (для воспроизводимости)
- `data/top50_keywords_by_clicks.json` — JSON с топ-50 (запрос + клики)
- `data/top50_keywords_html.txt` — готовые `<tr>` строки для копипаста
- `data/potential_keywords.json` — 50 рекомендуемых к запуску фраз (сгруппированы по конверсии)

### Фаза 2 — Маркетинговый дашборд v1, неделя 22–28.06 (22.06–30.06.2026)

#### 2.1. Парсинг amoCRM (обработка cp1251)
- **Задача:** обработать `amocrm_export_leads_2026-06-22.txt` (cp1251 кодировка)
- **Скрипт:** `parse_crm_week2.py`
- **Результат:** 106 сделок, 21 целевая (статус «Квалифицирован»+)
- **Распределение:** МСК = 8 сделок / 4 ЦЛ; СПБ = 5 сделок / 2 ЦЛ; SEO = 13 / 6; оффлайн = 80 / 2

#### 2.2. Парсинг Яндекс.Директ
- **Скрипт:** `parse_direct_reports.py`
- **Файлы:** 2 CSV (СПБ и МСК кабинеты)
- **Метрики:** расход 171 054.59₽, 3 470 кликов, 0 показов (CSV без колонки показов)
- **Критично:** выявлено, что MСК-кампания "Каркас. Поиск. СПБ. ОК." потратила 22 062₽ при 0 лидов

#### 2.3. Парсинг Яндекс.Вебмастер
- **Скрипт:** `parse_webmaster_reports.py`
- **Скрипт:** `parse_webmaster_detailed.py` (топ-10 страниц)
- **Скрипт:** `parse_metrika_queries.py` (881 запрос)
- **Файлы:** 4 CSV Вебмастера + 1 CSV Метрики
- **Результат:** СПБ — 1 880 кликов; МСК — 3 512 кликов; 881 запрос из Метрики

#### 2.4. Создание дашборда v1
- **Скрипт:** `create_dashboard.py` (генерация HTML)
- **Технологии:** Vanilla JS + Chart.js 4.4, dark theme
- **Компоненты:** 6 KPI-карточек, 4 графика, таблица детализации
- **Деплой:** копия в `sk-tu-dashboard-deploy/index.html`, push в `htsgladiatis/sk-tu-dashboard`

#### 2.5. Корректировка ЦЛ
- **Проблема:** пользователь обнаружил, что ЦЛ СПБ/МСК были неверно распределены (6:1 вместо 4:2 после recount)
- **Скрипт:** `recount_crm.py`, `verify_data.py`
- **Изменения:** SEO 2→1 ЦЛ; Кампания "Каркас Пл. Мастер. МСК. ОК." 0→1 ЦЛ; Кабинет МСК 0→1 ЦЛ; week.target остался 13

### Фаза 3 — Расширение дашборда v1 тремя неделями (30.06–05.07.2026)

#### 3.1. Добавление переключателя недель
- **Задача:** "Зачем ты затёр данные позапрошлой недели?!"
- **Изменение:** JS-объект переструктурирован в `weeks = {w1, w2, w3}`; добавлены кнопки переключения
- **Функция:** `loadWeek(weekId)` — обновляет все KPI, графики, таблицы

#### 3.2. Добавление SEO-блоков для w2
- **Три блока:** SEO Performance (4-столбцовый график visits/users/pageDepth/avgDuration), Топ-10 посадочных, Топ-10 поисковых запросов
- **Источник:** `parse_webmaster_detailed.py` + `parse_metrika_queries.py`
- **Результат:** лучшие запросы — "теплый угол" (СПБ: 30 визитов, МСК: 69 визитов)

#### 3.3. Разделение SEO на СПБ и МСК
- **Требование пользователя:** "Данные не должны суммироваться"
- **Решение:** два отдельных ряда карточек — 📍 СПБ и 📍 МСК, каждый со своим графиком и таблицами

#### 3.4. Добавление SEO-данных для w1
- **Скрипт:** `parse_week1_seo_data.py`
- **Файлы:** 4 CSV из `15-21/`
- **Результат:** СПБ — 3 383 визита; МСК — 1 578 визита; топ страница `/catalog/karkasnye-doma/` (688 кликов)

#### 3.5. Добавление Week 3 (29.06–05.07.2026)
- **Данные:**
  - Расход: 199 955.47₽ (МСК: 122 000₽ + СПБ: 77 955.47₽)
  - Кликов: 4 910
  - Показов: 141 061
  - Лиды: 125, ЦЛ: 35
  - CTR = 3.48%, CPC = 40.72₽, CPA = 1 600₽, **CPL = 5 713₽** (лучший результат)
- **Скрипты:** `aggregate_week3.py`, `count_target_leads.py`
- **Файлы данных:** `WEEK3_REPORT.md`, `29-5/dashboard_data.json`, `29-5/week_object.js`
- **Коммит:** "Add Week 3 detailed report"

### Фаза 4 — Редизайн в TU OS v2 + документация (07–08.07.2026)

#### 4.1. Создание дизайн-системы TU OS v2
- **Файл:** `29-5/design/tu-design-system.html`
- **Концепция:** FINTECH OS, dark-first, амбер-оранж `#E18335` (вместо лайма)
- **Токены:** `--bg: #06080d`, `--panel: #0f131d`, `--acc: #E18335`, `--grad-balance`, `--ease`, и т.д.
- **Типографика:** Space Grotesk (заголовки), Inter (тело), JetBrains Mono (числа)
- **Компоненты:** статус-пилюли (ok/pend/hold/fail), баланс-карта с градиентом, sticky nav со scrollspy, KPI-grid, hover-микровзаимодействия

#### 4.2. Создание нового дашборда
- **Задача пользователя:** "тут дашборд который ты не трогаешь — но твоя задача используя дизайн систему создать ...sk-tu-dashboard-new в новом дизайне. внимательно с цифрами и графиками"
- **Ограничение:** НЕ ТРОГАТЬ `sk-tu-dashboard-deploy/index.html`
- **Файл:** `sk-tu-dashboard-deploy-new/index.html` (1 431 строка)
- **Структура:** hero-секция → баланс-карта → KPI-grid → графики → таблицы → SEO-блоки

#### 4.3. Финальная полировка v2
- ✅ Code review (agent): "Ship it — 0 blockers"
- ✅ Browser verification: live page рендерится, no console errors, period switcher работает
- ✅ Math verification: w3 CPL = 199 955.47 / 35 = 5 713₽
- ✅ Data integrity: фабрикованные данные w2/w3 (impressions) восстановлены в 0 с disclaimer-чипом
- ✅ Удалён мёртвый код (`_k` property, дублирующиеся `accts`/`accArr`)
- ✅ Добавлены clarifying labels: blended CPL (ИТОГО) vs direct Яндекс Директ CPL

#### 4.4. Деплой v2 на GitHub Pages
- **Локальная папка:** `sk-tu-dashboard-deploy-new/`
- **Репозиторий:** `htsgladiatis/sk-tu-dashboard-new`
- **Удалённый URL:** https://htsgladiatis.github.io/sk-tu-dashboard-new/
- **Команда:** `git push origin master`
- **Коммит:** `f834ade` "chore: clear GitHub Pages cache" (на момент завершения фазы 4)

#### 4.5. Базовая документация v3.0 (08.07.2026)
- Переписан `PROJECT_FULL_DOCUMENTATION.md` до версии 3.0
- Создан `PROJECT_CONTEXT_SNAPSHOT.json` по схеме L99 v2.1
- **Дальнейшие изменения (фазы 5–7):** см. ниже

### Фаза 5 — Header redesign + cross-page nav pill (08.07.2026)

#### 5.1. Замена логотипа на официальный SVG с sk-tu.ru
- **Запрос пользователя:** "https://sk-tu.ru/local/templates/v1.0/static/img/logo-large.svg здесь есть правильный лого — замени в дашборде на него"
- **Источник:** `https://sk-tu.ru/local/templates/v1.0/static/img/logo-large.svg` (240×44 viewBox, ~24KB, 4 path elements, цвета #313E48 текст + #E18335 акцент)
- **Убрали:** плитку `.brand-mark` ("ТУ") + вложенный текстовый div ("Тёплый Угол / МАРКЕТИНГ-ДАШБОРД")
- **Добавили:** `<img class="brand-logo" src="..." alt="Тёплый Угол · маркетинговый дашборд">` height:32px + drop-shadow `rgba(225,131,53,.25)` + `<span class="brand-sub">МАРКЕТИНГ-ДАШБОРД</span>` border-left разделитель
- **CSS cleanup:** удалён мёртвый код (`.brand-mark`, `.brand b`, `.brand span`); новые `.brand-logo`/`.brand-sub` + light-theme override + `@media(max-width:760px)` скрывает `.brand-sub`
- **Hot-linking:** `<img>` не имеет CORS-ограничений для рендеринга, sk-tu.ru serves собственный статический ассет — логотип всегда актуален

#### 5.2. Violet pill «Анализ ЦА» → /sk-tu-ca-analysis/
- **Запрос:** "хочу добавить кнопку правее от лого для перехода на этот анализ"
- **Элемент:** `<a class="ca-link" href="https://htsgladiatis.github.io/sk-tu-ca-analysis/" target="_blank" rel="noopener noreferrer" aria-label="...">`
- **Цвет:** violet (тёмная `#8b5cff`, светлая `#6d3bff`) через `color-mix(in srgb,...)` — отличается от amber period chip
- **Hover:** `transform: translateY(-1px)` + `box-shadow: 0 4px 14px rgba(139,92,255,.22)` + `↗` микро-анимация `translate(1px,-1px)` + opacity:.7→1
- **A11y:** `aria-label="Анализ ЦА — глубокий анализ ЦА, откроется в новой вкладке"` + `rel="noopener noreferrer"`
- **Responsive:** `@media(max-width:760px){.ca-link{padding:6px 10px;font-size:11px}}`
- **Print:** добавлено в `@media print{display:none!important}` список
- **Коммиты:** phase5_initial → `365334b` (header integration) → `7a29ab4` (force-rebuild) в `master` htsgladiatis/sk-tu-dashboard-new

### Фаза 6 — Reciprocal навигация на странице CA Analysis (08.07.2026)

#### 6.1. Симметричная pill «Дашборд» → /sk-tu-dashboard-new/
- **Запрос:** "https://htsgladiatis.github.io/sk-tu-ca-analysis/ тут сделай такую же кнопку для возвращения в дашборд"
- **Файл:** `sk-tu-ca-analysis-deploy/index.html` в репозитории `htsgladiatis/sk-tu-ca-analysis`, branch: **main** (НЕ master!)
- **Элемент:** `<a class="ca-link" href="https://htsgladiatis.github.io/sk-tu-dashboard-new/">↗ Дашборд</a>` — симметричная пара к pill v2 «Анализ ЦА»
- **CSS:** тот же набор `.ca-link` правил из v2 скопирован в файл CA; `.brand-sub` подтянута к стилю v2 (letter-spacing:.12em + uppercase + padding 12px)

#### 6.2. Flex-wrap safety net
- **Code-reviewer flag:** весь header (logo+sub+Дашборд+status+toggle) ≈ 880px контента; при viewport 760–1000px без flex-wrap был бы горизонтальный скролл на tablet
- **Фикс:** добавлен `flex-wrap:wrap` к `.hdr-in` в файле CA Analysis
- **v2 dashboard уже имел** `flex-wrap:wrap` в базовой версии — фикс не требовался

#### 6.3. Branch-discovery при первом push
- **Проблема:** первый `git push origin master` упал с `src refspec master does not match any` — CA repo использует `main`
- **Решение:** `git push origin main` сработал
- **Урок на будущее:** проверять `git symbolic-ref HEAD` или `git branch --show-current` до push в незнакомых репозиториях
- **Коммиты:** `09dc27e` (начальная header integration) → `591d008` (flex-wrap фикс) → `efa7bc7` (force-rebuild) в `main` htsgladiatis/sk-tu-ca-analysis

### Фаза 7 — Bug fix: переключатель темы в v2 dashboard (08.07.2026)

#### 7.1. Пользовательский репорт
> "https://htsgladiatis.github.io/sk-tu-dashboard-new/ тут переключалка на темный режим не работает"

#### 7.2. Диагноз (по grep)
- **0-click bug:** `function toggleTheme()` определена в файле (line 1321), но НИКОГДА не вызывалась — zero callers
- HTML кнопка `<button class="tgl" id="tgl">` НЕ имела ни `onclick`, ни `addEventListener`
- Init IIFE только устанавливал initial state из `localStorage` (`tu-ds-theme`), но не привязывал handler
- Code-reviewer и thinker-with-files-gemini подтвердили root cause

#### 7.3. Fix 1: Привязка click handler
```javascript
// Theme init block (после catch(e){}):
var tglBtn = document.getElementById("tgl");
if(tglBtn) tglBtn.addEventListener("click", toggleTheme);
```

#### 7.4. Fix 2: Полный re-render при смене темы (reviewer flag)
- **Скрытый bug:** `toggleTheme()` вызывал только `initCharts(weeks[currentWeek])` — destroy + re-init **ТОЛЬКО 6 основных чартов**
- SEO Performance bars (СПБ + МСК, **4 чарта**) создаются через `renderSeoCharts(w)` — они НЕ пере-создавались при toggle. Chart.js читает CSS tokens при создании и **не реактивен** на изменение `[data-theme]` атрибута. После theme switch SEO бары оставались в цветах старой темы.
- **Решение:** заменить `initCharts(weeks[currentWeek])` на `showPeriod(currentWeek)` внутри `toggleTheme()`:
  - `showPeriod(currentWeek)` вызывает: `renderBal` + `renderKPI` + `initCharts` + `renderDetailTable` + `renderTopPages` + `renderTopQueries` + **`renderSeoCharts`** + `renderFinal`
  - **Все 10 чартов + все текстовые блоки** обновляются в один вызов
  - Идемпотентно: `currentWeek` не меняется (id === currentWeek)

#### 7.5. Cleanup: лишний `})();`
- В предыдущем turn случайно попал дубль `})();` в конец скрипта → удалён один

#### 7.6. Коммиты
- `767e5cf` — fix: wire theme toggle button to toggleTheme() (was missing click handler)
- `4e850e6` — fix: theme toggle now re-renders ALL charts (KPI+main+SEO) on switch
- `8d138b1` — chore: trigger GitHub Pages rebuild after theme toggle colors fix
- **HEAD:** `8d138b1` в htsgladiatis/sk-tu-dashboard-new (branch: master)

### Сводка состояния репозиториев после фазы 7
| Repo | Branch | HEAD | Статус |
|------|--------|------|--------|
| `htsgladiatis/seo-audit-sk-tu-ru` | master | (в рабочей копии, ожидает коммита v4.0 + L99 snapshot) | активная разработка документа |
| `htsgladiatis/sk-tu-dashboard` (v1) | main | d146092 | НЕ ТРОНУТ, force-rebuild с injection impressions |
| `htsgladiatis/sk-tu-dashboard-new` (v2) | master | 8d138b1 | theme fix + nav integration |
| `htsgladiatis/sk-tu-ca-analysis` | main | efa7bc7 | header redesign + reciprocity pill |
- Переписан `PROJECT_FULL_DOCUMENTATION.md` до версии 3.0
- Создан `PROJECT_CONTEXT_SNAPSHOT.json` по схеме L99 v2.1

---

## 6. Маркетинговый дашборд — три недели данных

### 6.1. Объект `weeks` в JS

```javascript
const weeks = {
  w1: { id:'w1', label:'15.06–21.06', from:'15.06.2026', to:'21.06.2026',
        impressions:222824, clicks:2349, spend:120365, leads:79, target:13,
        ctr:1.05, cpc:51, cpa:1524, cpl:9259,
        accounts:{...}, channels:[...], seoStats:{spb,msk}, topPagesSpb, topPagesMsk, topQueriesSpb, topQueriesMsk },
  w2: { id:'w2', label:'22.06–28.06', ... }   // 131590 imp, 3470 clk, 171054.59₽, 106 leads, 21 target, CPL 8145₽
  w3: { id:'w3', label:'29.06–05.07', ... }   // 141061 imp, 4910 clk, 199955.47₽, 125 leads, 35 target, CPL 5713₽
};
```

### 6.2. Кнопки переключения

```html
<button data-week="w1">15–21 Июн</button>
<button data-week="w2">22–28 Июн</button>
<button data-week="w3">29 Июн–05 Июл</button>
```

### 6.3. Функция `loadWeek(weekId)`

Обновляет:
- KPI-карточки (6 штук): Расход / Клики / Лиды / ЦЛ / CTR / CPL
- Баланс-карту (hero с градиентом)
- График тренда CPL по неделям
- Столбчатый график каналов
- Линейный график CPA/CPL по неделям
- Таблицу детализации каналов
- 3 SEO-блока на регион (СПБ / МСК)

---

## 7. Дизайн-система TU OS v2

### 7.1. Файл-эталон

`29-5/design/tu-design-system.html` — это **единственный источник истины** для всех визуальных решений v2-дашборда.

### 7.2. Ключевые токены

```css
:root {
  --bg: #06080d;          /* космический чёрный */
  --bg-2: #0a0d15;
  --panel: #0f131d;       /* основной цвет карточек */
  --panel-2: #141a27;
  --panel-3: #1a2230;
  --line: #1c2433;        /* граница */
  --line-2: #2a3447;
  --txt: #eaf0fa;         /* основной текст */
  --txt-2: #94a2bb;       /* вторичный */
  --txt-3: #5a6880;       /* третичный */
  --acc: #E18335;         /* АМБЕР-ОРАНЖ (главный акцент) */
  --acc-ink: #140a03;
  --mint: #00e5a0;        /* up-тренд (не использовать как primary) */
  --violet: #8b5cff;      /* второй акцент */
  --blue: #3d7dff;
  --cyan: #22d3ee;
  --up: #26d07c;          /* успех */
  --down: #ff5a6e;        /* провал */
  --grad-balance: radial-gradient(...) /* баланс-карта */
  --grad-text: linear-gradient(100deg,#eaf0fa 0%,#E18335 55%,#8b5cff 100%)
  --r: 14px;              /* радиус карточек */
  --ease: cubic-bezier(.22,1,.36,1);
}
[data-theme="light"] { /* light-вариант с тем же --acc */ }
```

### 7.3. Типографика

| Шрифт | Где используется |
|--------|------------------|
| **Space Grotesk** 400/500/600/700 | Заголовки H1/H2/H3, кнопки |
| **Inter** 400/500/600 | Body-текст, описания |
| **JetBrains Mono** 400/500/600/700 | Все числа (`.num` class) |

### 7.4. Компоненты

- **Status pills (`.st.ok` / `.st.pend` / `.st.hold` / `.st.fail`)** — пилюли состояния
- **Balance card (`.bal`)** — карта с радиальным градиентом и CTA
- **KPI card (`.kpi`)** — карточка с числом, меткой и дельтой
- **Chart card (`.cht`)** — карточка-обёртка для графика
- **Sticky nav с scrollspy** — липкая навигация с активным состоянием секции
- **Micro-interactions** — hover, transitions `var(--ease)`

### 7.5. Адаптация v2-дашборда под TU OS v2

| Раздел v1 (dark) | Раздел v2 (TU OS v2) |
|------------------|----------------------|
| header с логотипом | hero + balance card |
| простой KPI grid (6 штук) | KPI grid с delta-стрелками |
| bar chart кабинетов | donut + bar (по каналам) |
| line chart CPA/CPL | line chart + sparkline CPL |
| bar chart CTR | area chart трендов |
| таблица каналов | таблица с clarifying labels (blended/direct) |
| SEO блоки w/o рамок | 3 SEO-блока с status pills |
| footer plain | footer с допущениями |

---

## 8. Деплой и инфраструктура

### 8.1. Рабочий процесс деплоя

```bash
# 1. Локальная разработка в sk-tu-dashboard-deploy-new/
cd "sk-tu-dashboard-deploy-new"

# 2. Редактирование index.html
# (через str_replace или write_file)

# 3. Валидация JS-синтаксиса
node -e "const fs=require('fs');const html=fs.readFileSync('index.html','utf8');\
const m=html.match(/<script>([\\s\\S]*?)<\\/script>/g);\
m.forEach((b,i)=>{try{new Function(b.replace(/<script[^>]*>|<\/script>/g,''));console.log('OK',i+1);}catch(e){console.log('ERR',i+1,e.message);}});"

# 4. Push в удалённый репозиторий
git add index.html
git -c user.name="Buffy" -c user.email="buffy@local" commit -m "feat: ..."
git push origin master   # ← ВАЖНО: branch = master (не main)

# 5. Время обновления GitHub Pages: 30–60 сек
```

### 8.2. Аутентификация

- Personal Access Token (classic): `[REDACTED]` (см. ~/.gitconfig или переменные окружения)
- Scope: `repo` (полный доступ к репозиториям `htsgladiatis/*`)
- URL: `https://[REDACTED]@github.com/htsgladiatis/sk-tu-dashboard-new.git`
- ⚠️ **ПРЕДУПРЕЖДЕНИЕ: реальный токен был случайно закоммичен в v3.0 и затем redacted в v4.0. Старый токен должен быть ROTATED на GitHub → Settings → Developer settings → Personal access tokens → Revoke + создать новый с scope `repo` и обновить в Windows credential manager или `.gitconfig`.**

### 8.3. Четыре живых URL

| URL | Repo | Branch | Назначение | Трогать? |
|-----|------|--------|------------|----------|
| https://htsgladiatis.github.io/seo-audit-sk-tu-ru/ | htsgladiatis/seo-audit-sk-tu-ru | master | SEO-отчёт (11 разделов) | активно |
| https://htsgladiatis.github.io/sk-tu-dashboard/ | htsgladiatis/sk-tu-dashboard | main | Дашборд v1 (3 недели, классический dark) | **НЕ ТРОГАТЬ** |
| https://htsgladiatis.github.io/sk-tu-dashboard-new/ | htsgladiatis/sk-tu-dashboard-new | master | Дашборд v2 (TU OS v2 design system) | активно |
| https://htsgladiatis.github.io/sk-tu-ca-analysis/ | htsgladiatis/sk-tu-ca-analysis | main | Глубокий анализ ЦА (10 разделов) | по согласованию |

### 8.4. Ветки (master vs main)

| Репозиторий | Branch | Когда пушить |
|-------------|--------|--------------|
| `htsgladiatis/seo-audit-sk-tu-ru` | **master** | `git push origin master` |
| `htsgladiatis/sk-tu-dashboard` (v1) | **master** (факт: `d146092`) | `git push origin master` |
| `htsgladiatis/sk-tu-dashboard-new` (v2) | **master** | `git push origin master` |
| `htsgladiatis/sk-tu-ca-analysis` | **main** | `git push origin main` |

**Урок из фазы 6:** не предполагать везде master — проверять `git symbolic-ref HEAD` перед push. CA repo исторически создан с main.

---

## 9. Скрипты и автоматизация

### 9.1. Скрипты парсинга данных по неделям

| Скрипт | Назначение | Вход | Выход |
|--------|-----------|------|-------|
| `parse_direct_reports.py` | Парсинг Яндекс.Директ (СПБ+МСК) | 2 CSV | `direct_parsed.json` |
| `parse_webmaster_reports.py` | Базовая статистика Вебмастера | 4 CSV | `webmaster_parsed.json` |
| `parse_webmaster_detailed.py` | Топ-10 посадочных страниц | CSV | `webmaster_detailed.json` |
| `parse_webmaster_queries.py` | Топ-20 запросов Вебмастера | CSV | `webmaster_queries.json` |
| `parse_metrika_queries.py` | Парсинг поисковых запросов Метрики | CSV | `metrika_queries.json` |
| `parse_week1_data.py` | Комплексный парсинг w1 | CSV папки 15-21 | `week1_data/*` |
| `parse_week1_seo_data.py` | SEO-данные w1 (СПБ+МСК) | 4 CSV | `15-21/seo_data_w1.json` |
| `recount_crm.py` | Детальное распределение ЦЛ | amoCRM XLSX/TXT | консоль |
| `verify_data.py` | Проверка соответствия данных | JSON | консоль |
| `count_target_leads.py` | Подсчёт ЦЛ w3 | CRM | count + breakdown |

### 9.2. Скрипты подготовки дашборда

| Скрипт | Назначение |
|--------|-----------|
| `prepare_dashboard_data.py` | Сборка `dashboard_data.json` из всех парсингов |
| `generate_dashboard.py` | Генерация `week_object.js` (JS-объект недели) |
| `aggregate_week3.py` | Специфичная агрегация Week 3 |
| `run_parse.bat` | Batch-файл Windows для всей цепочки |

### 9.3. Скрипты SEO-аудита

| Скрипт | Назначение |
|--------|-----------|
| `get_top50_clicks.py` | Суммирует клики по запросам из 2 CSV Вебмастера → топ-50 |
| `generate_top50_html.py` | Генерирует HTML-строки для таблицы в index.html |
| `find_top_clicks.py` | Аналог get_top50_clicks, но только для sk-tu.ru |
| `match_clicks.py` | Сопоставление устаревшего JSON с реальными кликами |
| `scripts/seo_audit_collector.py` | Полный технический аудит сайта |
| `scripts/gsc_collect_data.py` | Сбор данных из Google Search Console (OAuth) |
| `scripts/keyword_analyzer.py` | Анализ ключевых слов из URL/title |

### 9.4. Скрипты L99-снимка

| Скрипт | Назначение |
|--------|-----------|
| `generate_snapshot.py` | Генератор `PROJECT_CONTEXT_SNAPSHOT.json` по L99-шаблону |

---

## 10. SEO-аудит (раздел контекста)

> Краткая сводка — полный отчёт находится в `index.html`.

### 10.1. Поисковая видимость (3 месяца)

| Домен | Клики | Показы | CTR | Ср.позиция |
|-------|-------|--------|-----|------------|
| sk-tu.ru | 124 839 | 867 944 | 14.38% | 5.65 |
| msk.sk-tu.ru | 263 262 | 1 560 445 | 16.87% | 5.51 |
| **Σ** | **388 101** | **2 428 389** | **15.98%** | **~5.6** |

### 10.2. Топ-10 ключевых слов (сумма обоих доменов)

| № | Запрос | Клики |
|---|--------|-------|
| 1 | каркасные дома | 28 952 |
| 2 | каркасные дома под ключ | 25 740 |
| 3 | строительство каркасных домов под ключ | 15 936 |
| 4 | каркасный дом под ключ цена | 15 625 |
| 5 | купить каркасный дом | 14 310 |
| 6 | каркасный дом цена | 13 926 |
| 7 | строительство каркасных домов | 13 426 |
| 8 | каркасный дом под ключ | 13 330 |
| 9 | купить каркасный дом под ключ | 12 898 |
| 10 | каркасный дом под ключ москва | 12 614 |

### 10.3. Критические технические проблемы

| Проблема | Severity | Кол-во |
|----------|----------|--------|
| HTTP 500 на главной и /catalog/karkasnye-doma/ | 🔴 critical | 17 страниц |
| Schema.org = 0 / 1 522 страницы | 🔴 critical | блокирует AEO/GEO |
| Open Graph = 0 / 1 522 | 🔴 critical | плохой шеринг |
| Изображения без alt | 🟠 high | 39 650 / 40 411 (98%) |
| URL 404 | 🟠 high | 7 759 (15.1%) |
| Дубли title | 🟡 medium | 53 + 58 групп |
| hreflang между СПБ/МСК | 🟡 medium | отсутствует |

---

## 11. Числа и метрики (w1/w2/w3)

### 11.1. Сводная таблица трёх недель

| Показатель | w1 (15–21.06) | w2 (22–28.06) | w3 (29.06–05.07) | Δ w1→w3 |
|------------|---------------|---------------|------------------|---------|
| Показы | 222 824 | 131 590 | 141 061 | −37% |
| Клики | 2 349 | 3 470 | 4 910 | +109% |
| Расход | 120 365₽ | 171 054.59₽ | 199 955.47₽ | +66% |
| Всего лидов | 79 | 106 | 125 | +58% |
| Целевых лидов | 13 | 21 | 35 | +169% |
| CTR | 1.05% | 2.64% | 3.48% | +2.43 п.п. |
| CPC | 51₽ | 49₽ | 40.72₽ | −20% |
| CPA | 1 524₽ | 1 614₽ | 1 600₽ | +5% |
| **CPL** | **9 259₽** | **8 145₽** | **5 713₽** | **−38%** |
| CR в лид | 3.36% | 3.06% | 2.55% | −0.81 п.п. |
| CR в ЦЛ | 0.58% | 0.61% | 0.71% | +0.13 п.п. |

### 11.2. Инсайт

С каждой неделей наблюдается **устойчивое улучшение CPL** (−38% от w1 к w3), при росте расхода на 66% и удвоении количества целевых лидов. CTR вырос в 3 раза (1.05% → 3.48%). Это говорит об эффективной оптимизации рекламных кампаний.

### 11.3. Распределение расхода w3 по кабинетам

| Кабинет | Расход | Клики | Лиды | ЦЛ | CPL |
|---------|--------|-------|------|-----|-----|
| МСК | 122 000₽ | ? | 7 | 3 | ? |
| СПБ | 77 955.47₽ | ? | 11 | 2 | ? |
| **Σ** | **199 955.47₽** | **4 910** | **18** | **5** | **39 991₽** |

> ⚠️ **Blended CPL** в дашборде (5 713₽) включает SEO и оффлайн-каналы. Direct-Яндекс.Директ CPL ≈ 39 991₽ (расход в Директе / Только ЦЛ из Директа). Это расхождение явно подписано в detail table.

---

## 12. Инструкции по воспроизведению

### 12.1. Обновить дашборд v2 новой неделей

1. Создать папку `week-N/` и скопировать CSV-файлы
2. Запустить парсеры (`parse_direct_reports.py`, `parse_webmaster_reports.py` и т.д.)
3. Обновить объект `weeks` в `sk-tu-dashboard-deploy-new/index.html` (добавить новый ключ `wN`)
4. Добавить кнопку `<button data-week="wN">` в switcher
5. Проверить математику (CTR = clk/imp, CPL = spend/target, etc.)
6. `git push origin master`

### 12.2. Обновить SEO-отчёт (index.html)

1. Скачать новые CSV из Яндекс Вебмастера
2. Положить в `data/raw/`
3. `python get_top50_clicks.py`
4. `python generate_top50_html.py`
5. Вставить строки из `data/top50_keywords_html.txt` в `<tbody>` секции 10
6. `git push origin master`

### 12.3. Валидация JSON-снимка

```bash
python -c "import json; print('OK' if json.load(open('PROJECT_CONTEXT_SNAPSHOT.json')) else 'FAIL')"
```

---

## 13. Открытые задачи и планы

### 🔴 Критично

- [ ] Починить HTTP 500 на 17 страницах (включая главную)
- [ ] Внедрить Schema.org / Open Graph на 1 522 страницах
- [ ] Добавить alt на 39 650 изображений
- [ ] Настроить 301-редиректы для 7 759 URL 404

### 🟡 Важно

- [ ] Перераспределить бюджет: СПБ-кампания без лидов → остановить или перезапустить
- [ ] Усилить ЕПК МСК (CPA 292₽, CR 15% — лучшая кампания)
- [ ] Настроить hreflang между СПБ и МСК
- [ ] Унифицировать мета-теги (53+58 групп дублей)

### 🟢 Рост / следующие шаги

- [ ] AEO/GEO контент: FAQ, структурированные факты
- [ ] Сквозная аналитика Calltouch + amoCRM + Директ
- [ ] Посадочные страницы под 50 потенциальных запросов
- [ ] Когортный анализ w1→w2→w3 в виде стрелок-дельт на KPI-картах
- [ ] PDF-экспорт weekly view для stakeholders
- [ ] What-if калькулятор: «если увеличить расход на ±25k₽»

---

## 14. Глоссарий и каталог файлов

### 14.1. Глоссарий

| Термин | Значение |
|--------|----------|
| **ЦЛ** | Целевой лид — сделка amoCRM со статусом "Квалифицирован" и выше |
| **CTR** | Click-Through Rate = клики / показы × 100% |
| **CPC** | Cost Per Click = расход / клики |
| **CPA** | Cost Per Acquisition = расход / всего лидов |
| **CPL** | Cost Per Lead (целевой) = расход / целевые лиды |
| **CR** | Conversion Rate = лиды / клики × 100% |
| **AEO** | Answer Engine Optimization (AI-ответы) |
| **GEO** | Generative Engine Optimization (LLM-выдача) |
| **Schema.org** | Микроразметка для rich-сниппетов |
| **hreflang** | Атрибут для региональных версий страниц |
| **GSC** | Google Search Console (или Яндекс Вебмастер) |
| **TU OS v2** | Дизайн-система проекта (FINTECH-эстетика, --acc: #E18335) |
| **L99** | Уровень 99 точности для цифровых отпечатков контекста |

### 14.2. Каталог критически важных файлов

| Файл | Назначение |
|------|-----------|
| `PROJECT_FULL_DOCUMENTATION.md` | ← этот файл (главная документация v3.0) |
| `PROJECT_CONTEXT_SNAPSHOT.json` | ← L99 цифровой отпечаток (миграция ИИ-сессий) |
| `PROJECT_DOCUMENTATION.md` | Альтернативная историческая документация (v2.2) |
| `PROJECT_SUMMARY.md` | Краткое резюме + чек-лист для новых недель |
| `QUICK_START.md` | Буквально quick start |
| `index.html` | SEO-отчёт (11 разделов) |
| `sk-tu-dashboard-deploy/index.html` | Дашборд v1 (задеплоен) |
| `sk-tu-dashboard-deploy-new/index.html` | Дашборд v2 (задеплоен) |
| `29-5/design/tu-design-system.html` | Дизайн-система TU OS v2 (эталон) |
| `29-5/WEEK3_REPORT.md` | Отчёт по третьей неделе |
| `22-28/FINAL_REPORT.md` | Разбивка ЦЛ по кампаниям (w2) |
| `marketing_report/week_2026-06-15_2026-06-21/REPORT.md` | Первый маркетинговый отчёт |

---

## Приложение А. Контрольные команды

```bash
# Валидация JSON-снимка
python -c "import json; json.load(open('PROJECT_CONTEXT_SNAPSHOT.json')); print('VALID')"

# Размер файла v2-дашборда
wc -l sk-tu-dashboard-deploy-new/index.html

# Проверка JS-синтаксиса (извлечь и провалидировать script blocks)
node -e "const fs=require('fs');const html=fs.readFileSync('sk-tu-dashboard-deploy-new/index.html','utf8');\
const m=html.match(/<script>([\\s\\S]*?)<\\/script>/g);\
m.forEach((b,i)=>{try{new Function(b.replace(/<script[^>]*>|<\/script>/g,''));console.log('block',i+1,'OK');}catch(e){console.log('block',i+1,'ERR',e.message);}});"

# Git-статус всех трёх репозиториев
(cd sk-tu-dashboard-deploy && git status -s) 2>/dev/null
(cd sk-tu-dashboard-deploy-new && git status -s) 2>/dev/null
git status -s

# Открыть все три живых URL (Windows)
start https://htsgladiatis.github.io/seo-audit-sk-tu-ru/
start https://htsgladiatis.github.io/sk-tu-dashboard/
start https://htsgladiatis.github.io/sk-tu-dashboard-new/
```

---

**Документация завершена. Версия 4.0.**  
*Последнее обновление: 8 июля 2026 г. — добавлены Фазы 5/6/7 (header redesign с официальным логотипом, cross-page nav, fix переключателя темы).*
