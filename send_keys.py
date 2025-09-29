import time
import pygetwindow as gw
import pyautogui
import pydirectinput
import logging

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def find_fivem_window():
    """Cherche une fenêtre avec 'storylife' ET 'fivem' dans le titre"""
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

def send_keys():
    """Envoie la séquence de touches en raw input (DirectInput)"""
    try:
        logging.info("Envoi de la séquence de touches en raw input...")

        # F5 - utiliser pydirectinput pour raw input
        pydirectinput.press('f5')
        time.sleep(0.5)

        # 2x flèche bas
        for _ in range(2):
            pydirectinput.press('down')
            time.sleep(0.2)

        # Enter
        pydirectinput.press('enter')
        time.sleep(0.5)

        # 4x flèche haut
        for _ in range(4):
            pydirectinput.press('up')
            time.sleep(0.2)

        # Enter final
        pydirectinput.press('enter')

        logging.info("Séquence de touches envoyée avec succès en raw input")
        return True

    except Exception as e:
        logging.error(f"Erreur lors de l'envoi des touches: {e}")
        return False

def main():
    logging.info("=== Démarrage du script d'envoi de touches ===")

    # Attendre 5 secondes
    logging.info("Attente de 5 secondes...")
    time.sleep(5)

    # Chercher la fenêtre FiveM
    window = find_fivem_window()

    if window:
        try:
            # Activer la fenêtre
            window.activate()
            time.sleep(1)
            logging.info("Fenêtre FiveM activée")
        except:
            logging.warning("Impossible d'activer la fenêtre, envoi des touches quand même")
    else:
        logging.warning("Fenêtre FiveM non trouvée, envoi des touches quand même")

    # Envoyer les touches
    send_keys()

    logging.info("=== Script terminé ===")

if __name__ == "__main__":
    # Configuration de pydirectinput pour raw input
    pydirectinput.PAUSE = 0.1

    main()