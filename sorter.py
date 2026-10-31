from pathlib import Path
WATCH_DIRS = [ Path.home() / "Desktop", Path.home() / "Documents", Path.home() / "Downloads"]
ALLOWED_SUFFIXES = {".jpeg", ".jpg", ".png", ".pdf", ".pptx", ".docx", ".mp3", ".wav", ".mp4", ".mkv"}

def is_safe_to_move(path):
    if path.is_dir():
        return False
    if path.name.startswith("."):
        return False
    if path.suffix.lower() not in ALLOWED_SUFFIXES:
        return False
    return True

def main():
    for folder in WATCH_DIRS:
        if not folder.exists():
            print("MISSING:", folder)
            continue
        print("=====",folder,"=====")
        for item in folder.iterdir():
            status = "OK" if is_safe_to_move(item) else "SKIP"
            print(status,folder.name,item.name)

if __name__ == "__main__" : 
    main()

