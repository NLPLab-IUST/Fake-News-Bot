from urllib.parse import unquote

class EN:
    STANCE = "Stance Detection"
    TEXT = "Search Text"
    IMAGE = "Search Image"
    BOT_LANGUAGE = "Bot Language"
    WELCOME = "Welcome to the Stance Detection bot. \nThis bot is created by our NLPlab team at the University of science and technology. \n\nYou can also check our website to see other works of ours. \nhttps://main-web.pvqa-frontend.pages.dev"
    STOP_BOT = "Thanks for using our bot\n GoodBye 👋"
    ABOUT = "The main purpose of this bot is to detect the stance of the input text according to the chosen target. \nFirst of all, you need to choose a target. Then, you can type your desired text which you want to know about its stance. The provided AI will predict the stance of your given text."
    HELP = '''
    Functionality:\n
    /stance: The detection of the stance of the sent text in relation to the target has been determined\n
    /text_search: The first 5 searched links related to the sent text\n
    /image_search: The first 5 searched links related to the sent image
    '''
    ERROR = "error"
    UNKNOWN_COMMAND = "🔴 Unknown command!"
    TYPE_START_FIRST = "please type /start first!"
    ATHEISM = "Atheism"
    CLIMATE_CHANGE_CONCERN = "Climate Change Concern"
    DONALD_TRUMP = "Donald Trump"
    FEMINIST = "Feminist"
    HILLARY_CLINTON = "Hillary Clinton"
    LEGALIZATION_OF_ABORTION = "Legalization of Abortion"
    TARGET_SELECTION = "please choose a target!"
    WRONG_TARGET = "please choose your target from below list"
    POSITIVE_FEEDBACK = "Yes 👍"
    NEGATIVE_FEEDBACK = "No 👎"
    WRONG_FORMAT = "the format of input is incorrect❗"

    def GET_MORE_INFO(links, topic=None, titles=None):
        result = f'Search topic: {topic}\n' if topic else ''
        result += f'Related links:\n'
        if titles is None:
            titles = []
            for link in links:
                titles.append(unquote(link)[8::])
        i = 0
        for link in links:
            result += f"\t{i+1}) <a href='{link}'>{titles[i]}</a>\n"
            i += 1
        return result

    def INSTANCE_DETECTION_RESULT(target, text, result):
        return f'Target : {target}\
                \n\nText : {text}\
                \n\nOur Stance Prediction : {result}'
    AGREE_WITH_PREDICTION = "Do you agree with our prediction?"
    SEND_TEXT = "Now you can send your text ..."
    SEND_IMAGE = "Now you can send your image ..."
    TRY_OTHER_FUNCTIONALITY = "Try out other functionality!"
    FARSI = "Farsi"
    ENGLISH = "English"
    CHOOSE_LANGUAGE = "Choose preferred language ..."


class FA:
    STANCE = "تشخیص موضع"
    TEXT = "جست و جوی متن"
    IMAGE = "جست و جوی تصویر"
    BOT_LANGUAGE = "زبان بات"
    WELCOME = "سلام، به بات تشخیص موضع خوش آمدید. \nاین ربات تلگرامی توسط تیم NLPlab ما در دانشگاه علم و صنعت ایران ایجاد شده است. \n\nبرای دیدن سایر فعالیت های تیم ما می توانید به وب سایت NLPlab سر بزنید. \nhttps://main-web.pvqa-frontend.pages.dev"
    STOP_BOT = "تشکر بابت استفاده از بات تلگرامی ما\nخدانگهدار 👋"
    ABOUT = "هدف کلی این ربات تشخیص موضع اخبار است. \nبه این صورت که شما باید یکی از موضوعات ارائه شده را انتخاب کنید و در ادامه متنی که می خواهید موضع آن را بدانید را وارد می کنید. سپس مدل هوش مصنوعی ما، موضع متن شما را تشخیص می دهد. \n"
    HELP = '''
    کارکردها:
    /stance: تشخیص موضع متن ارسالی نسبت به موضوع تعیین شده \n
    /text_search: پنج لینک اول جستجو شده مربوط به متن ارسال شده \n
    /image_search: پنج لینک اول جستجو شده مربوط به تصویر ارسال شده 
    '''
    ERROR = "خطا"
    UKNOWN_COMMAND = "🔴 دستور ناشناخته!"
    TYPE_START_FIRST = "لطفا ابتدا /start را تایپ کنید"
    ATHEISM = "کفر"
    CLIMATE_CHANGE_CONCERN = "نگرانی تغییرات آب و هوا"
    DONALD_TRUMP = "دونالد ترامپ"
    FEMINIST = "فمینیست"
    HILLARY_CLINTON = "هیلاری کلینتون"
    LEGALIZATION_OF_ABORTION = "قانونی شدن سقط جنین"
    TARGET_SELECTION = "لطفا یک عنوان را انتخاب کنید!"
    WRONG_TARGET = "لطفا موضوع خود را از بین موضوع های لیست زیر انتخاب کنید"
    POSITIVE_FEEDBACK = "بله 👍"
    NEGATIVE_FEEDBACK = "خیر 👎"
    WRONG_FORMAT = "فرمت پیام ارسالی اشتباه است❗"

    def GET_MORE_INFO(links, topic=None, titles=None):
        result = f'موضوع جستجو: {topic}\n' if topic else ''
        result += f'لینک های مرتبط:\n'
        if titles is None:
            titles = []
            for link in links:
                titles.append(unquote(link)[8::])
        i = 0
        for link in links:
            result += f"\t{i+1}) <a href='{link}'>{titles[i]}</a>\n"
            i += 1
        return result

    def INSTANCE_DETECTION_RESULT(target, text, result):
        return f'نمونه : {target}\
                \n\nمتن : {text}\
                \n\nپیش بینی ما : {result}'
    AGREE_WITH_PREDICTION = "آیا با پیش بینی ما موافقید؟"
    SEND_TEXT = "حالا میتوانید متن خود را بفرستید ..."
    SEND_IMAGE = "حالا میتوانید تصویر خود را بفرستید ..."
    TRY_OTHER_FUNCTIONALITY = "عملکردهای دیگر را امتحان کنید!"
    FARSI = "فارسی"
    ENGLISH = "انگلیسی"
    CHOOSE_LANGUAGE = "زبان بات را انتخاب کنید ..."

class Language:
    IRAN_FLAG = "🇮🇷"
    ENGLAND_FLAG = "🇬🇧"
    IRAN_EN = 'Farsi' + IRAN_FLAG
    IRAN_FA =  'فارسی' + IRAN_FLAG
    ENGLAND_EN = 'English' + ENGLAND_FLAG
    ENGLAND_FA =  'انگلیسی' + ENGLAND_FLAG
    LANGUAGES = [IRAN_EN, IRAN_FA, ENGLAND_EN, ENGLAND_FA]
    LANGUAGE_SELECTOR = {
        IRAN_EN: FA, IRAN_FA: FA,
        ENGLAND_EN: EN, ENGLAND_FA: EN
    }
    BOT_LANGUAGE = [EN.BOT_LANGUAGE, FA.BOT_LANGUAGE]
    POSITIVE_FEEDBACKS = [EN.POSITIVE_FEEDBACK, FA.POSITIVE_FEEDBACK]
    NEGATIVE_FEEDBACKS = [EN.NEGATIVE_FEEDBACK, FA.NEGATIVE_FEEDBACK]