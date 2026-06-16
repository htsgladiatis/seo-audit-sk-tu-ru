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

# Save as JSON
result = []
for q, c in sorted_queries[:50]:
    result.append([q, int(c)])

with open('data/top50_keywords_by_clicks.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print('Top 50 queries by clicks (sum of both domains):')
print('='*80)
for i, (q, c) in enumerate(sorted_queries[:50], 1):
    print(f'{i:2d}. {q:55s} | {int(c):>6d}')
