import subprocess
import sys
import os
import shutil

def check_pyinstaller():
    """Vérifie si PyInstaller est installé"""
    try:
        import PyInstaller
        print("✓ PyInstaller est déjà installé")
        return True
    except ImportError:
        print("PyInstaller n'est pas installé. Installation en cours...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✓ PyInstaller installé avec succès")
        return True

def create_spec_file():
    """Crée un fichier .spec personnalisé pour PyInstaller"""
    spec_content = """# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['fivem_auto.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('send_keys.py', '.')  # Inclure send_keys.py dans le bundle
    ],
    hiddenimports=[
        'pygetwindow',
        'pyautogui',
        'pydirectinput',
        'PIL',
        'numpy',
        'cv2',
        'mouseinfo',
        'pyperclip',
        'pytweening',
        'pymsgbox'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='FiveM_Auto',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Garder la console pour voir les logs
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Vous pouvez ajouter une icône ici si vous voulez
    version_file=None,
    uac_admin=False,  # Mettre à True si vous avez besoin des droits admin
    uac_uiaccess=False,
)
"""

    with open("FiveM_Auto.spec", "w", encoding="utf-8") as f:
        f.write(spec_content)
    print("✓ Fichier .spec créé")

def build_exe():
    """Lance la compilation avec PyInstaller"""
    print("\n📦 Compilation de l'exécutable...")
    print("Cela peut prendre quelques minutes...\n")

    try:
        # Utiliser le fichier .spec personnalisé
        subprocess.check_call([
            sys.executable,
            "-m",
            "PyInstaller",
            "--clean",  # Nettoyer les fichiers temporaires
            "--noconfirm",  # Pas de confirmation pour écraser
            "FiveM_Auto.spec"
        ])
        print("\n✓ Compilation terminée avec succès!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Erreur lors de la compilation: {e}")
        return False

def clean_build_files():
    """Nettoie les fichiers temporaires de build"""
    dirs_to_remove = ["build", "__pycache__"]
    files_to_remove = ["FiveM_Auto.spec"]

    for dir_name in dirs_to_remove:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"✓ Dossier {dir_name} supprimé")

    for file_name in files_to_remove:
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"✓ Fichier {file_name} supprimé")

def main():
    print("=== Build de FiveM Auto ===\n")

    # Vérifier qu'on est dans le bon dossier
    if not os.path.exists("fivem_auto.py"):
        print("✗ Erreur: fivem_auto.py non trouvé!")
        print("Assurez-vous d'exécuter ce script dans le dossier du projet.")
        return

    if not os.path.exists("send_keys.py"):
        print("✗ Erreur: send_keys.py non trouvé!")
        print("Assurez-vous que send_keys.py est dans le même dossier.")
        return

    # Vérifier/installer PyInstaller
    if not check_pyinstaller():
        print("✗ Impossible d'installer PyInstaller")
        return

    # Créer le fichier .spec
    create_spec_file()

    # Compiler l'exécutable
    if build_exe():
        exe_path = os.path.join("dist", "FiveM_Auto.exe")
        if os.path.exists(exe_path):
            size_mb = os.path.getsize(exe_path) / (1024 * 1024)
            print(f"\n✅ Exécutable créé avec succès!")
            print(f"📍 Emplacement: {os.path.abspath(exe_path)}")
            print(f"📊 Taille: {size_mb:.2f} MB")
            print(f"\nL'exécutable peut être lancé sur n'importe quel PC Windows")
            print("même sans Python installé!")
        else:
            print("\n✗ L'exécutable n'a pas été créé")

    # Optionnel: nettoyer les fichiers de build
    response = input("\nVoulez-vous nettoyer les fichiers temporaires de build? (o/n): ")
    if response.lower() == 'o':
        clean_build_files()
        print("✓ Nettoyage terminé")

    print("\n=== Build terminé ===")

if __name__ == "__main__":
    main()