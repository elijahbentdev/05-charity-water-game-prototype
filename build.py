import re

with open("DROP_BY_DROP_PRD.md", "r", encoding="utf-8") as f:
    text = f.read()

# Extract Section 5 HTML
html_match = re.search(r'## 5\. FULL HTML STRUCTURE\n\n.*?```html\n(.*?)\n```', text, re.DOTALL)
html_code = html_match.group(1)

# Extract Section 6 CSS
css_match = re.search(r'## 6\. FULL CSS SPECIFICATION\n\n.*?```css\n(.*?)\n```', text, re.DOTALL)
css_code = css_match.group(1)

# Extract Section 7 JS
js_match = re.search(r'## 7\. FULL JAVASCRIPT GAME LOGIC\n\n.*?```javascript\n(.*?)\n```', text, re.DOTALL)
js_code = js_match.group(1)

# Replace the placeholders
html_code = html_code.replace("/* === ALL CSS GOES HERE (see Section 6) === */", css_code)
html_code = html_code.replace("/* === ALL JAVASCRIPT GOES HERE (see Section 7) === */", js_code)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("Generated index.html successfully.")
