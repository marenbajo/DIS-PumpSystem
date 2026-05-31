import sys
import os

# Absoluter Pfad zum Code/-Ordner (dort liegt diese Datei)
_here = os.path.dirname(os.path.abspath(__file__))

# Alle Unterordner in sys.path legen, damit flache Imports funktionieren
# (sowohl in Entwicklung als auch im PyInstaller-Bundle)
for _subdir in ('', 'app', 'components', 'data'):
    _p = os.path.join(_here, _subdir)
    if _p not in sys.path:
        sys.path.insert(0, _p)

from main import App

if __name__ == '__main__':
    app = App()
    app.mainloop()
