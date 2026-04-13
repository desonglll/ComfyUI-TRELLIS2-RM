# from pathlib import Path
# from comfy_env import setup_env, copy_files

# setup_env()

# SCRIPT_DIR = Path(__file__).resolve().parent
# COMFYUI_DIR = SCRIPT_DIR.parent.parent

# # Copy assets
# copy_files(SCRIPT_DIR / "assets", COMFYUI_DIR / "input")

import shutil
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
COMFYUI_DIR = SCRIPT_DIR.parent.parent

# 原生的文件拷贝逻辑，替换原来的 copy_files
def manual_copy(src, dst):
    if src.exists() and src.is_dir():
        dst.mkdir(parents=True, exist_ok=True)
        for item in src.iterdir():
            target = dst / item.name
            if item.is_dir():
                shutil.copytree(item, target, dirs_exist_ok=True)
            else:
                shutil.copy2(item, target)
        print(f"[Manual Patch] Copied assets from {src} to {dst}")

# 执行拷贝
manual_copy(SCRIPT_DIR / "assets", COMFYUI_DIR / "input")