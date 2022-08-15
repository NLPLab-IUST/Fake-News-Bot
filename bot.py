from environs import Env
from googlesearch import search
import logging
import os
from telegram.ext import *
from unittest import result
import requests
from telegram import *
import time
import requests, json
import pyimgur
from serpapi import GoogleSearch

# Environment Variables
env = Env()  # new
env.read_env()  # read .env file, if it exists

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = env.str("TOKEN")

stance_target = None
stance_text = None
user_state = {}
stance = "Stance Detection"
text = "Search Text"
image = "Search Image"
button_list = [stance, text, image]
client_id = "9345c5d096864df"
last_message = []

def start(update: Update, context: CallbackContext):
    if len(last_message) != 0:
        context.bot.delete_message(chat_id=update.effective_chat.id, message_id=last_message[0].message_id)
    buttons = [[KeyboardButton(stance)], [KeyboardButton(text)], [KeyboardButton(image)]]
    
    last_message[0] = context.bot.send_message(chat_id=update.effective_chat.id,
                             reply_markup=ReplyKeyboardMarkup(buttons), text="Welcome to my bot!\nTODO: Write something to describe out bot functionality.")


def help(update, context):
    text = "The purpose of this bot is to check the truthness of the combination of a text and an image from social media, thus it takes a text and an image as inputs, then it passes this inputs to our fact checking model. The output of this bot is a percentage that indicates the possibility that this corresponding news is fake."
    update.message.reply_text(text)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def print_website_names(update, context):
    user_id = update.message.chat.id
    query = update.message.text
    for j in search(query, tld="co.in", num=5, stop=5, pause=2):
        update.message.reply_text(j)
    user_state[user_id]["role"] = None

def image_search_google(url):
    params = {
      "engine": "google_reverse_image",
      "image_url": url,
      "api_key": "4d23bf13fb411ce6020adae40bececefd699b8dd60cc7f5960b233664c8643ef"
    }
    print(url)

    search = GoogleSearch(params)
    results = search.get_dict()
    return results['image_results'][:5]

def downloadImageDoc(update, context):
    user_id = update.message.chat.id
    if user_id in user_state:
        if user_state[user_id]["role"] == "image":
            try:
                downloaded_path = ""
                file_id = update.message.document.file_id
                file_unique_id = update.message.document.file_unique_id

                new_file = context.bot.get_file(file_id)
                saving_path = os.path.join(downloaded_path, "{}.jpg".format(file_unique_id))
                new_file.download(saving_path)

                im = pyimgur.Imgur(client_id)
                uploaded_image = im.upload_image(saving_path, title="nothing")

                print("link =", uploaded_image.link)
                result = image_search_google(uploaded_image.link)
                

                for res in result:
                    update.message.reply_text(res["link"])

                user_state[user_id]["role"] = None

                # context.bot.send_photo(update.message.chat.id, open(saving_path, 'rb'), 'This is your image')
                # context.bot.send_message(chat_id=update.effective_chat.id, text="Thanks for image")
            except:
                context.bot.send_message(chat_id=update.effective_chat.id, text="error")
    else:
        update.message.reply_text("please type /start first!")


def downloadImagePhoto(update, context):
    user_id = update.message.chat.id
    if user_id in user_state:
        if user_state[user_id]["role"] == "image":
            try:
                downloaded_path = ""
                file_id = update.message.photo[-1].file_id
                file_unique_id = update.message.photo[-1].file_unique_id

                new_file = context.bot.get_file(file_id)
                saving_path = os.path.join(downloaded_path, "{}.jpg".format(file_unique_id))
                new_file.download(saving_path)

                im = pyimgur.Imgur(client_id)
                uploaded_image = im.upload_image(saving_path, title="nothing")

                print("link = ", uploaded_image.link)
                result = image_search_google(uploaded_image.link)

                for res in result:
                    update.message.reply_text(res["link"])

                user_state[user_id]["role"] = None

                # context.bot.send_photo(update.message.chat.id, open(saving_path, 'rb'), 'This is your image')
                # context.bot.send_message(chat_id=update.effective_chat.id, text="Thanks for image")
            except:
                context.bot.send_message(chat_id=update.effective_chat.id, text="error")
    else:
        update.message.reply_text("please type /start first!")


def build_menu(buttons,n_cols,header_buttons=None,footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

def target_selection(update, context, last_message):
    button_labels = [['Atheism'], ['Climate Change Concern'], ['Donald Trump'],\
                     ['Feminist'], ['Hillary Clinton'], ['Legalization of Abortion']]
    
    reply_keyboard = ReplyKeyboardMarkup(button_labels)
    context.bot.send_chat_action(chat_id=update.effective_user.id, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=update.message.chat_id,text='please choose a target!',reply_markup=reply_keyboard)

def api_pipline(update, context, stage="stage0"):
    user_id = update.message.chat.id
    print("stage : ", stage)
    if stage == "stage0":
        user_state[user_id]["role"] = "stance_detection"
        user_state[user_id]["state"] = "stage1"
        target_selection(update, context, last_message)
    elif stage == "stage1":
        user_state[user_id]["target"] = update.message.text
        update.message.reply_text("please enter a text!")
    elif stage == "stage2":
        user_state[user_id]["text"] = update.message.text
        result = api_test(user_state[user_id]["target"], user_state[user_id]["text"])
        
        reply_msg = f'Target : {user_state[user_id]["target"]}\
                    \n\nText : {user_state[user_id]["text"]}\
                    \n\nOur Stance Prediction : {result}'
        update.message.reply_text(reply_msg)

        buttons = [[InlineKeyboardButton("👍", callback_data="like")],
                   [InlineKeyboardButton("👎", callback_data="dislike")]]
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 reply_markup=InlineKeyboardMarkup(buttons),
                                 text="Do you agree with our prediction?")


def api_test(stance_target, stance_text):
    # TODO : change after deploy API successfully
    print(stance_text)
    print(stance_target)
    result = 'None'
    # API_dictionary = {
    #     "topic": stance_text,
    #     "tweet": stance_target}
    
    # # API URL
    # api_url = "http://172.17.3.126:9100//"
    # header = {"X-Api-Key": 'w6MCbeG3-kpiR1cZu2JoAQ'}
    # # get response from API
    # t1 = time.time()
    # response = requests.post(api_url, json=API_dictionary, headers=header)
    # # get json part of response
    # result = response.json()
    # t2 = time.time()
    # print("result : ", result)
    
    # print("time taken:", t2 - t1)
    return result


def text_message(update, context):
    user_id = update.message.chat.id
    
    print("here in text message")
    print("update.message.text : ", update.message.text)

    if user_id not in user_state or user_state[user_id]["role"] == None:
        print("if")
        button_list = [stance, text, image]
        user_state[user_id] = {"role" : None, "state" : None, "target" : None, "text" : None}
        if stance in update.message.text:
            user_state[user_id]["role"] = "stance_detection"
            api_pipline(update, context, "stage0")
        elif text == update.message.text:
            user_state[user_id]["role"] = "text"
            update.message.reply_text("Now you can send your text.")
        elif image in update.message.text:
            user_state[user_id]["role"] = "image"
            update.message.reply_text("Now you can send your image.")
        else:
            update.message.reply_text("please type /start first!")

    else:
        print("else")
        print('user_state[user_id]["role"] : ', user_state[user_id]["role"])
        if user_state[user_id]["role"] == "text":
            print_website_names(update, context)
            
        elif user_state[user_id]["role"] == "stance_detection":
            if user_state[user_id]["state"] == "stage1":
                api_pipline(update, context, "stage1")
                user_state[user_id]["state"] = "stage2"
            elif user_state[user_id]["state"] == "stage2":
                api_pipline(update, context, "stage2")
                user_state[user_id]["role"] = None
                buttons = [[KeyboardButton(stance)], [KeyboardButton(text)], [KeyboardButton(image)]]
    
                last_message[0] = context.bot.send_message(chat_id=update.effective_chat.id,
                                        reply_markup=ReplyKeyboardMarkup(buttons), text="Try out other functionality!")
            else:
                api_pipline(update, context, "stage0")
                user_state[user_id].append("stage1")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(CommandHandler("targets", target_selection))

    dp.add_handler(MessageHandler(Filters.text, text_message))

    dp.add_handler(MessageHandler(Filters.document, downloadImageDoc))
    dp.add_handler(MessageHandler(Filters.photo, downloadImagePhoto))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
    
