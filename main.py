"""Entrypoint script for news image repository container."""

import os
import shutil
import sys

def run():
    # Container execution verified
    base_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(base_dir, "entry.png"),
        "/bot/entry.png",
        "entry.png",
    ]
    src = None
    for p in candidates:
        if os.path.exists(p):
            src = p
            break
    if not src:
        sys.exit(f"Source file not found among {candidates}")
    dest_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(dest_dir, exist_ok=True)
    target = os.path.join(dest_dir, "entry.png")
    shutil.copyfile(src, target)
    print(f"Exported {src} to {target} ({os.path.getsize(target)} bytes)")

if __name__ == "__main__":
    run()
