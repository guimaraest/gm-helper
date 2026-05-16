import os

MARKER = ".gmcli"
GLOBAL_TEMPLATES_DIR = os.path.join(os.path.expanduser("~"), ".gmcli", "templates")


def get_project_root() -> str | None:
    current = os.getcwd()
    while True:
        if os.path.exists(os.path.join(current, MARKER)):
            return current
        parent = os.path.dirname(current)
        if parent == current:
            return None
        current = parent


def get_directives_dir() -> str | None:
    root = get_project_root()
    return os.path.join(root, "directives") if root else None


def get_templates_dir() -> str:
    return GLOBAL_TEMPLATES_DIR