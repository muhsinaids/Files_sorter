from pathlib import Path

HOME = Path.home()
WATCH_DIRS = [HOME / "Desktop", HOME / "Documents", HOME / "Downloads"]

EXTENSION_MAP = {
    ".jpg": HOME / "Pictures", ".jpeg": HOME / "Pictures", ".png": HOME / "Pictures",
    ".mp3": HOME / "Music", ".wav": HOME / "Music",
    ".mp4": HOME / "Videos", ".mkv": HOME / "Videos",
    ".pdf": HOME / "Documents" / "PDFs",
    ".pptx": HOME / "Documents" / "Slides",
    ".docx": HOME / "Documents" / "Word",
}

def is_safe_to_move(path):
    if path.is_dir():
        return False
    if path.name.startswith("."):
        return False
    if path.suffix.lower() not in EXTENSION_MAP:
        return False
    return True

def run(dry_run=True):
    for folder in WATCH_DIRS:
        if not folder.exists():
            print("MISSING:", folder)
            continue
        print("=====", folder, "=====")
        for item in folder.iterdir():
            if not is_safe_to_move(item):
                continue
            dest_dir = EXTENSION_MAP[item.suffix.lower()]
            if item.parent == dest_dir:
                print("ALREADY HOME:", item.name)
                continue
            print("WOULD MOVE:", item.name, "->", dest_dir)
            if not dry_run:
                pass

if __name__ == "__main__":
    run(dry_run=True)