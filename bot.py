import requests
import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Récupérer les variables d'environnement
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Test de l'initialisation
def test_initialization():
    if not TOKEN or not HUGGINGFACE_API_KEY:
        print("Erreur: Token ou clé API manquants !")
        return False
    print("Initialisation réussie !")
    return True

def generate_compliment():
    """Génère un compliment avec l'API Hugging Face."""
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}"
    }
    data = {
        "inputs": "Génère un compliment sincère, chaleureux et mignon, non genré, pour une personne.",
        "parameters": {"max_length": 60}
    }
    logging.info(f"Envoi de la requête à l'API Hugging Face avec les données : {data}")
    response = requests.post("https://api-inference.huggingface.co/models/bigscience/bloom", headers=headers, json=data)
    response.raise_for_status()  # Vérifie les erreurs HTTP
    return response.json()[0]["generated_text"].strip()

async def send_compliment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Envoie un compliment en réponse à la commande /weewoo."""
    try:
        compliment = generate_compliment()
        message = f"🚨🚓🚨WEE WOO !!! POLICE DU SELF-LOVE !!\n{compliment}"
        await update.message.reply_text(message)
    except Exception as e:
        logging.error(f"Erreur lors de l'envoi du compliment : {e}")

def main():
    """Démarre le bot Telegram."""
    application = ApplicationBuilder().token(TOKEN).build()

    # Ajouter la gestion de la commande /weewoo
    application.add_handler(CommandHandler("weewoo", send_compliment))

    # Démarrer le polling
    application.run_polling()

if __name__ == "__main__":
    if test_initialization():
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        logger = logging.getLogger(__name__)

        # Démarrer le bot dans le thread principal
        main()
