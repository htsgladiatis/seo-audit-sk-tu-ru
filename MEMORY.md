# Память проекта: SK Tepliy Ugol SEO Audit

## Дата: 2026-06-16

## Контекст
Проект SEO/AEO/GEO аудита сайта "СК Теплый Угол" (sk-tu.ru, msk.sk-tu.ru).

## Ключевые результаты аудита

### sk-tu.ru (Санкт-Петербург)
- 761 страница проверена
- 3 страницы без Description
- 761 страница без Schema.org (100% — критично!)
- 39 650 изображений без alt
- 1 дубль: index.php

### msk.sk-tu.ru (Москва)
- 761 страница проверена
- 0 страниц без Title/Description
- 761 страница без Schema.org (100% — критично!)
- 39 650 изображений без alt
- 1 дубль: index.php

## Критические проблемы
1. **Schema.org отсутствует** — 100% страниц на обоих сайтах без структурированных данных
2. **Alt-теги** — ~39 650 изображений без описания
3. **Дубли** — index.php на обоих сайтах

## Структура проекта
- `data/raw/` — CSV/GZ данные GSC
- `data/seo_audit_*.json` — результаты аудита (761 стр. × 2)
- `scripts/` — seo_audit_collector.py, gsc_collect_data.py
- `docs/` — SKILL_SEO_AUDIT.md (алгоритм аудита)
- `html_pages/` — сохранённые HTML-страницы

## Архив
`seo-audit-sk-tu-ru.zip` (33.5 МБ) в `C:\Users\user\Desktop\cline\`

## Следующие шаги (если вернёмся)
- [ ] Добавить Schema.org (Organization, Service, Product, FAQ)
- [ ] Прописать alt-теги для изображений
- [ ] Убрать дубли (редирект index.php → /)
- [ ] Собрать данные GSC через gsc_collect_data.py (нужен токен)
- [ ] Сформировать приоритизированный план исправлений

## GitHub
Репозиторий: `htsgladiatis/seo-audit-sk-tu-ru`
