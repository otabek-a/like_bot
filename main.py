from telegram.ext import Updater,MessageHandler,Filters,CommandHandler,CallbackContext,Filters
from telegram import Bot, Update,InlineKeyboardButton,InlineKeyboardMarkup
import os





def info(update: Update, context):
    photo=update.message.photo[-1]
    file_id=photo.file_id
    inline_button = InlineKeyboardButton(text="👍",callback_data=1)
    inline_button1 = InlineKeyboardButton(text="👎",callback_data=1)
    inline_keyboard = InlineKeyboardMarkup([[inline_button,inline_button1]])
    update.message.reply_photo(photo=file_id,caption='do you like/dislike ?',reply_markup=inline_keyboard)

def start(update: Update, context):
    update.message.reply_text("Hey please send photo for work this bot")

TOKEN = os.environ['TOKEN']

updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher

# add handlers here



dispatcher.add_handler(MessageHandler(Filters.photo, info))

dispatcher.add_handler(CommandHandler('start',start))

updater.start_polling()
updater.idle()