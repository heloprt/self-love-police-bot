import asyncio
import os
import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Configuration des logs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# 🔑 Récupération des variables d'environnement (corrigé)
TOKEN = os.getenv("TOKEN")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# 🔍 Vérification des tokens
if not TOKEN or not MISTRAL_API_KEY:
    raise ValueError("❌ Erreur: Token ou clé API Mistral manquants ! Vérifiez vos variables d'environnement.")

async def generate_compliment():
    """Génère un compliment avec l'IA Mistral."""
    url = "https://api.mistral.ai/v1/completions"
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistral-7b",
        "prompt": "Génère un compliment sincère, chaleureux et mignon, non genré, pour une personne.",
        "max_tokens": 60
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Vérifie les erreurs HTTP
        return response.json()["choices"][0]["text"].strip()
    except requests.exceptions.RequestException as e:
        logger.error(f"❌ Erreur API Mistral: {e}")
        return "Erreur lors de la génération du compliment. 😢"

async def send_compliment(update: Update, context: CallbackContext):
    """Envoie un compliment en réponse à la commande /weewoo."""
    compliment = await generate_compliment()
    message = f"🚨🚓🚨WEE WOO !!! POLICE DU SELF-LOVE !!\n{compliment}"
    await update.message.reply_text(message)

async def start(update: Update, context: CallbackContext):
    """Répond à la commande /start."""
    await update.message.reply_text("👋 Hello ! Tape /weewoo pour recevoir un compliment !")

async def main():
    """Démarre le bot Telegram."""
    application = Application.builder().token(TOKEN).build()

    # Ajout des commandes
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("weewoo", send_compliment))

    # Lancer le bot
    await application.run_polling()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if "This event loop is already running" in str(e):
            import nest_asyncio
            nest_asyncio.apply()
            asyncio.run(main())
        else:
            raise e
