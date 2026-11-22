import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi! Main Prompt Editing Bot hun ✨\n\n"
        "Koi bhi prompt bhejo, main usko aur accha bana dunga.\n\n"
        "Example:\n"
        "Tum bhejoge: `a girl in garden`\n"
        "Main dunga: `A beautiful girl standing in a lush green garden, golden hour sunlight, ultra realistic, 4k, cinematic...`\n\n"
        "Bas apna prompt bhej do!"
    )

def edit_prompt(text):
    text = text.strip()
    # Simple smart editing
    styles = "ultra detailed, high quality, cinematic lighting, 4k, sharp focus, realistic"
    if len(text) < 100:
        return f"{text}, {styles}, beautiful composition, vibrant colors, professional photography"
    else:
        return f"Enhanced Prompt: {text}, {styles}"

async def handle_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    new_prompt = edit_prompt(user_text)
    await update.message.reply_text(f"✨ **Tumhara Edited Prompt:**\n\n`{new_prompt}`\n\nIse copy karke use kar lo!", parse_mode="Markdown")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_msg))
    print("Bot chal raha hai...")
    app.run_polling()

if __name__ == "__main__":
    main()
