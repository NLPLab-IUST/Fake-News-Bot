from environs import Env
from googlesearch import search
import logging
import os
from telegram.ext import *
from telegram import *
import pyimgur
from serpapi import GoogleSearch
from lan import Language, EN, FA
# Environment Variables
env = Env()  # new
env.read_env()  # read .env file, if it exists

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
# TOKEN = env.str("TOKEN")
TOKEN = "5684748227:AAEKsdSo2-TNAacjC-vy_xS01ckyFlkvjos"
LANGUAGE = EN

stance_target = None
stance_text = None
user_state = {}

stance = LANGUAGE.STANCE
text = LANGUAGE.TEXT
image = LANGUAGE.IMAGE
language = LANGUAGE.BOT_LANGUAGE
button_list = [stance, text, image]
client_id = "9345c5d096864df"
last_message = []

def assign_global_value():
    global stance, text, image, language, button_list
    stance = LANGUAGE.STANCE
    text = LANGUAGE.TEXT
    image = LANGUAGE.IMAGE
    language = LANGUAGE.BOT_LANGUAGE
    button_list = [stance, text, image]


def start(update: Update, context: CallbackContext):
    if len(last_message) != 0:
        context.bot.delete_message(chat_id=update.effective_chat.id, message_id=last_message[0].message_id)
    buttons = [[KeyboardButton(stance)], [KeyboardButton(text)], [KeyboardButton(image)], [KeyboardButton(language)]]
    user_id = update.message.chat.id
    user_state[user_id] = {"role" : None, "state" : None, "target" : None, "text" : None}
    last_message[0] = context.bot.send_message(chat_id=update.effective_chat.id,
                             reply_markup=ReplyKeyboardMarkup(buttons), text=LANGUAGE.WELCOME)


def stop(update: Update, context: CallbackContext):
    user_id = update.message.chat.id
    user_state[user_id] = {"role" : None, "state" : "stop", "target" : None, "text" : None}
    context.bot.send_message(chat_id=update.effective_chat.id, text = LANGUAGE.STOP_BOT)


def about(update, context):
    text = LANGUAGE.ABOUT
    update.message.reply_text(text)


def help(update, context):
    text = LANGUAGE.HELP
    update.message.reply_text(text)


def pending_stance_detection(update: Update, context: CallbackContext):
    user_id = update.message.chat.id
    if user_id in user_state and user_state[user_id]["state"] != "stop":
        user_state[user_id] = {"role" : None, "state" : None, "target" : None, "text" : None}
        user_state[user_id]["role"] = "stance_detection"
        api_pipline(update, context, "stage0")
    else:
        update.message.reply_text(LANGUAGE.TYPE_START_FIRST)


def pending_search_text(update: Update, context: CallbackContext):
    user_id = update.message.chat.id
    if user_id in user_state and user_state[user_id]["state"] != "stop":
        user_state[user_id] = {"role" : None, "state" : None, "target" : None, "text" : None}
        user_state[user_id]["role"] = "text"
        update.message.reply_text(LANGUAGE.SEND_TEXT)
    else:
        update.message.reply_text(LANGUAGE.TYPE_START_FIRST)


def pending_search_image(update: Update, context: CallbackContext):
    user_id = update.message.chat.id
    if user_id in user_state and user_state[user_id]["state"] != "stop":
        user_state[user_id] = {"role" : None, "state" : None, "target" : None, "text" : None}
        user_state[user_id]["role"] = "image"
        update.message.reply_text(LANGUAGE.SEND_IMAGE)
    else:
        update.message.reply_text(LANGUAGE.TYPE_START_FIRST)


def pending_bot_language(update: Update, context: CallbackContext):
    user_id = update.message.chat.id
    user_state[user_id] = {"role" : None, "state" : None, "target" : None, "text" : None}
    user_state[user_id]["role"] = "change_language"
    buttons = [[KeyboardButton(LANGUAGE.FARSI + Language.IRAN_FLAG)], [KeyboardButton(LANGUAGE.ENGLISH + Language.ENGLAND_FLAG)]]
    context.bot.send_message(chat_id=update._effective_chat.id, text=LANGUAGE.CHOOSE_LANGUAGE, reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))


def change_language(update: Update, context: CallbackContext):
    user_id = update.message.chat.id
    if user_state[user_id]["role"] == "change_language":
        global LANGUAGE
        choosen_language = update.message.text
        LANGUAGE = Language.LANGUAGE_SELECTOR[choosen_language]
        user_state[user_id]["role"] = None
        assign_global_value()
        start(update, context)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def build_menu(buttons,n_cols,header_buttons=None,footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu


def target_selection(update: Update, context: CallbackContext, last_message):
    button_labels = [[LANGUAGE.ATHEISM], [LANGUAGE.CLIMATE_CHANGE_CONCERN], [LANGUAGE.DONALD_TRUMP],\
                     [LANGUAGE.FEMINIST], [LANGUAGE.HILLARY_CLINTON], [LANGUAGE.LEGALIZATION_OF_ABORTION]]

    reply_keyboard = ReplyKeyboardMarkup(button_labels)
    context.bot.send_chat_action(chat_id=update.effective_user.id, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=update.message.chat_id, text=LANGUAGE.TARGET_SELECTION, reply_markup=reply_keyboard)


def like_feedback(update: Update, context: CallbackContext):
    user_id = update.message.chat.id
    if user_id in user_state and user_state[user_id]['state'] == 'stage2':
        #.............
        #... TODO ....
        #.............
        user_state[user_id] = {"role" : None, "state" : None, "target" : None, "text" : None}
        buttons = [[KeyboardButton(stance)], [KeyboardButton(text)], [KeyboardButton(image)], [KeyboardButton(language)]]
        last_message[0] = context.bot.send_message(chat_id=update.effective_chat.id,
                                reply_markup=ReplyKeyboardMarkup(buttons), text=LANGUAGE.TRY_OTHER_FUNCTIONALITY)
    else:
        update.message.reply_text(LANGUAGE.UKNOWN_COMMAND)


def dislike_feedback(update: Update, context: CallbackContext):
    user_id = update.message.chat.id
    if user_id in user_state and user_state[user_id]['state'] == 'stage2':
        #.............
        #... TODO ....
        #.............
        user_state[user_id] = {"role" : None, "state" : None, "target" : None, "text" : None}
        buttons = [[KeyboardButton(stance)], [KeyboardButton(text)], [KeyboardButton(image)], [KeyboardButton(language)]]
        last_message[0] = context.bot.send_message(chat_id=update.effective_chat.id,
                                reply_markup=ReplyKeyboardMarkup(buttons), text=LANGUAGE.TRY_OTHER_FUNCTIONALITY)
    else:
        update.message.reply_text(LANGUAGE.UKNOWN_COMMAND)


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
                context.bot.send_message(chat_id=update.effective_chat.id, text=LANGUAGE.ERROR)
    else:
        update.message.reply_text(LANGUAGE.TYPE_START_FIRST)


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
                context.bot.send_message(chat_id=update.effective_chat.id, text=LANGUAGE.ERROR)
    else:
        update.message.reply_text(LANGUAGE.TYPE_START_FIRST)


def api_pipline(update, context, stage="stage0"):
    user_id = update.message.chat.id
    print("stage : ", stage)
    if stage == "stage0":
        user_state[user_id]["role"] = "stance_detection"
        user_state[user_id]["state"] = "stage1"
        target_selection(update, context, last_message)
    elif stage == "stage1":
        user_state[user_id]["target"] = update.message.text
        update.message.reply_text(LANGUAGE.SEND_TEXT)
    elif stage == "stage2":
        user_state[user_id]["text"] = update.message.text
        result = api_test(user_state[user_id]["target"], user_state[user_id]["text"])

        reply_msg = LANGUAGE.INSTANCE_DETECTION_RESULT(user_state[user_id]["target"], user_state[user_id]["text"], result)
        update.message.reply_text(reply_msg)

        buttons = [[KeyboardButton(LANGUAGE.POSITIVE_FEEDBACK)], [KeyboardButton(LANGUAGE.NEGATIVE_FEEDBACK)]]
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True),
                                 text=LANGUAGE.AGREE_WITH_PREDICTION)


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

    if user_id in user_state and user_state[user_id]["state"] == "stop":
        update.message.reply_text(LANGUAGE.TYPE_START_FIRST)

    elif user_id not in user_state or user_state[user_id]["role"] == None:
        print("if")
        user_state[user_id] = {"role" : None, "state" : None, "target" : None, "text" : None}
        if stance in update.message.text:
            pending_stance_detection(update, context)
        elif text == update.message.text:
            pending_search_text(update, context)
        elif image in update.message.text:
            pending_search_image(update, context)
        else:
            update.message.reply_text(LANGUAGE.UKNOWN_COMMAND)

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
            else:
                api_pipline(update, context, "stage0")
                user_state[user_id].append("stage1")



def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    start_command = BotCommand('start', 'Start the bot')
    stop_command = BotCommand('stop', 'Stop the bot')
    about_command = BotCommand('about', 'Summary of the purpose of the bot')
    help_command = BotCommand('help', 'Description of commands')
    language_command = BotCommand('bot_language', 'Change the language of the bot')
    stance_command = BotCommand('stance', 'Stance Detection')
    image_command = BotCommand('image_search', 'Search Image')
    text_command = BotCommand('text_search', 'Search Text')
    bot_commands = [start_command, stop_command, about_command, help_command,\
                    language_command, stance_command, text_command, image_command]
    dp.bot.set_my_commands(bot_commands)

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stop", stop))
    dp.add_handler(CommandHandler("about", about))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("stance", pending_stance_detection))
    dp.add_handler(CommandHandler('bot_language', pending_bot_language))
    dp.add_handler(CommandHandler('text_search', pending_search_text))
    dp.add_handler(CommandHandler('image_search', pending_search_image))

    dp.add_handler(MessageHandler(Filters.text(Language.BOT_LANGUAGE), pending_bot_language))
    dp.add_handler(MessageHandler(Filters.text(Language.LANGUAGES), change_language))
    dp.add_handler(MessageHandler(Filters.text(Language.POSITIVE_FEEDBACKS), like_feedback))
    dp.add_handler(MessageHandler(Filters.text(Language.NEGATIVE_FEEDBACKS), dislike_feedback))
    dp.add_handler(MessageHandler(Filters.text, text_message))
    dp.add_handler(MessageHandler(Filters.document, downloadImageDoc))
    dp.add_handler(MessageHandler(Filters.photo, downloadImagePhoto))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
