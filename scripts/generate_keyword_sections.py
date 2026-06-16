#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

# Читаем данные
with open('data/top50_keywords.json', 'r', encoding='utf-8') as f:
    top50 = json.load(f)

with open('data/potential_keywords.json', 'r', encoding='utf-8') as f:
    potential = json.load(f)

# Генерируем HTML для Топ-50
top50_rows = ""
for i, (keyword, count) in enumerate(top50, 1):
    top50_rows += f'              <tr><td class="td-rank">#{i}</td><td><strong>{keyword}</strong></td><td class="td-pos-good">{count:,}</td></tr>\n'

# Генерируем HTML для потенциальных
potential_rows = ""
for i, (keyword, conv_type) in enumerate(potential, 1):
    pill_class = "pill-green" if "Высокая" in conv_type else ("pill-yellow" if "Средняя" in conv_type else "pill-blue")
    potential_rows += f'              <tr><td class="td-rank">#{i}</td><td><strong>{keyword}</strong></td><td><span class="pill {pill_class}">{conv_type}</span></td></tr>\n'

html = f'''    <!-- SECTION 10: Топ-50 ключевых слов -->
    <section id="s10" class="section">
      <div class="section-header">
        <div class="section-icon icon-blue">🔑</div>
        <div class="section-title-wrap">
          <div class="section-number">Раздел 10</div>
          <div class="section-title">Топ-50 ключевых слов по трафику</div>
        </div>
        <span class="pill pill-blue">На основе обхода 51 492 URL</span>
      </div>
      <div class="section-body">
        <p>Ключевые слова, выделенные из URL-структуры сайта и HTML-заголовков страниц. Частота показывает, сколько раз данная фраза встречается в обходе поисковых систем.</p>
        <div class="table-wrap">
          <table>
            <thead><tr><th>№</th><th>Ключевое слово / фраза</th><th>Частота в обходе</th></tr></thead>
            <tbody>
{top50_rows}            </tbody>
          </table>
        </div>
        <div class="obs-block">
          <div class="obs-icon">💡</div>
          <div class="obs-text"><span class="obs-tag">ИНСАЙТ</span>«Каркасные дома» — абсолютный лидер (11 545 упоминаний). Это подтверждает, что основной трафик идёт на каркасное строительство. Дома из бруса и дачные дома — второстепенные, но важные направления для расширения семантики.</div>
        </div>
      </div>
    </section>

    <!-- SECTION 11: 50 потенциальных ключевых слов -->
    <section id="s11" class="section">
      <div class="section-header">
        <div class="section-icon icon-green">🎯</div>
        <div class="section-title-wrap">
          <div class="section-number">Раздел 11</div>
          <div class="section-title">50 потенциальных ключевых слов</div>
        </div>
        <span class="pill pill-green">Рекомендации</span>
      </div>
      <div class="section-body">
        <p>Ключевые слова и фразы, которых <strong>нет</strong> в текущей семантике сайта, но которые потенциально могут привести конверсионный трафик. Сгруппированы по приоритету внедрения.</p>
        <div class="table-wrap">
          <table>
            <thead><tr><th>№</th><th>Ключевое слово / фраза</th><th>Конверсия</th></tr></thead>
            <tbody>
{potential_rows}            </tbody>
          </table>
        </div>
        <div class="grid-2">
          <div class="info-card">
            <div class="info-card-title">🟢 Высокая конверсия</div>
            <ul>
              <li>Запросы с ценовым интентом («цена», «под ключ», «купить»)</li>
              <li>Региональные запросы («спб», «москва», «московская область»)</li>
              <li>Рекомендуется внедрить в первую очередь</li>
            </ul>
          </div>
          <div class="info-card">
            <div class="info-card-title">🟡 Средняя конверсия</div>
            <ul>
              <li>Размерные запросы («6x6», «8x8», «10x10»)</li>
              <li>Функциональные («с мансардой», «с террасой», «с баней»)</li>
              <li>Информационные с коммерческим потенциалом</li>
            </ul>
          </div>
        </div>
        <div class="alert alert-green">
          <div class="alert-icon">✅</div>
          <div class="alert-content">
            <div class="alert-title">Рекомендация по внедрению</div>
            <div class="alert-text">Создать отдельные посадочные страницы под высококонверсионные запросы (например, «Каркасные дома под ключ в СПБ», «Дома из бруса 6x6 цена»). Для средней конверсии — добавить фильтры и мета-теги в существующий каталог.</div>
          </div>
        </div>
      </div>
    </section>
'''

with open('scripts/keyword_sections.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Generated scripts/keyword_sections.html')
