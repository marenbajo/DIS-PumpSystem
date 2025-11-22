import os
import platform
import tkinter as tk

def set_app_icon(app, ico_name="icon.ico", png_name="icon.png"):
    """
    Set the application icon using paths relative to the project root.
    Works regardless of the current working directory.
    """

    # __file__ is inside app/, so go up one level to project root
    base_dir = os.path.dirname(os.path.dirname(__file__))
    ico_path = os.path.join(base_dir, "data", ico_name)
    png_path = os.path.join(base_dir, "data", png_name)

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
