# SK Tepliy Ugol - SEO/AEO/GEO Audit Project

## Структура проекта

```
07. SK Tepliy Ugol/
├── README.md                    # Документация проекта
├── data/                        # Данные и конфигурация
│   ├── raw/                     # Исходные данные (CSV/GZ файлы)
│   │   ├── msk.sk-tu.ru_*.csv   # Данные с msk.sk-tu.ru
│   │   ├── msk.sk-tu.ru_*.gz    # Сжатые данные msk
│   │   ├── sk-tu.ru_*.csv       # Данные с sk-tu.ru
│   │   └── sk-tu.ru_*.gz        # Сжатые данные sk-tu.ru
│   ├── state_store.db/          # База данных agentmemory
│   ├── stream_store/            # Хранилище потоков
│   ├── skills-lock.json         # Конфигурация навыков
│   ├── seo_audit_sk-tu_ru.json      # Аудит sk-tu.ru (761 стр.)
│   └── seo_audit_msk_sk-tu_ru.json  # Аудит msk.sk-tu.ru (761 стр.)
├── docs/                        # Документация и отчёты
│   ├── PROJECT-BUNDLE.md        # Общий бандл проекта
│   └── SKILL_SEO_AUDIT.md       # Алгоритм SEO-аудита (skill)
├── html_pages/                  # Сохранённые HTML-страницы
│   ├── about_page.html          # О компании
│   ├── catalog_page.html        # Каталог
│   ├── contacts_page.html       # Контакты
│   ├── faq_page.html            # FAQ
│   ├── full_page.html           # Полная версия
│   ├── page.html                # Базовый шаблон
│   ├── reviews_page.html        # Отзывы
│   └── sk-tu-homepage.html      # Главная страница
├── scripts/                     # Скрипты анализа
│   ├── analyze.py               # Извлечение meta-тегов
│   ├── seo_audit_collector.py   # Полный SEO-аудит сайта
│   ├── gsc_collect_data.py      # Сбор данных из Google Search Console
│   ├── py_test.txt              # Тестовые данные
│   └── test.txt                 # Тестовые данные
├── site_analysis/               # Анализ сайта
│   ├── site_analysis.html       # HTML-отчёт
│   └── site_content.txt         # Содержимое сайта
└── skills/                      # Навыки для cline
    ├── 1. andrej-karpathy-skills/
    ├── 2. seo-aeo-geo-visibility-architect/
    └── 3. agentmemory/
```

## Что где искать

| Что нужно | Где искать |
|-----------|------------|
| HTML-страницы сайта | `html_pages/` |
| Результаты анализа | `site_analysis/` |
| Скрипты для анализа | `scripts/` |
| Исходные данные (CSV) | `data/raw/` |
| Документация | `docs/` |
| Конфигурация навыков | `data/skills-lock.json` |

## Описание

Проект: SEO/AEO/GEO аудит сайта "СК Теплый Угол" (sk-tu.ru, msk.sk-tu.ru)

- **SEO** - поисковая оптимизация
- **AEO** - ответовая поисковая оптимизация
- **GEO** - географическая поисковая оптимизация

## Результаты SEO-аудита (2026-06-16)

### sk-tu.ru (Санкт-Петербург)

| Метрика | Значение |
|---------|----------|
| Страниц проверено | 761 |
| HTTP 200 | 761 (100%) |
| Без Title | 0 |
| Без Description | 3 |
| Без Schema.org | 761 (100%) — **критично!** |
| Без Canonical | 0 |
| Изображений без alt | 39 650 |
| Потенциальных дублей | 1 (index.php) |
| robots.txt блок CSS | ✅ Нет |
| robots.txt блок JS | ✅ Нет |

### msk.sk-tu.ru (Москва)

| Метрика | Значение |
|---------|----------|
| Страниц проверено | 761 |
| HTTP 200 | 761 (100%) |
| Без Title | 0 |
| Без Description | 0 |
| Без Schema.org | 761 (100%) — **критично!** |
| Без Canonical | 0 |
| Изображений без alt | 39 650 |
| Потенциальных дублей | 1 (index.php) |
| robots.txt блок CSS | ✅ Нет |
| robots.txt блок JS | ✅ Нет |

### Критические проблемы
1. **Отсутствие Schema.org** — 100% страниц на обоих сайтах без структурированных данных
2. **Изображения без alt** — ~39 650 изображений без описания (SEO + доступность)
3. **Дубли** — index.php на обоих сайтах, дополнительно pk-102/pk-103 на msk

### Архив проекта
`seo-audit-sk-tu-ru.zip` (33.5 МБ) в `C:\Users\user\Desktop\cline\`

## GitHub

Репозиторий: `htsgladiatis/seo-audit-sk-tu-ru`

---
*Обновлено: 2026-06-16*
