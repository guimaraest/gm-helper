import os
import subprocess
from app.context import get_project_root, MARKER, GLOBAL_TEMPLATES_DIR


def init_project():
    root = get_project_root()
    if root:
        print(f" [!] Already a GM project: {root}")
        return

    cwd = os.getcwd()
    open(os.path.join(cwd, MARKER), 'w').close()
    os.makedirs(os.path.join(cwd, "directives"), exist_ok=True)
    os.makedirs(GLOBAL_TEMPLATES_DIR, exist_ok=True)

    print(f" [OK] Initialized GM project in {cwd}")
    print(f" [OK] Global templates dir: {GLOBAL_TEMPLATES_DIR}")

    try:
        subprocess.Popen(["code", cwd])
        print(f" [OK] Opened in VS Code.")
    except FileNotFoundError:
        print(" [!] VS Code CLI ('code') not found. Open the folder manually.")