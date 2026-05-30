# -*- mode: python ; coding: utf-8 -*-
import os

# Pfad zum Code/-Ordner (dort liegt diese .spec-Datei)
CODE_DIR = os.path.abspath('.')

a = Analysis(
    ['run.py'],
    pathex=[CODE_DIR],          # Code/ ist in sys.path → app/, components/, data/ findbar
    binaries=[],
    datas=[
        ('data/dis_logo.jpg', 'data'),
        ('data/icon.png',     'data'),
        ('data/icon.ico',     'data'),
    ],
    hiddenimports=[
        # app-Paket
        'app.config',
        'app.layout',
        'app.icon_choice',
        'app.theme',
        # components-Paket
        'components.segmented_button',
        'components.customer_info_frame',
        'components.step_reco_tab',
        'components.step_frame',
        'components.reco_frame',
        'components.timer_frame',
        'components.buttons_frame',
        'components.logo_frame',
        'components.notes_frame',
        'components.testnumber_frame',
        # data-Paket
        'data.save_file',
        'data.pdf_exporter',
    ],
    collect_all=['customtkinter'],
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
    console=False,          # kein schwarzes Terminal-Fenster
    icon='data/icon.ico',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='DIS_PumpSystem',
)
