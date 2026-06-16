import csv, json

# Read CSV and get top queries by clicks (sum both domains)
queries = {}
for csv_file in ['data/raw/sk-tu.ru_25bf9db0d98391dd73015adb.csv', 'data/raw/msk.sk-tu.ru_c6d72ee0451ea5f89f837eab.csv']:
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                if len(row) >= 4:
                    query = row[0].strip('"')
                    try:
                        clicks = float(row[3].strip('"'))
                    except:
                        clicks = 0
                    queries[query] = queries.get(query, 0) + clicks
    except FileNotFoundError:
        pass

# Sort by clicks
sorted_queries = sorted(queries.items(), key=lambda x: x[1], reverse=True)

# Generate HTML rows
html_rows = []
for i, (q, c) in enumerate(sorted_queries[:50], 1):
    clicks_str = f'{int(c):,}'.replace(',', ' ')
    html_rows.append(f'              <tr><td class="td-rank">#{i}</td><td><strong>{q}</strong></td><td class="td-pos-good">{clicks_str}</td></tr>')

html = '\n'.join(html_rows)

# Save to file
with open('data/top50_keywords_html.txt', 'w', encoding='utf-8') as f:
    f.write(html)

print('HTML table rows saved to data/top50_keywords_html.txt')
print('\nPreview (first 10):')
print('\n'.join(html_rows[:10]))
