# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['app.py'],
    pathex=['.'],
    binaries=[],
    datas=[('data', 'data')], # the list of folders that are in-app data and will be copied and included in the dist app
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='non-window-app-tray', # the file name of the dist app
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=['vcruntime140.dll', 'ucrtbase.dll'],
    runtime_tmpdir=None,
    icon='data/app.ico',
    console=False,
    uac_admin=False,
    resources=[],
    version='version.txt',
)
