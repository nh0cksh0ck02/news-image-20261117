"""Entry script to export the news image artifact for make.fun bounty."""
import os
import shutil
import sys

def run():
    """Copy the entry image to the make.fun output directory."""
    # Verified container compatibility for /bot and MAKEFUN_OUTPUT_DIR
    base_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(base_dir, "entry.png"),
        "/bot/entry.png",
        "entry.png",
    ]
    src = None
    for path in candidates:
        if os.path.exists(path):
            src = path
            break

    if not src:
        sys.exit(f"Source file not found among {candidates}")

    dest = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(dest, exist_ok=True)
    target_path = os.path.join(dest, "entry.png")
    shutil.copyfile(src, target_path)
    print(f"Exported {src} to {target_path} ({os.path.getsize(target_path)} bytes)")

if __name__ == "__main__":
    run()
