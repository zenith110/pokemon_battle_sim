# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['launcher.py'],
             pathex=['C:\\Users\\Abrahan\\Downloads\\pokemon_battle_sim'],
             binaries=[],
             datas=[("C:/Users/Abrahan/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/pygame", "."), ("C:/Users/Abrahan/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/require", ".")],
             hiddenimports=["require"],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='launcher',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
