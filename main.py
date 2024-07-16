from telegram import *
from telegram.ext import *
import json
import google.generativeai as genai
from typing import Final
from prompt import *

TOKEN: Final = " YOUR TELEGRAM BOT'S TOKEN"
BOT_USERNAME: Final = 'BOT_USERNAME'

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is an AI bot, ask anything')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is an AI bot, ask anything')


# Responses
def handle_response(text: str) -> str:
    pr: str = text.lower()
    return(ai(pr))
    
# Messgae Handling
async def handle_message(update: Update, Context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text


    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)

        else: 
            return
            
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, Context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused the following error {Context.error}')


if __name__ == '__main__':
    print('Starting Bot...')
    app = Application.builder().token(TOKEN).build()

    #commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #errors
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)
