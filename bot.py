import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters
import requests
import logging
import os

# Récupérer les variables d'environnement
TOKEN = os.getenv("TOKEN")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
CHAT_ID = os.getenv("CHAT_ID", "-1001267100130")

# Test de l'initialisation
def test_initialization():
    if not TOKEN or not MISTRAL_API_KEY:
        print("Erreur: Token ou clé API manquants !")
        return False
    print("Initialisation réussie !")
    return True

async def generate_compliment():
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

async def send_compliment(update: Update, context: CallbackContext):
    """Envoie un compliment en réponse à la commande /weewoo."""
    try:
        compliment = await generate_compliment()
        message = f"🚨🚓🚨WEE WOO !!! POLICE DU SELF-LOVE !!\n{compliment}"
        await update.message.reply_text(message)
    except Exception as e:
        logging.error(f"Erreur lors de l'envoi du compliment : {e}")

async def handle_message(update: Update, context: CallbackContext):
    """Envoie un compliment tous les 500 messages."""
    if 'message_count' not in context.bot_data:
        context.bot_data['message_count'] = 0

    context.bot_data['message_count'] += 1

    if context.bot_data['message_count'] % 500 == 0:
        try:
            compliment = await generate_compliment()
            message = f"🚨🚨POLICE DU SELF-LOVE ! INTERVENTION SURPRISE !\n{compliment}"
            await update.message.reply_text(message)
        except Exception as e:
            logging.error(f"Erreur lors de l'envoi du compliment : {e}")

async def main():
    """Démarre le bot Telegram."""
    application = Application.builder().token(TOKEN).build()

    # Ajouter la gestion des messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Ajouter la gestion de la commande /weewoo
    application.add_handler(CommandHandler("weewoo", send_compliment))

    # Lancer l'application
    await application.run_polling()

if __name__ == "__main__":
    if test_initialization():
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        logger = logging.getLogger(__name__)

        # Obtenir la boucle d'événements actuelle ou en créer une nouvelle
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(main())
        except RuntimeError as e:
            if "This event loop is already running" in str(e):
                import nest_asyncio
                nest_asyncio.apply()
                loop.run_until_complete(main())
            else:
                raise e
