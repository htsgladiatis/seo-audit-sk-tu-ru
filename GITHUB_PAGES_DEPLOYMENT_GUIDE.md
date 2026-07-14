# 📊 GitHub Pages: Способы и места размещения отчетов

## 🎯 Общая информация

Проект "СК Тёплый Угол" использует **GitHub Pages** для публикации двух типов отчетов:

1. **SEO-отчет** (SEO/AEO/GEO аудит)
2. **Маркетинговый дашборд** (интерактивный)

---

## 📁 Два GitHub-репозитория

### 1. SEO-отчет: `htsgladiatis/seo-audit-sk-tu-ru`

**Репозиторий:** https://github.com/htsgladiatis/seo-audit-sk-tu-ru  
**GitHub Pages URL:** https://htsgladiatis.github.io/seo-audit-sk-tu-ru/  
**Главный файл:** `index.html` (корень репозитория)  
**Ветка:** `master`  

**Расположение на локальной машине:**
```
C:\Users\user\Desktop\AI Проекты\cline\07. SK Tepliy Ugol\
```

### 2. Маркетинговый дашборд: `htsgladiatis/sk-tu-dashboard`

**Репозиторий:** https://github.com/htsgladiatis/sk-tu-dashboard  
**GitHub Pages URL:** https://htsgladiatis.github.io/sk-tu-dashboard/  
**Главный файл:** `index.html` (корень репозитория)  
**Ветка:** `main`  

**Расположение на локальной машине:**
```
C:\Users\user\Desktop\AI Проекты\cline\07. SK Tepliy Ugol\sk-tu-dashboard-deploy\
```

---

## 🔧 Настройка GitHub Pages

### Для обоих репозиториев используется:

- **Source:** Deploy from a branch
- **Branch:** `master` (SEO-отчет) или `main` (дашборд)
- **Folder:** `/ (root)`
- **Jekyll:** отключен (файл `.nojekyll` в корне)

### Почему `.nojekyll`?

Файл `.nojekyll` отключает обработку Jekyll на GitHub Pages, чтобы:
- Статические HTML-файлы публиковались "как есть"
- Не игнорировались папки, начинающиеся с `_`
- Ускорялась публикация

---

## 🚀 Способ деплоя

### 🔐 Аутентификация через Personal Access Token (PAT)

Оба репозитория используют **GitHub Personal Access Token** для push:

#### SEO-отчет:
```bash
origin https://htsgladiatis:ghp_REDACTED_SEO@github.com/htsgladiatis/seo-audit-sk-tu-ru.git
```

#### Маркетинговый дашборд:
```bash
origin https://ghp_REDACTED_DASHBOARD@github.com/htsgladiatis/sk-tu-dashboard.git
```

---

## 📝 Инструкции по обновлению отчетов

### 1️⃣ Обновление SEO-отчета

**Расположение:** `C:\Users\user\Desktop\AI Проекты\cline\07. SK Tepliy Ugol\`

```powershell
# 1. Отредактировать index.html или обновить данные
# (например, обновить топ-50 ключевых слов)

# 2. Убедиться, что .nojekyll существует
if (-not (Test-Path ".nojekyll")) { New-Item -ItemType File -Name ".nojekyll" }

# 3. Добавить изменения в git
git add index.html data/ scripts/ docs/ .nojekyll

# 4. Создать коммит
git commit -m "Обновление SEO-аудита: [описание изменений]"

# 5. Отправить на GitHub
git push origin master
```

**Автоматическая публикация:** GitHub Pages обновится через 1-3 минуты после push.

**Проверка:** https://htsgladiatis.github.io/seo-audit-sk-tu-ru/

---

### 2️⃣ Обновление маркетингового дашборда

#### Вариант А: Прямое редактирование в папке деплоя

**Расположение:** `C:\Users\user\Desktop\AI Проекты\cline\07. SK Tepliy Ugol\sk-tu-dashboard-deploy\`

```powershell
# 1. Отредактировать index.html в папке sk-tu-dashboard-deploy/

# 2. Добавить изменения
git -C "sk-tu-dashboard-deploy" add index.html

# 3. Создать коммит
git -C "sk-tu-dashboard-deploy" commit -m "update dashboard: [описание]"

# 4. Отправить на GitHub
git -C "sk-tu-dashboard-deploy" push origin main
```

#### Вариант Б: Копирование из рабочей версии

Если дашборд редактируется в другом месте (например, `C:\Users\user\Documents\Отчет СК\`):

```powershell
# 1. Скопировать обновленный файл
Copy-Item -Path "C:\Users\user\Documents\Отчет СК\dashboard_2026-06-15_2026-06-21.html" `
  -Destination "C:\Users\user\Desktop\AI Проекты\cline\07. SK Tepliy Ugol\sk-tu-dashboard-deploy\index.html" `
  -Force

# 2. Перейти в папку деплоя
cd "C:\Users\user\Desktop\AI Проекты\cline\07. SK Tepliy Ugol\sk-tu-dashboard-deploy"

# 3. Добавить изменения
git add index.html

# 4. Создать коммит
git commit -m "update dashboard: [описание]"

# 5. Отправить на GitHub
git push origin main
```

**Автоматическая публикация:** GitHub Pages обновится через 1-3 минуты после push.

**Проверка:** https://htsgladiatis.github.io/sk-tu-dashboard/

---

## 📊 История деплоев

### SEO-отчет (последние 5 коммитов)

```
d080570 docs: update PROJECT_DOCUMENTATION.md and L99 PROJECT_CONTEXT_SNAPSHOT.json
6af496c Обновление раздела 10: топ-50 ключевых слов по реальным кликам
14f75bf Add keyword analysis sections: Top-50 and 50 potential keywords
2bad560 Remove skills/3. agentmemory from git index
72066a2 Trigger new GitHub Pages build
```

### Маркетинговый дашборд (последние 10 коммитов)

```
86474d4 Добавлены SEO-данные для недели w1 (15-21.06.2026)
fe4576b feat: SEO-блоки разделены на 2 строки (СПБ и МСК раздельно)
5032864 fix: График SEO Performance теперь показывает 4 столбца с разными цветами
7be94db feat: Добавлены реальные данные поисковых запросов из Метрики
8d2c03b feat: Добавлены все 3 SEO-блока (график, страницы, запросы)
261852c feat: Добавлены SEO-блоки с топ-страницами
a148850 fix: Корректировка распределения ЦЛ по кампаниям МСК 4 ЦЛ СПБ 2 ЦЛ
18e9cf3 feat: Добавлен выбор недели (15-21 и 22-28 июня)
b5febf6 fix: Исправление количества лидов 98→106
2728d18 Обновление дашборда 22-28.06.2026: 171К расход, 98 лидов, 21 ЦЛ
```

---

## 🔍 Ключевые особенности

### SEO-отчет (`index.html`)

- **Размер:** 1284 строки HTML
- **Разделы:** 11 разделов аудита
- **Данные:** 
  - 761 страница × 2 домена = 1522 страницы
  - 51,492 URL обхода
  - Топ-50 ключевых слов по реальным кликам (суммарно с обоих доменов)
  - 50 потенциальных ключевых слов

### Маркетинговый дашборд (`sk-tu-dashboard-deploy/index.html`)

- **Размер:** ~984 строки HTML
- **Библиотеки:** Chart.js 4.4.0
- **Функционал:**
  - Переключение между неделями (w1: 15-21.06, w2: 22-28.06)
  - 6 KPI-карточек
  - 4 графика (кабинеты, каналы, воронка, SEO Performance)
  - Таблицы топ страниц и запросов для СПБ и МСК отдельно
  - SEO-блоки разделены на 2 строки (📍 СПБ и 📍 МСК)

---

## ⚠️ Важные замечания

### 🔐 Безопасность токенов

**ВНИМАНИЕ!** GitHub Personal Access Tokens хранятся в открытом виде в конфигурации git remote.

**Текущие токены:**
- SEO-отчет: `ghp_REDACTED_SEO`
- Дашборд: `ghp_REDACTED_DASHBOARD`

**Рекомендации:**
1. Токены имеют ограниченные права (только push в конкретные репозитории)
2. При компрометации - немедленно отозвать токены в GitHub Settings → Developer settings → Personal access tokens
3. Создать новые токены и обновить remote URL

### 📅 Актуальность данных

- **SEO-отчет:** данные за 16.03–14.06.2026 (90 дней)
- **Маркетинговый дашборд:** данные за две недели июня 2026:
  - w1: 15-21 июня
  - w2: 22-28 июня

---

## 🛠️ Проверка статуса деплоя

### SEO-отчет

```powershell
# Проверить статус репозитория
cd "C:\Users\user\Desktop\AI Проекты\cline\07. SK Tepliy Ugol"
git status

# Открыть отчет в браузере
start https://htsgladiatis.github.io/seo-audit-sk-tu-ru/
```

### Маркетинговый дашборд

```powershell
# Проверить статус репозитория
git -C "sk-tu-dashboard-deploy" status

# Открыть дашборд в браузере
start https://htsgladiatis.github.io/sk-tu-dashboard/
```

---

## 📚 Связанная документация

- **PROJECT_DOCUMENTATION.md** - основная документация проекта
- **PROJECT_CONTEXT_SNAPSHOT.json** - цифровой отпечаток L99
- **PROJECT_FULL_DOCUMENTATION.md** - полная документация разработки
- **README.md** - краткое описание проекта

---

## 🎯 Быстрая справка

| Что нужно обновить | Где редактировать | Куда деплоить | GitHub Pages URL |
|-------------------|-------------------|---------------|------------------|
| SEO-отчет | `./index.html` | `master` branch | https://htsgladiatis.github.io/seo-audit-sk-tu-ru/ |
| Маркетинговый дашборд | `./sk-tu-dashboard-deploy/index.html` | `main` branch | https://htsgladiatis.github.io/sk-tu-dashboard/ |

---

**Создано:** 6 июля 2026 г.  
**Версия:** 1.0
