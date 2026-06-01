import sys
import os
import traceback

# Alle Unterordner in sys.path damit flache Imports funktionieren
_here = os.path.dirname(os.path.abspath(__file__))
for _subdir in ('', 'app', 'components', 'data'):
    _p = os.path.join(_here, _subdir)
    if _p not in sys.path:
        sys.path.insert(0, _p)

try:
    from main import App
    app = App()
    app.mainloop()
except Exception as e:
    # Fehler in eine Log-Datei neben der .exe schreiben
    log_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'error.log')
    with open(log_path, 'w', encoding='utf-8') as f:
        traceback.print_exc(file=f)
    # Auch als Popup anzeigen
    try:
        import tkinter.messagebox as mb
        mb.showerror("DIS PumpSystem – Fehler", str(e))
    except Exception:
        pass
