@echo off
echo === Build rapide de FiveM Auto ===
echo.

REM Installer les dépendances si nécessaire
echo Installation des dépendances...
pip install pygetwindow pyautogui pydirectinput pyinstaller

echo.
echo Création de l'exécutable...

REM Build avec PyInstaller en one-file
pyinstaller --onefile --clean --noconfirm ^
    --add-data "send_keys.py;." ^
    --hidden-import pygetwindow ^
    --hidden-import pyautogui ^
    --hidden-import pydirectinput ^
    --hidden-import PIL ^
    --console ^
    --name FiveM_Auto ^
    fivem_auto.py

echo.
if exist "dist\FiveM_Auto.exe" (
    echo Succès! L'exécutable est créé dans: dist\FiveM_Auto.exe
    echo Taille du fichier:
    dir "dist\FiveM_Auto.exe" | findstr FiveM_Auto.exe
) else (
    echo Erreur: L'exécutable n'a pas été créé
)

echo.
pause