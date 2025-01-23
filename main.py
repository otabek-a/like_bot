from telegram.ext import Updater,MessageHandler,Filters,CommandHandler,CallbackContext,Filters, CallbackQueryHandler
from telegram import Bot, Update,InlineKeyboardButton,InlineKeyboardMarkup
import os
button_count={'like':0, 'dislike':0}
res={}

def button_callback(update:Update,context):
    query=update.callback_query
    user_id=(query.from_user.id)
    query.answer()
    count=res.get(user_id, None)
    count=res.get(user_id,None)
    if query.data=='like' :
          if count=='dislike':
               button_count['dislike']-=1
          if count != 'like':
               button_count['like']+=1
               res[user_id]='like'
        
          
    elif query.data=='dislike' :
          if count=='like':
               button_count['like']-=1
          if count != 'dislike':
               button_count['dislike']+=1
               res[user_id]='dislike'
         
          
          
         
        
    
    inline_button = InlineKeyboardButton(text=f"👍 {button_count['like']}",callback_data='like')
    inline_button1 = InlineKeyboardButton(text=f"👎 {button_count['dislike']}",callback_data='dislike')
    inline_keyboard = InlineKeyboardMarkup([[inline_button,inline_button1]])


    query.edit_message_reply_markup(reply_markup=inline_keyboard)















def info(update: Update, context):
    photo=update.message.photo[-1]
    file_id=photo.file_id
    inline_button = InlineKeyboardButton(text=f"👍 {button_count['like']}",callback_data='like')
    inline_button1 = InlineKeyboardButton(text=f"👎 {button_count['dislike']}",callback_data='dislike')
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
dispatcher.add_handler(CallbackQueryHandler(button_callback))
updater.start_polling()
updater.idle()