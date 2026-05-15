import os
import subprocess
from datetime import date
 
DIRECTIVES_DIR = os.path.join(os.path.dirname(__file__), "..", "directives")
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "..", "templates")
 
DEFAULT_CONTENT = """\
---
subject: {name}
---
"""
 
 
def _load_template(template: str) -> str | None:
    path = os.path.join(TEMPLATES_DIR, f"{template}.md")
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
 
 
def _available_templates() -> list[str]:
    if not os.path.exists(TEMPLATES_DIR):
        return []
    return [f[:-3] for f in os.listdir(TEMPLATES_DIR) if f.endswith(".md")]
 
 
def new_file(name: str, template: str = None):
    os.makedirs(DIRECTIVES_DIR, exist_ok=True)
 
    file_name = f"{name}.md" if not name.endswith(".md") else name
    file_path = os.path.join(DIRECTIVES_DIR, file_name)
 
    if os.path.exists(file_path):
        print(f" [X] '{file_name}' already exists.")
        return
 
    if template is not None:
        raw = _load_template(template)
        if raw is None:
            available = _available_templates()
            print(f" [X] Unknown template '{template}'. Available: {', '.join(available) or 'none'}")
            return
        content = raw.format(name=name, title=name.replace("_", " ").upper(), date=date.today().isoformat())
    else:
        content = DEFAULT_CONTENT.format(name=name)
 
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
 
    print(f" [OK] Created: {file_path}")
 
    try:
        subprocess.Popen(["code", file_path])
        print(f" [OK] Opened in VS Code.")
    except FileNotFoundError:
        print(" [!] VS Code CLI ('code') not found. Open the file manually.")