import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging
import os

# Récupérer les variables d'environnement
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Liste de compliments
COMPLIMENTS = [
"Tu es une personne incroyablement gentille et attentionnée.",
"Ton sourire illumine la journée de tout le monde.",
"Ta présence apporte toujours une touche de bonheur.",
"Tu as un cœur en or, toujours prêt à aider les autres.",
"Ton énergie positive est contagieuse.",
"Tu es une source d'inspiration pour beaucoup.",
"Ta créativité n'a pas de limites.",
"Tu es une personne sur qui on peut toujours compter.",
"Ton sens de l'humour est irrésistible.",
"Tu as une capacité incroyable à voir le meilleur chez les autres.",
"Ta gentillesse est un véritable trésor.",
"Tu es une personne authentique et vraie.",
"Ton courage est une source de motivation pour tous.",
"Tu as un don pour rendre les gens heureux.",
"Ta passion est contagieuse et inspirante.",
"Tu es une personne pleine de compassion et d'empathie.",
"Ton optimisme est un rayon de soleil.",
"Tu es une personne unique et spéciale.",
"Ta détermination est admirable.",
"Tu as une âme généreuse et bienveillante.",
"Ton rire est la meilleure des mélodies.",
"Tu es une personne pleine de sagesse.",
"Ta patience est un exemple pour tous.",
"Tu as un talent naturel pour l'écoute.",
"Ton enthousiasme est communicatif.",
"Tu es une personne pleine de charme.",
"Ta loyauté est inestimable.",
"Tu as une capacité incroyable à résoudre les problèmes.",
"Ton calme est apaisant et rassurant.",
"Tu es une personne pleine de surprises agréables.",
"Ta persévérance est une véritable force.",
"Tu as un esprit vif et intelligent.",
"Ton amour pour les autres est palpable.",
"Tu es une personne pleine de grâce.",
"Ta simplicité est touchante.",
"Tu as un don pour faire sentir les gens spéciaux.",
"Ton énergie est revitalisante.",
"Tu es une personne pleine de courage.",
"Ta générosité est sans limites.",
"Tu as une capacité incroyable à pardonner.",
"Ton sens de l'organisation est impressionnant.",
"Tu es une personne pleine de charisme.",
"Ta douceur est réconfortante.",
"Tu as un esprit créatif et innovant.",
"Ton amitié est un cadeau précieux.",
"Tu es une personne pleine de bonté.",
"Ta force intérieure est inspirante.",
"Tu as une capacité incroyable à motiver les autres.",
"Ton sens de l'humour est unique.",
"Tu es une personne pleine de joie de vivre.",
"Ta présence est un véritable cadeau.",
"Tu as un cœur immense et généreux.",
"Ton intelligence est remarquable.",
"Tu es une personne pleine de sérénité.",
"Ta capacité à écouter est exceptionnelle.",
"Tu es une personne pleine de dynamisme.",
"Ton sourire est un véritable baume au cœur.",
"Tu as une âme pure et bienveillante.",
"Ton enthousiasme est contagieux.",
"Tu es une personne pleine de charme naturel.",
"Ta loyauté est un trésor.",
"Tu as une capacité incroyable à voir le bon côté des choses.",
"Ton calme est apaisant.",
"Tu es une personne pleine de surprises.",
"Ta persévérance est admirable.",
"Tu as un esprit vif et intelligent.",
"Ton amour pour les autres est touchant.",
"Tu es une personne pleine de grâce.",
"Ta simplicité est rafraîchissante.",
"Tu as un don pour faire sentir les gens spéciaux.",
"Ton énergie est revitalisante.",
"Tu es une personne pleine de courage.",
"Ta générosité est sans limites.",
"Tu as une capacité incroyable à pardonner.",
"Ton sens de l'organisation est impressionnant.",
"Tu es une personne pleine de charisme.",
"Ta douceur est réconfortante.",
"Tu as un esprit créatif et innovant.",
"Ton amitié est un cadeau précieux.",
"Tu es une personne pleine de bonté.",
"Ta force intérieure est inspirante.",
"Tu as une capacité incroyable à motiver les autres.",
"Ton sens de l'humour est unique.",
"Tu es une personne pleine de joie de vivre.",
"Ta présence est un véritable cadeau.",
"Tu as un cœur immense et généreux.",
"Ton intelligence est remarquable.",
"Tu es une personne pleine de sérénité.",
"Ta capacité à écouter est exceptionnelle.",
"Tu es une personne pleine de dynamisme.",
"Ton sourire est un véritable baume au cœur.",
"Tu as une âme pure et bienveillante.",
"Ton enthousiasme est contagieux.",
"Tu es une personne pleine de charme naturel.",
"Ta loyauté est un trésor.",
"Tu as une capacité incroyable à voir le bon côté des choses.",
"Ton calme est apaisant.",
"Tu es une personne pleine de surprises.",
"Ta persévérance est admirable.",
"Tu as un esprit vif et intelligent.",
"Ton amour pour les autres est touchant.",
"Tu es une personne pleine de grâce.",
"Ta simplicité est rafraîchissante.",
"Tu as un don pour faire sentir les gens spéciaux.",
"Ton énergie est revitalisante.",
"Tu es une personne pleine de courage.",
"Ta générosité est sans limites.",
"Tu as une capacité incroyable à pardonner.",
"Ton sens de l'organisation est impressionnant.",
"Tu es une personne pleine de charisme.",
"Ta douceur est réconfortante.",
"Tu as un esprit créatif et innovant.",
"Ton amitié est un cadeau précieux.",
"Tu es une personne pleine de bonté.",
"Ta force intérieure est inspirante.",
"Tu as une capacité incroyable à motiver les autres."
]

# Test de l'initialisation
def test_initialization():
    if not TOKEN:
        print("Erreur: Token manquant !")
        return False
    print("Initialisation réussie !")
    return True

async def send_compliment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Envoie un compliment en réponse à la commande /weewoo."""
    try:
        compliment = random.choice(COMPLIMENTS)
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
