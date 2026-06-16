# PROJECT BUNDLE: seo-audit-sk-tu-ru
# SEO/AEO/GEO Audit - SK Tepliy Ugol
# Generated: 2026-06-16

## File tree

```
07. SK Tepliy Ugol/
├── README.md                    # Документация проекта
├── docs/                        # Документация и отчёты (пусто)
├── html_pages/                  # Сохранённые HTML-страницы
│   ├── about_page.html          # О компании
│   ├── catalog_page.html        # Каталог
│   ├── contacts_page.html       # Контакты
│   ├── faq_page.html            # FAQ
│   ├── full_page.html           # Полная версия
│   ├── page.html                # Базовый шаблон
│   ├── reviews_page.html        # Отзывы
│   └── sk-tu-homepage.html      # Главная страница
├── site_analysis/               # Анализ сайта
│   ├── site_analysis.html       # HTML-отчёт
│   └── site_content.txt         # Содержимое сайта
├── scripts/                     # Скрипты анализа
│   ├── analyze.py               # Python-скрипт (meta-теги)
│   ├── py_test.txt              # Тестовые данные
│   └── test.txt                 # Тестовые данные
├── data/                        # Данные
│   ├── raw/                     # CSV/GZ файлы (данные сайта)
│   │   ├── msk.sk-tu.ru_*.csv   # Данные с msk.sk-tu.ru
│   │   ├── msk.sk-tu.ru_*.gz    # Архивы msk
│   │   ├── sk-tu.ru_*.csv       # Данные с sk-tu.ru
│   │   └── sk-tu.ru_*.gz        # Архивы sk-tu.ru
│   ├── state_store.db/          # База agentmemory
│   ├── stream_store/            # Хранилище потоков
│   └── skills-lock.json         # Конфигурация навыков
├── .agents/                     # Агентские навыки
├── skills/                      # Дополнительные навыки
│   ├── 1. andrej-karpathy-skills/
│   ├── 2. seo-aeo-geo-visibility-architect/
│   └── 3. agentmemory/
└── .git/                        # Git репозиторий
```

## Описание проекта

Проект: SEO/AEO/GEO аудит сайта строительной компании "СК Теплый Угол"

**Домены:**
- sk-tu.ru (основной)
- msk.sk-tu.ru (поддомен Москва)

**Направления аудита:**
- **SEO** - поисковая оптимизация
- **AEO** - Answer Engine Optimization
- **GEO** - географическая оптимизация

**GitHub:** htsgladiatis/seo-audit-sk-tu-ru

---

## FILE: README.md

# SK Tepliy Ugol - SEO/AEO/GEO Audit Project

## Структура проекта

```
07. SK Tepliy Ugol/
├── README.md                    # Документация проекта
├── data/
│   ├── raw/                     # Исходные данные (CSV/GZ файлы)
│   │   ├── msk.sk-tu.ru_*.csv   # Данные с msk.sk-tu.ru
│   │   ├── msk.sk-tu.ru_*.gz    # Сжатые данные msk
│   │   ├── sk-tu.ru_*.csv       # Данные с sk-tu.ru
│   │   └── sk-tu.ru_*.gz        # Сжатые данные sk-tu.ru
│   ├── state_store.db/          # База данных agentmemory
│   ├── stream_store/            # Хранилище потоков
│   └── skills-lock.json         # Конфигурация навыков
├── docs/                        # Документация и отчёты
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
| HTML-страницы сайта | html_pages/ |
| Результаты анализа | site_analysis/ |
| Скрипты для анализа | scripts/ |
| Исходные данные (CSV) | data/raw/ |
| Документация | docs/ |
| Конфигурация навыков | data/skills-lock.json |

## Описание

Проект: SEO/AEO/GEO аудит сайта "СК Теплый Угол" (sk-tu.ru, msk.sk-tu.ru)

- SEO - поисковая оптимизация
- AEO - ответовая поисковая оптимизация
- GEO - географическая поисковая оптимизация

## GitHub

Репозиторий: htsgladiatis/seo-audit-sk-tu-ru

---

## FILE: scripts/analyze.py

import re  
with open("page.html","r",encoding="utf-8") as f: content = f.read()  
metas = re.findall(r"<meta[^>]+>",content)  
for m in metas: print(m.strip()) 

---

## FILE: data/skills-lock.json

{
  "version": 1,
  "skills": {
    "agentmemory-agents": {
      "source": "rohitg00/agentmemory",
      "sourceType": "github",
      "skillPath": "plugin/skills/agentmemory-agents/SKILL.md",
      "computedHash": "651a4c714ebcefa0ffaa545995ed9933eb3043069bf76cf94335cc7fad7e35eb"
    },
    "agentmemory-architecture": {
      "source": "rohitg00/agentmemory",
      "sourceType": "github",
      "skillPath": "plugin/skills/agentmemory-architecture/SKILL.md",
      "computedHash": "2ca47add8385e45bd956d2233a160bdf3cdef7eab5a32e29b402f589195758ad"
    },
    "agentmemory-config": {
      "source": "rohitg00/agentmemory",
      "sourceType": "github",
      "skillPath": "plugin/skills/agentmemory-config/SKILL.md",
      "computedHash": "d3370a7ad71df628e01d02a58fa5757c6a27c95e3cbf65004c679681341284c6"
    },
    "commit-context": {
      "source": "rohitg00/agentmemory",
      "sourceType": "github",
      "skillPath": "plugin/skills/commit-context/SKILL.md",
      "computedHash": "279edb6dcaf8d51dbc84878c9d654e473f508c44c44e5e7c1d2daa65ad72f0ad"
    },
    "commit-history": {
      "source": "rohitg00/agentmemory",
      "sourceType": "github",
      "skillPath": "plugin/skills/commit-history/SKILL.md",
      "computedHash": "cf337496577dc9d7229b9f5d371c2dc0a837e4cc94ae39073eac1ab361fd0acf"
    },
    "forget": {
      "source": "rohitg00/agentmemory",
      "sourceType": "github",
      "skillPath": "plugin/skills/forget/SKILL.md",
      "computedHash": "791ad36f801055ed08107dc0d86a43ac31fa6760016a140acf11df96a975cb1c"
    },
    "handoff": {
      "source": "rohitg00/agentmemory",
      "sourceType": "github",
      "skillPath": "plugin/skills/handoff/SKILL.md",
      "computedHash": "f915ba05033ded7c905f6edfaf4e946e2f430deb642a83c51453c51a37f27e11"
    },
    "recall": {
      "source": "rohitg00/agentmemory",
      "sourceType": "github",
      "skillPath": "plugin/skills/recall/SKILL.md",
      "computedHash": "9a335c621588a47ab45e1cd8293ee7d6a03f681e40d4dc3de3c222506c13d16c"
    },
    "recap": {
      "source": "rohitg00/agentmemory",
      "sourceType": "github",
      "skillPath": "plugin/skills/recap/SKILL.md",
      "computedHash": "8c48af4454651cd50493d497186afce75abbaca7483f9ccb368bc893da8f9549"
    },
    "remember": {
      "source": "rohitg00/agentmemory",
      "sourceType": "github",
      "skillPath": "plugin/skills/remember/SKILL.md",
      "computedHash": "ed55bb7213947c89d4dd29ac908fd7619955c51afbf8df58bccb9ca44dc34656"
    },
    "session-history": {
      "source": "rohitg00/agentmemory",
      "sourceType": "github",
      "skillPath": "plugin/skills/session-history/SKILL.md",
      "computedHash": "791295c3d83f1e765ba380c74e9e231b767337eda3768d9346e399c1e776f5f3"
    },
    "write-agentmemory-skill": {
      "source": "rohitg00/agentmemory",
      "sourceType": "github",
      "skillPath": "plugin/skills/write-agentmemory-skill/SKILL.md",
      "computedHash": "a437f4b060c6d60769d32247ab075b08218c8eec880d81403631def2eca426ae"
    }
  }
}

---

## DATA FILES (CSV)

### data/raw/msk.sk-tu.ru_abe52232787b9b5d5fa1d189.csv
(Содержимое CSV файла с данными анализа msk.sk-tu.ru)

### data/raw/msk.sk-tu.ru_c6d72ee0451ea5f89f837eab.csv
(Содержимое CSV файла с данными анализа msk.sk-tu.ru)

### data/raw/sk-tu.ru_25bf9db0d98391dd73015adb.csv
(Содержимое CSV файла с данными анализа sk-tu.ru)

### data/raw/sk-tu.ru_73526315c1a61b45fcf1ad9e.csv
(Содержимое CSV файла с данными анализа sk-tu.ru)

### data/raw/sk-tu.ru_9478b733827e7d3512957453.csv
(Содержимое CSV файла с данными анализа sk-tu.ru)

### data/raw/sk-tu.ru_c00f73b1e96bd1a9a6de4456.csv
(Содержимое CSV файла с данными анализа sk-tu.ru)

---

## HTML PAGES SUMMARY

### html_pages/sk-tu-homepage.html
Главная страница сайта sk-tu.ru - сохранённый HTML с домашней страницы строительной компании "СК Теплый Угол".

### html_pages/about_page.html
Страница "О компании" - информация о компании-застройщике.

### html_pages/catalog_page.html
Страница каталога проектов домов.

### html_pages/contacts_page.html
Контактная информация компании.

### html_pages/faq_page.html
Вопросы и ответы (FAQ).

### html_pages/reviews_page.html
Страница отзывов клиентов.

### html_pages/page.html
Базовый HTML-шаблон страницы.

### html_pages/full_page.html
Полная версия страницы (возможно, страница услуг).

---

## SITE ANALYSIS

### site_analysis/site_analysis.html
HTML-отчёт с анализом сайта (мета-теги, структура и т.д.)

### site_analysis/site_content.txt
Полный HTML-код сохранённой страницы сайта (содержит head с meta-тегами, body со структурой страницы)

---

## KEY METADATA FROM site_content.txt

Сайт: msk.sk-tu.ru (Московский поддомен)
Title: Сруб дома из бревна в Москве и Московской области от производителя, цены, отзывы и фото
Description: Профессиональное строительство срубов из бревна в Москве и области. Цены, фото, отзывы, калькулятор. СК Теплый Угол - надежный застройщик.
Canonical: https://msk.sk-tu.ru/

---

## SKILLS INFO

### skills/2. seo-aeo-geo-visibility-architect/
SEO/AEO/GEO Visibility Architect - навык для работы с поисковой оптимизацией, Answer Engine Optimization и географической оптимизацией.

### skills/3. agentmemory/
AgentMemory - система памяти для сохранения контекста между сессиями.

### skills/1. andrej-karpathy-skills/
Руководства и примеры от Andrej Karpathy по работе с AI-агентами.

---

## NOTES FOR ASSISTANT

1. Это локальная копия репозитория seo-audit-sk-tu-ru
2. CSV файлы содержат экспортированные данные из Яндекс Вебмастера и других аналитических систем
3. GZ файлы - архивированные дампы данных
4. HTML файлы - сохранённые версии страниц сайта для оффлайн-анализа
5. Для получения полного содержимого CSV/TXT/HTML файлов требуется их прочитать отдельно
6. Проект связан с GitHub: https://github.com/htsgladiatis/seo-audit-sk-tu-ru

---
*END OF PROJECT BUNDLE*