import os


def _output_path(path: str) -> str:
    """Return a filesystem path rooted inside the `output/` folder."""
    # Allow callers to pass 'output/...' or '...'; normalize to single 'output/<rest>'
    if path.startswith("output/") or path.startswith("output\\"):
        path = path.split("/", 1)[1] if "/" in path else path
    return os.path.join("output", path)


def create_folder(name: str):
    """Create a folder inside `output/`.

    If the caller passes a nested path like `website/assets` this will create
    `output/website/assets`.
    """
    out = _output_path(name)
    os.makedirs(out, exist_ok=True)
    return f"Folder '{out}' created"


def write_file(filename: str, content: str):
    """Write a file under `output/`, creating parent directories as needed."""
    out_path = _output_path(filename)
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    return f"File '{out_path}' written successfully"