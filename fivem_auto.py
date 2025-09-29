import time
import subprocess
import os
import pygetwindow as gw
import pyautogui
import logging
from datetime import datetime
from send_keys import send_keys
import psutil

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('fivem_auto.log'),
        logging.StreamHandler()
    ]
)

def find_fivem_window():
    try:
        windows = gw.getAllWindows()
        for window in windows:
            if window.title:
                title_lower = window.title.lower()
                if 'storylife' in title_lower and 'fivem' in title_lower:
                    logging.info(f"Fenêtre FiveM trouvée: {window.title}")
                    return window
    except Exception as e:
        logging.error(f"Erreur lors de la recherche de fenêtre: {e}")
    return None

def kill_fivem_processes():
    killed = False
    processes_to_kill = ['FiveM.exe', 'FiveM_b2802_GTAProcess.exe', 'FiveM_GTAProcess.exe', 'FiveM_DumpServer.exe']

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] in processes_to_kill:
                logging.info(f"Arrêt du processus {proc.info['name']} (PID: {proc.info['pid']})")
                proc.kill()
                killed = True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            logging.warning(f"Impossible de tuer le processus: {e}")

    if killed:
        logging.info("Processus FiveM tués, attente de 5 secondes...")
        time.sleep(5)
    return killed

def launch_fivem():
    url = "fivem://connect/cfx.re/join/aaex7k"
    logging.info(f"Lancement de FiveM: {url}")

    try:
        result = subprocess.run(['explorer', url], capture_output=True, text=True)
        logging.info("Commande de lancement envoyée via explorer.exe")

        logging.info("Attente du démarrage de FiveM...")
        time.sleep(60)

        return True

    except Exception as e:
        logging.error(f"Erreur lors du lancement: {e}")
        return False

def send_keys_to_window(window):
    try:
        window.activate()
        time.sleep(1)

        logging.info("Envoi de la séquence de touches via send_keys...")

        result = send_keys()

        if result:
            logging.info("Séquence de touches envoyée avec succès")
        return result

    except Exception as e:
        logging.error(f"Erreur lors de l'envoi des touches: {e}")
        return False

def display_intro():
    ascii_art = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║   ██████╗ ██╗███╗   ███╗███████╗ ██████╗ ██╗   ██╗           ║
    ║   ██╔══██╗██║████╗ ████║╚══███╔╝██╔═══██╗██║   ██║           ║
    ║   ██║  ██║██║██╔████╔██║  ███╔╝ ██║   ██║██║   ██║           ║
    ║   ██║  ██║██║██║╚██╔╝██║ ███╔╝  ██║   ██║██║   ██║           ║
    ║   ██████╔╝██║██║ ╚═╝ ██║███████╗╚██████╔╝╚██████╔╝           ║
    ║   ╚═════╝ ╚═╝╚═╝     ╚═╝╚══════╝ ╚═════╝  ╚═════╝            ║
    ║                                                              ║
    ║              Script développé par DIMZOU                     ║
    ║                  © 2025 - Tous droits réservés               ║
    ║                                                              ║
    ╠══════════════════════════════════════════════════════════════╣
    ║                                                              ║
    ║     📺 YouTube  : https://www.youtube.com/@dimzou           ║
    ║     💻 GitHub   : https://github.com/clmvlt/                ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(ascii_art)

    for i in range(5, 0, -1):
        print(f"\r    Démarrage dans {i}...", end="", flush=True)
        time.sleep(1)
    print("\r    ▶ Script démarré!        \n")

def main():
    display_intro()
    logging.info("=== Démarrage du script FiveM Auto ===")

    already_processed = False
    last_launch_time = None

    initial_window = find_fivem_window()
    if initial_window:
        logging.info("FiveM est déjà lancé au démarrage du script")
        logging.info("Attente de 3 secondes avant d'envoyer les touches...")
        time.sleep(3)

        if send_keys_to_window(initial_window):
            already_processed = True
            logging.info("Traitement initial terminé")

    while True:
        try:
            fivem_window = find_fivem_window()

            if fivem_window:
                if last_launch_time and not already_processed:
                    elapsed = time.time() - last_launch_time
                    wait_time = 180 - elapsed

                    if wait_time > 0:
                        logging.info(f"Attente de {wait_time:.0f} secondes avant d'envoyer les touches...")
                        time.sleep(wait_time)

                    if send_keys_to_window(fivem_window):
                        already_processed = True
                        logging.info("Traitement terminé pour cette session")

            else:
                if not already_processed:
                    logging.info("Fenêtre FiveM avec 'storylife' et 'fivem' non trouvée")
                    logging.info("Tentative de lancement de FiveM...")

                    if launch_fivem():
                        last_launch_time = time.time()
                        logging.info("Commande de lancement exécutée, attente de la fenêtre FiveM...")
                        logging.info("Le jeu devrait se lancer dans quelques secondes")
                        logging.info("Attente de 3 minutes après détection de la fenêtre avant d'envoyer les touches")
                    else:
                        logging.error("Impossible d'exécuter la commande de lancement")
                        time.sleep(10)
                else:
                    logging.info("Fenêtre fermée après traitement, reset du cycle")
                    logging.info("Forçage de l'arrêt des processus FiveM...")
                    kill_fivem_processes()
                    logging.info("Attente de 60 secondes avant de relancer FiveM...")
                    time.sleep(60)
                    already_processed = False
                    last_launch_time = None

            time.sleep(5)

        except KeyboardInterrupt:
            logging.info("Arrêt demandé par l'utilisateur")
            break
        except Exception as e:
            logging.error(f"Erreur dans la boucle principale: {e}")
            time.sleep(10)

    logging.info("=== Arrêt du script ===")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.1

    main()