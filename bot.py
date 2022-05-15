from environs import Env
from googlesearch import search
import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Environment Variables
env = Env()  # new
env.read_env()  # read .env file, if it exists

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = env.str("TOKEN")


def start(update, context):
    update.message.reply_text(
        'Please enter a text and an image that you want to check!')


def help(update, context):
    text = "The purpose of this bot is to check the truthness of the combination of a text and an image from social media, thus it takes a text and an image as inputs, then it passes this inputs to our fact checking model. The output of this bot is a percentage that indicates the possibility that this corresponding news is fake."
    update.message.reply_text(text)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def print_website_names(update, context):
    query = update.message.text
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        update.message.reply_text(j)


def downloadImageDoc(update, context):
    try:
        downloaded_path = ""
        file_id = update.message.document.file_id
        file_unique_id = update.message.document.file_unique_id

        new_file = context.bot.get_file(file_id)
        saving_path = os.path.join(
            downloaded_path, "{}.jpg".format(file_unique_id))
        new_file.download(saving_path)

        context.bot.send_photo(update.message.chat.id, open(
            saving_path, 'rb'), 'This is your image')

        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Thanks for image")
    except:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="error")


def downloadImagePhoto(update, context):
    try:
        downloaded_path = ""
        file_id = update.message.photo[-1].file_id
        file_unique_id = update.message.photo[-1].file_unique_id

        new_file = context.bot.get_file(file_id)
        saving_path = os.path.join(
            downloaded_path, "{}.jpg".format(file_unique_id))
        new_file.download(saving_path)

        context.bot.send_photo(update.message.chat.id, open(
            saving_path, 'rb'), 'This is your image')

        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Thanks for image")
    except:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="error")


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, print_website_names))
    # dp.add_handler(MessageHandler((~Filters.text) & (~Filters.command), downloadImage))
    dp.add_handler(MessageHandler(Filters.document, downloadImageDoc))
    dp.add_handler(MessageHandler(Filters.photo, downloadImagePhoto))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
