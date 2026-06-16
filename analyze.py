import re  
with open("page.html","r",encoding="utf-8") as f: content = f.read()  
metas = re.findall(r"<meta[^>]+>",content)  
for m in metas: print(m.strip()) 
