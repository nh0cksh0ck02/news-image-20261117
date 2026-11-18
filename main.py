import logging
import os
import shutil
import sys
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("news-image-exporter")

def main():
    target_filename = "entry.png"
    candidates = [
        os.path.dirname(os.path.abspath(__file__)),
        "/bot",
        os.getcwd(),
    ]

    logger.info("Scanning candidate directories for %s...", target_filename)
    src = None
    for cand in candidates:
        candidate_path = os.path.join(cand, target_filename)
        logger.debug("Checking path: %s", candidate_path)
        if os.path.isfile(candidate_path):
            src = candidate_path
            logger.info("Located source file at %s", src)
            break

    if not src:
        logger.error("Could not locate %s in candidate directories: %s", target_filename, candidates)
        sys.exit(1)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        logger.error("Failed to create output directory %s: %s", out_dir, exc)
        sys.exit(1)

    dst = os.path.join(out_dir, target_filename)

    try:
        file_size = os.path.getsize(src)
        if file_size == 0:
            logger.warning("Source file %s is empty (0 bytes).", src)
        shutil.copy2(src, dst)
    except (IOError, shutil.Error) as err:
        logger.error("Failed to copy file from %s to %s: %s", src, dst, err)
        sys.exit(1)

    logger.info("Successfully copied %s (%d bytes) to %s", src, file_size, dst)
    print(f"Export successful: {src} -> {dst}")

if __name__ == "__main__":
    main()
