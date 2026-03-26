import re

files_to_fix = ['tools-phones.html', 'tools-compare.html']

svg_data_uri = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjOUNBM0FGIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHJlY3QgeD0iNSIgeT0iMiIgd2lkdGg9IjE0IiBoZWlnaHQ9IjIwIiByeD0iMiIgcnk9IjIiPjwvcmVjdD48bGluZSB4MT0iMTIiIHkxPSIxOCIgeDI9IjEyLjAxIiB5Mj0iMTgiPjwvbGluZT48L3N2Zz4="

for file in files_to_fix:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for onerror attribute
    pattern1 = r"""onerror="this\.onerror=null; this\.src='data:image/svg\+xml;utf8,<svg[^>]+>.*?<\/svg>';\""""
    replacement1 = f"""onerror="this.onerror=null; this.src='{svg_data_uri}';\""""
    
    # Pattern for src attribute when no image exists
    pattern2 = r"""src="data:image/svg\+xml;utf8,<svg[^>]+>.*?<\/svg>\""""
    replacement2 = f"""src="{svg_data_uri}\""""

    new_content = re.sub(pattern1, replacement1, content)
    new_content = re.sub(pattern2, replacement2, new_content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Fixed {file}")

