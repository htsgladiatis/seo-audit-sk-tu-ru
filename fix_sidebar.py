import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the s9 nav item and add s10, s11 after it
old_text = '      <a class="nav-item" href="#s9"><span class="nav-dot dot-green"></span>9. Чек-лист</a>\n    </div>'
new_text = '      <a class="nav-item" href="#s9"><span class="nav-dot dot-green"></span>9. Чек-лист</a>\n      <a class="nav-item" href="#s10"><span class="nav-dot dot-blue"></span>10. Топ-50 ключевых слов</a>\n      <a class="nav-item" href="#s11"><span class="nav-dot dot-green"></span>11. Потенциальные ключевые слова</a>\n    </div>'

if old_text in content:
    content = content.replace(old_text, new_text)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('SUCCESS: Sidebar updated with s10 and s11 links')
else:
    print('ERROR: Could not find the sidebar section to replace')
    # Try to find what's there
    match = re.search(r'href="#s9".*?</a>\s*</div>', content, re.DOTALL)
    if match:
        print('Found:', repr(match.group()[:200]))
