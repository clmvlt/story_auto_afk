# FiveM Auto Macro

Script d'automatisation pour FiveM développé par **DIMZOU**

[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@dimzou)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/clmvlt/)

## 📋 Prérequis

- Python 3.8 ou supérieur
- Windows OS

## 🚀 Installation

### Option 1 : Exécution avec Python

1. **Cloner le repository**
```bash
git clone https://github.com/clmvlt/fivem-auto-macro.git
cd fivem-auto-macro
```

2. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

3. **Lancer le script**
```bash
python fivem_auto.py
```

### Option 2 : Utiliser l'exécutable

1. **Build l'exécutable**
```bash
python build_simple.py
```

2. **Lancer l'application**
```bash
cd dist
fivem_auto.exe
```

## 🎮 Utilisation

Le script se lance et affiche :
- Un écran de bienvenue avec ASCII art
- Compte à rebours de 5 secondes
- Recherche automatique de la fenêtre FiveM
- Exécution automatique des macros configurées

## 📝 Logs

Les logs sont sauvegardés dans `fivem_auto.log`

## ⚙️ Configuration

Le script recherche automatiquement une fenêtre contenant "storylife" et "fivem" dans le titre.

## 📄 License

© 2025 DIMZOU - Tous droits réservés

## 👤 Auteur

**DIMZOU**
- YouTube : [@dimzou](https://www.youtube.com/@dimzou)
- GitHub : [@clmvlt](https://github.com/clmvlt/)
