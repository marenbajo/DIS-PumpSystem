# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_all

# SPECPATH ist eine PyInstaller-Variable: absoluter Pfad zum Ordner dieser Spec-Datei (= Code/)
CODE_DIR = SPECPATH

# customtkinter komplett einsammeln (Themes, Assets, Submodule)
ctk_datas, ctk_binaries, ctk_hiddenimports = collect_all('customtkinter')

a = Analysis(
    ['run.py'],
    pathex=[CODE_DIR],
    binaries=ctk_binaries,
    datas=[
        ('data/dis_logo.jpg', 'data'),
        ('data/icon.png',     'data'),
        ('data/icon.ico',     'data'),
    ] + ctk_datas,
    hiddenimports=ctk_hiddenimports + [
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
