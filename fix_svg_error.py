import re
import os

files_to_fix = ['tools-phones.html', 'tools-compare.html']

for file in files_to_fix:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # The buggy code is injecting a raw SVG string that breaks the onerror attribute quotes.
    # It looks like:
    # let placeholder = `data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100"><rect width="100" height="100" fill="%231f2937"/><text x="50%" y="50%" font-family="Arial" font-size="14" fill="%239ca3af" text-anchor="middle" dy=".3em">Phone Placeholder</text></svg>`;

    # Better approach is to use base64 encoding to avoid any quote issues inside the SVG string breaking the HTML attributes.
    base64_placeholder_string = "`data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDAiIGhlaWdodD0iMTAwIj48cmVjdCB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgZmlsbD0iIzFmMjkzNyIvPjx0ZXh0IHg9IjUwJSIgeT0iNTAlIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTQiIGZpbGw9IiM5Y2EzYWYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGR5PSIuM2VtIj5QaG9uZTwvdGV4dD48L3N2Zz4=`"

    # Match the previous placeholder assignment
    old_placeholder_pattern = r"let placeholder = `data:image/svg\+xml;utf8,<svg xmlns=\"http://www\.w3\.org/2000/svg\" width=\"100\" height=\"100\"><rect width=\"100\" height=\"100\" fill=\"%231f2937\"/><text x=\"50%\" y=\"50%\" font-family=\"Arial\" font-size=\"14\" fill=\"%239ca3af\" text-anchor=\"middle\" dy=\"\.3em\">Phone Placeholder</text></svg>`;"
    
    new_placeholder_line = f"let placeholder = {base64_placeholder_string};"
    
    if re.search(old_placeholder_pattern, content):
        new_content = re.sub(old_placeholder_pattern, new_placeholder_line, content)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {file}")
    else:
        print(f"Pattern not found in {file}")

