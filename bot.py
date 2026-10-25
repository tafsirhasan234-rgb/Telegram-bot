import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import google.generativeai as genai

GEMINI_API_KEY = os.getenv("AQ.Ab8RN6KwXAwvlwVrZtOdcEd6HqzfQmAeUKGEQFPtEiflmguVug")
TELEGRAM_BOT_TOKEN = os.getenv("8902940908:AAEpMBYi0gdOMiBAD1v-qfuGVuqeKdVkIvM")

genai.configure(api_key=AQ.Ab8RN6KwXAwvlwVrZtOdcEd6HqzfQmAeUKGEQFPtEiflmguVug)
model = genai.GenerativeModel('gemini-1.5-flash')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    chat_id = update.message.chat_id
    
    try:
        response = model.generate_content(user_message)
        await context.bot.send_message(chat_id=chat_id, text=response.text)
    except Exception as e:
        await context.bot.send_message(chat_id=chat_id, text=f"Error: {e}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(8902940908:AAEpMBYi0gdOMiBAD1v-qfuGVuqeKdVkIvM).build()
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
    application.add_handler(message_handler)

    print("Telegram AI Agent is running on Cloud...")
    application.run_polling()
EOF
  
