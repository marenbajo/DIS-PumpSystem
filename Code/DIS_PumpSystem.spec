# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_all

# SPECPATH = absoluter Pfad zum Code/-Ordner (PyInstaller-Variable)
APP_DIR  = os.path.join(SPECPATH, 'app')
COMP_DIR = os.path.join(SPECPATH, 'components')
DATA_DIR = os.path.join(SPECPATH, 'data')

# customtkinter komplett einsammeln
ctk_datas, ctk_binaries, ctk_hiddenimports = collect_all('customtkinter')

a = Analysis(
    ['run.py'],
    # Alle Unterordner in den Analysepfad – PyInstaller findet alle Module flach
    pathex=[SPECPATH, APP_DIR, COMP_DIR, DATA_DIR],
    binaries=ctk_binaries,
    datas=[
        ('data/dis_logo.jpg', 'data'),
        ('data/icon.png',     'data'),
        ('data/icon.ico',     'data'),
    ] + ctk_datas,
    hiddenimports=ctk_hiddenimports + [
        # app/
        'config', 'layout', 'icon_choice', 'theme', 'main', 'paths',
        # components/
        'segmented_button', 'customer_info_frame', 'step_reco_tab',
        'step_frame', 'reco_frame', 'timer_frame', 'buttons_frame',
        'logo_frame', 'notes_frame', 'testnumber_frame',
        # data/
        'save_file', 'pdf_exporter',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='DIS_PumpSystem',
    debug=False,
    console=False,
    icon='data/icon.ico',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='DIS_PumpSystem',
)
