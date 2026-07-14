# 🗺️ Схема деплоя отчетов на GitHub Pages

## 📊 Два независимых pipeline

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     ЛОКАЛЬНАЯ МАШИНА                                     │
│  C:\Users\user\Desktop\AI Проекты\cline\07. SK Tepliy Ugol\             │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
       
┌──────────────────────────────┐      ┌──────────────────────────────┐
│   📄 SEO-ОТЧЕТ               │      │   📊 МАРКЕТИНГОВЫЙ ДАШБОРД   │
├──────────────────────────────┤      ├──────────────────────────────┤
│ Файл: index.html             │      │ Папка: sk-tu-dashboard-      │
│       (корень проекта)       │      │        deploy/               │
│                              │      │ Файл: index.html             │
│ Git Remote:                  │      │                              │
│ htsgladiatis/                │      │ Git Remote:                  │
│ seo-audit-sk-tu-ru           │      │ htsgladiatis/                │
│                              │      │ sk-tu-dashboard              │
│ Branch: master               │      │                              │
│                              │      │ Branch: main                 │
└──────────────┬───────────────┘      └──────────────┬───────────────┘
               │                                     │
               │ git push origin master              │ git push origin main
               │                                     │
               ▼                                     ▼
┌──────────────────────────────┐      ┌──────────────────────────────┐
│   🐙 GITHUB REPOSITORY       │      │   🐙 GITHUB REPOSITORY       │
├──────────────────────────────┤      ├──────────────────────────────┤
│ htsgladiatis/                │      │ htsgladiatis/                │
│ seo-audit-sk-tu-ru           │      │ sk-tu-dashboard              │
│                              │      │                              │
│ ✅ GitHub Pages: Enabled     │      │ ✅ GitHub Pages: Enabled     │
│    Source: master / (root)   │      │    Source: main / (root)     │
│    .nojekyll: ✓              │      │    .nojekyll: ✓ (optional)   │
└──────────────┬───────────────┘      └──────────────┬───────────────┘
               │                                     │
               │ Auto-deploy (1-3 min)               │ Auto-deploy (1-3 min)
               │                                     │
               ▼                                     ▼
┌──────────────────────────────┐      ┌──────────────────────────────┐
│   🌐 GITHUB PAGES            │      │   🌐 GITHUB PAGES            │
├──────────────────────────────┤      ├──────────────────────────────┤
│ htsgladiatis.github.io/      │      │ htsgladiatis.github.io/      │
│ seo-audit-sk-tu-ru/          │      │ sk-tu-dashboard/             │
│                              │      │                              │
│ 📄 Статический SEO-отчет     │      │ 📊 Интерактивный дашборд     │
│    11 разделов               │      │    Chart.js, 2 недели        │
│    1522 страницы аудита      │      │    6 KPI, 4 графика          │
│    Топ-50 ключевых слов      │      │    SEO-блоки СПБ/МСК         │
└──────────────────────────────┘      └──────────────────────────────┘
```

---

## 🔄 Процесс обновления

### SEO-отчет

```
Редактирование       Git операции              GitHub Pages
───────────────      ─────────────              ────────────

┌──────────┐         ┌──────────┐               ┌──────────┐
│ Изменить │         │   git    │               │  GitHub  │
│ index.   │  ──────>│   add    │  ──────────>  │  Pages   │
│ html     │         │  commit  │   Auto-build  │ обновлен │
│          │         │   push   │               │          │
└──────────┘         └──────────┘               └──────────┘
                                                      │
                                                      ▼
                                            Доступен через 1-3 мин
                                    https://htsgladiatis.github.io/
                                    seo-audit-sk-tu-ru/
```

### Маркетинговый дашборд (2 варианта)

#### Вариант А: Прямое редактирование

```
sk-tu-dashboard-deploy/        Git операции              GitHub Pages
──────────────────────         ─────────────              ────────────

┌──────────┐                   ┌──────────┐               ┌──────────┐
│ Изменить │                   │ git -C   │               │  GitHub  │
│ index.   │  ──────────────>  │ "sk-tu-" │  ──────────>  │  Pages   │
│ html     │                   │ push     │   Auto-build  │ обновлен │
└──────────┘                   └──────────┘               └──────────┘
```

#### Вариант Б: Копирование из рабочей версии

```
C:\Users\user\Documents\       sk-tu-dashboard-deploy/    GitHub Pages
Отчет СК\                      ─────────────────────      ────────────
─────────                      

┌──────────┐    Copy-Item      ┌──────────┐  git push    ┌──────────┐
│ Рабочая  │  ─────────────>   │ Деплой   │  ─────────>  │  GitHub  │
│ копия    │                   │ копия    │              │  Pages   │
│ dashboard│                   │ index.   │              │ обновлен │
│  .html   │                   │ html     │              │          │
└──────────┘                   └──────────┘              └──────────┘
```

---

## 🔐 Аутентификация

```
┌─────────────────────────────────────────────────────────┐
│           GitHub Personal Access Token (PAT)            │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  SEO-отчет:                                             │
│  ghp_REDACTED_SEO              │
│                                                         │
│  Маркетинговый дашборд:                                 │
│  ghp_REDACTED_DASHBOARD              │
│                                                         │
│  Хранится в: git remote URL                             │
│  Формат: https://TOKEN@github.com/user/repo.git         │
└─────────────────────────────────────────────────────────┘
```

---

## 📁 Структура файлов

### SEO-отчет (корень проекта)

```
07. SK Tepliy Ugol/
├── index.html          ⭐ Главный файл для GitHub Pages
├── .nojekyll           ⭐ Отключает Jekyll
├── README.md
├── data/               📊 Данные аудита
├── scripts/            🔧 Скрипты Python
└── docs/               📄 Документация
    
Git remote:
→ https://github.com/htsgladiatis/seo-audit-sk-tu-ru

GitHub Pages:
→ https://htsgladiatis.github.io/seo-audit-sk-tu-ru/
```

### Маркетинговый дашборд (подпапка)

```
07. SK Tepliy Ugol/
└── sk-tu-dashboard-deploy/    🚀 Отдельный git-репозиторий
    ├── .git/
    └── index.html             ⭐ Главный файл для GitHub Pages

Git remote:
→ https://github.com/htsgladiatis/sk-tu-dashboard

GitHub Pages:
→ https://htsgladiatis.github.io/sk-tu-dashboard/
```

---

## ⏱️ Timeline деплоя

```
Время     Действие                      Статус
────────  ─────────────────────────     ─────────────────
00:00     git push origin master/main   ⬆️ Отправка на GitHub
00:05     GitHub получил коммит          ✅ Коммит виден
00:30     GitHub Actions начал сборку    🔄 Building...
02:00     Деплой завершен                ✅ Сайт обновлен
03:00     Изменения видны всем           🌐 Доступно публично
```

---

## 🎯 Ключевые моменты

| Аспект | SEO-отчет | Маркетинговый дашборд |
|--------|-----------|----------------------|
| Репозиторий | `seo-audit-sk-tu-ru` | `sk-tu-dashboard` |
| Ветка | `master` | `main` |
| Файл | `./index.html` | `./sk-tu-dashboard-deploy/index.html` |
| URL | `/seo-audit-sk-tu-ru/` | `/sk-tu-dashboard/` |
| Размер | 1284 строки | ~984 строки |
| Технологии | HTML, CSS, JS | HTML, CSS, JS, Chart.js |
| Данные | Статичные (16.03-14.06.2026) | Динамичные (2 недели июня) |
| Обновление | По мере изменения данных | Еженедельно |

---

**Создано:** 6 июля 2026 г.
