import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
updater = Updater("709201082:AAGQ1i3v2Zx6ysLcM6aYSJKFgHvrodP4hr0")

def photo(bot, update):
    file_id = update.message.photo[-1].file_id
    newFile = bot.getFile(file_id)
    newFile.download(file_id+'.jpg')
    print(file_id)
    FN = str(file_id)
    bot.sendMessage(chat_id=update.message.chat_id, text="Working... :) *note:Open file below with a text editor and put your mobile phone at Landscape mode @goodzilam")
    cmd = "python x.py "+FN+".jpg "+FN+".txt"+" > "+FN+"1.txt"
    os.system(cmd)
    #bot.send_document(dispatcher.bot, update, document=open(FN+'1.txt', 'rb'))
    bot.sendDocument(chat_id=update.message.chat_id, document=open(FN+'1.txt', 'rb'))
photo_handler = MessageHandler(Filters.photo, photo)
updater.dispatcher.add_handler(photo_handler)


dispatcher = updater.dispatcher

updater.start_polling()
updater.idle()
