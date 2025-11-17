import platform
import tkinter as tk

def set_app_icon(app, ico_path="data/icon.ico", png_path="data/icon.png"):
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
