#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import re
import urllib.parse
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
print('=== TOP 50 KEYWORDS ===')
for kw, count in counter.most_common(50):
    print(f'{count:4d} | {kw}')
