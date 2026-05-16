import os
from app.context import get_directives_dir


def _resolve_path(file_name: str) -> str | None:
    directives_dir = get_directives_dir()
    if not directives_dir:
        print(" [X] No GM project found. Run 'gm init' first.")
        return None
    path = file_name if os.path.exists(file_name) else os.path.join(directives_dir, file_name)
    if not path.endswith(".md"):
        path += ".md"
    return path if os.path.exists(path) else None


def build_directive(file_name: str) -> str | None:
    path = _resolve_path(file_name)

    if not path:
        print(f" [X] File '{file_name}' not found.")
        return None

    with open(path, 'r', encoding='utf-8') as f:
        body = f.read()

    separator = "=" * 30
    print(f"\n{separator}\n PREVIEW: {os.path.basename(path)}\n{separator}")
    print(body)
    print(f"{separator}\n")

    return body