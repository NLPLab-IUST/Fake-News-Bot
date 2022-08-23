
class EN:
    STANCE = "Stance Detection"
    TEXT = "Search Text"
    IMAGE = "Search Image"
    BOT_LANGUAGE = "Bot Language"
    WELCOME = "Welcome to my bot!\nTODO: Write something to describe out bot functionality."
    STOP_BOT = "Thanks for using our bot\n GoodBye 👋"
    ABOUT = "The purpose of this bot is to check the truthness of the combination of a text and an image from social media, thus it takes a text and an image as inputs, then it passes this inputs to our fact checking model. The output of this bot is a percentage that indicates the possibility that this corresponding news is fake."
    HELP = '''
    Functionality:\n
    /stance: The detection of the stance of the sent text in relation to the target has been determined\n
    /text_search: The first 5 searched links related to the sent text\n
    /image_search: The first 5 searched links related to the sent image
    '''
    ERROR = "error"
    UKNOWN_COMMAND = "🔴 Uknown command!"
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
    WELCOME = "به ربات من خوش آمدید!\n TODO: چیزی برای توصیف عملکرد ربات بنویسید."
    STOP_BOT = "تشکر بابت استفاده از بات تلگرامی ما\nخدانگهدار 👋"
    ABOUT = "هدف این ربات بررسی صحت ترکیب یک متن و یک تصویر از رسانه های اجتماعی است، بنابراین یک متن و یک تصویر را به عنوان ورودی می گیرد، سپس این ورودی ها را به مدل بررسی واقعیت ما ارسال می کند. خروجی این ربات درصدی است که نشان دهنده احتمال جعلی بودن این خبر مربوطه است."
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