import os
import sys
import platform
import tkinter as tk
from paths import get_data_dir

def set_app_icon(app, ico_name="icon.ico", png_name="icon.png"):
    """Setzt das App-Icon – funktioniert im Dev-Modus, PyInstaller und Nuitka."""
    base_dir = get_data_dir()

    ico_path = os.path.join(base_dir, ico_name)
    png_path = os.path.join(base_dir, png_name)

    system = platform.system()
    if system == "Windows":
        try:
            app.iconbitmap(ico_path)
        except Exception as e:
            print(f"Failed to set .ico icon: {e}")
    else:
        try:
            icon = tk.PhotoImage(file=png_path)
            app.wm_iconphoto(True, icon)
        except Exception as e:
            print(f"Failed to set .png icon: {e}")
