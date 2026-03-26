import re

def replace_in_file(path, old, new):
    with open(path, "r") as f:
        content = f.read()
    content = content.replace(old, new)
    with open(path, "w") as f:
        f.write(content)

replace_in_file("/app/kinantouch22.com/robots.txt", "https://kinantouch.com/sitemap.xml", "https://kinanmjeed88.github.io/kinantouch22.com/sitemap.xml")
replace_in_file("/app/kinantouch22.com/vite.config.ts", "kinantouch.com", "kinanmjeed88.github.io/kinantouch22.com")
