import os
import subprocess
from datetime import date
from app.context import get_directives_dir, get_templates_dir

DEFAULT_CONTENT = """\
---
subject: {name}
---
"""


def _load_template(template: str) -> str | None:
    path = os.path.join(get_templates_dir(), f"{template}.md")
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def _available_templates() -> list[str]:
    templates_dir = get_templates_dir()
    if not os.path.exists(templates_dir):
        return []
    return [f[:-3] for f in os.listdir(templates_dir) if f.endswith(".md")]


def new_file(name: str, template: str = None):
    directives_dir = get_directives_dir()
    if not directives_dir:
        print(" [X] No GM project found. Run 'gm init' first.")
        return

    os.makedirs(directives_dir, exist_ok=True)

    file_name = f"{name}.md" if not name.endswith(".md") else name
    file_path = os.path.join(directives_dir, file_name)

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