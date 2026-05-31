import os
import sys
import platform
import tkinter as tk

def set_app_icon(app, ico_name="icon.ico", png_name="icon.png"):
    """Setzt das App-Icon – funktioniert im Dev-Modus und im PyInstaller-Bundle."""

    if getattr(sys, "frozen", False):
        # PyInstaller-Exe: Icons liegen in sys._MEIPASS/data/
        base_dir = os.path.join(sys._MEIPASS, "data")
    else:
        # Entwicklung: Icons liegen in Code/data/
        # __file__ = Code/app/icon_choice.py → eine Ebene hoch = Code/
        base_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")

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
