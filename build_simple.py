import PyInstaller.__main__
import os
import shutil

script_name = "fivem_auto.py"
output_name = "StoryLife auto afk"

PyInstaller.__main__.run([
    script_name,
    '--onefile',
    '--noconsole',
    '--name', output_name,
    '--icon=NONE',
    '--uac-admin',
    '--manifest=fivem_auto.exe.manifest',
    '--add-data', 'fivem_auto.exe.manifest;.',
    '--distpath', './dist',
    '--workpath', './build',
    '--specpath', './',
    '--clean',
])

print(f"\nBuild terminé! L'exécutable se trouve dans: dist/{output_name}.exe")