import os
import subprocess

DIRECTIVES_DIR = os.path.join(os.path.dirname(__file__), "..", "directives")

TEMPLATE = """\
# DIRETIVA: {title}

**Classificação:** RESERVADO  
**Data:** {date}  
**Origem:** Gabinete Operacional  

---

## Objetivo


## Execução


## Observações

"""


def new_file(name: str):
    os.makedirs(DIRECTIVES_DIR, exist_ok=True)

    file_name = f"{name}.md" if not name.endswith(".md") else name
    file_path = os.path.join(DIRECTIVES_DIR, file_name)

    if os.path.exists(file_path):
        print(f" [X] '{file_name}' already exists.")
        return

    from datetime import date
    content = TEMPLATE.format(
        title=name.replace("_", " ").upper(),
        date=date.today().isoformat()
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f" [OK] Created: {file_path}")

    try:
        subprocess.Popen(["code", file_path])
        print(f" [OK] Opened in VS Code.")
    except FileNotFoundError:
        print(" [!] VS Code CLI ('code') not found. Open the file manually.")