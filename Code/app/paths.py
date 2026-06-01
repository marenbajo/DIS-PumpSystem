"""
Zentrale Pfad-Hilfsfunktionen.
Funktioniert in Entwicklung (Python), PyInstaller und Nuitka.
"""
import sys
import os


def get_app_base() -> str:
    """Gibt den Basis-Ordner der laufenden App zurück."""
    # PyInstaller setzt _MEIPASS
    if hasattr(sys, '_MEIPASS'):
        return os.path.dirname(sys.executable)
    # Nuitka oder anderer Compiler: argv[0] ist die .exe
    argv0 = os.path.abspath(sys.argv[0])
    if argv0.lower().endswith('.exe'):
        return os.path.dirname(argv0)
    # Entwicklung: run.py liegt in Code/, paths.py in Code/app/
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_data_dir() -> str:
    """Ordner mit Icons und Logo (Code/data/ bzw. neben der .exe)."""
    return os.path.join(get_app_base(), 'data')


def get_data_files_dir() -> str:
    """Ordner für gespeicherte Testdaten."""
    return os.path.join(get_app_base(), 'data_files')
