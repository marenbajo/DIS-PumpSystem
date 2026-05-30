import sys
import os

# Make Code/ and Code/app/ available for all imports
_code_dir = os.path.dirname(os.path.abspath(__file__))
_app_dir  = os.path.join(_code_dir, "app")

for _p in (_app_dir, _code_dir):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from app.main import App

if __name__ == "__main__":
    app = App()
    app.mainloop()
