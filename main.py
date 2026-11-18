"""Entry script to export the news image artifact for make.fun bounty."""
import os
import shutil

def run():
    """Copy the entry image to the make.fun output directory."""
    src = 'entry.png'
    if not os.path.exists(src):
        raise FileNotFoundError(f"Source file {src} does not exist.")

    dest = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(dest, exist_ok=True)
    target_path = os.path.join(dest, 'entry.png')
    shutil.copyfile(src, target_path)
    print(f"Exported {src} to {target_path}")

if __name__ == '__main__':
    run()
