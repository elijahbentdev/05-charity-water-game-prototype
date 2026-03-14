import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Extract CSS
css_match = re.search(r'<style>\s*(.*?)\s*</style>', html, re.DOTALL)
if css_match:
    css_content = css_match.group(1)
    with open("game.css", "w", encoding="utf-8") as f:
        f.write(css_content)
    # Replace style block with link
    html = html.replace(css_match.group(0), '<link rel="stylesheet" href="game.css" />')

# Extract JS
js_match = re.search(r'<script>\s*(.*?)\s*</script>', html, re.DOTALL)
if js_match:
    js_content = js_match.group(1)
    with open("game.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    # Replace script block with src
    html = html.replace(js_match.group(0), '<script src="game.js"></script>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Split completed successfully.")
