#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import re
import urllib.parse
import json
from collections import Counter
from pathlib import Path

keywords = []
for f in Path('data/raw').glob('*.csv'):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            url = row.get('url', '')
            decoded = urllib.parse.unquote(url).lstrip('/')
            for part in decoded.split('/'):
                if part in ('', 'catalog', 'articles', 'portfolio', 'rabotyi', 'o-nas', 'stati', 'katalog', 'doma-iz-brusa', 'karkasnye-doma', 'dachnye-doma', 'doma-pod-klyuch', 'bani-iz-brusa', 'karkasnye-bani', 'proyekty', 'page', 'filters', 'print', 'reviews'):
                    continue
                if '?' in part or '&' in part or '=' in part:
                    continue
                if re.match(r'^(pk|dk|db|dd|bk)-\d+', part):
                    continue
                if part.endswith(('.html', '.xml', '.docx')):
                    continue
                clean = part.replace('-', ' ').replace('_', ' ').strip()
                if clean and len(clean) > 2:
                    keywords.append(clean.lower())

counter = Counter(keywords)
top50 = counter.most_common(50)

with open('data/top50_keywords.json', 'w', encoding='utf-8') as f:
    json.dump(top50, f, ensure_ascii=False, indent=2)

print(f'Saved {len(top50)} keywords to data/top50_keywords.json')
