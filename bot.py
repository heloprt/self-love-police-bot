import threading
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, Updater
import requests
import logging
import os

# Récupérer les variables d'environnement
TOKEN = os.getenv("TOKEN")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# Test de l'initialisation
def test_initialization():
    if not TOKEN or not MISTRAL_API_KEY:
        print("Erreur: Token ou clé API manquants !")
        return False
    print("Initialisation réussie !")
    return True

def generate_compliment():
    """Génère un compliment avec l'IA Mistral."""
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistral-7b",
        "prompt": "Génère un compliment sincère, chaleureux et mignon, non genré, pour une personne.",
        "max_tokens": 60
    }
    response = requests.post("https://api.mistral.ai/v1/completions", json=data, headers=headers)
    response.raise_for_status()  # Vérifie les erreurs HTTP
    return response.json()["choices"][0]["text"].strip()

def send_compliment(update: Update, context: CallbackContext):
    """Envoie un compliment en réponse à la commande /weewoo."""
    try:
        compliment = generate_compliment()
        message = f"🚨🚓🚨WEE WOO !!! POLICE DU SELF-LOVE !!\n{compliment}"
        update.message.reply_text(message)
    except Exception as e:
        logging.error(f"Erreur lors de l'envoi du compliment : {e}")

def main():
    """Démarre le bot Telegram."""
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Ajouter la gestion de la commande /weewoo
    dispatcher.add_handler(CommandHandler("weewoo", send_compliment))

    # Démarrer le polling dans un thread séparé
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    if test_initialization():
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        logger = logging.getLogger(__name__)

        # Démarrer le bot dans un thread séparé
        bot_thread = threading.Thread(target=main)
        bot_thread.start()
