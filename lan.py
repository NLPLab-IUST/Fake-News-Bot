
class EN:
    STANCE = "Stance Detection"
    TEXT = "Search Text"
    IMAGE = "Search Image"
    BOT_LANGUAGE = "Bot Language"
    WELCOME = "Welcome to my bot!\nTODO: Write something to describe out bot functionality."
    ABOUT = "The purpose of this bot is to check the truthness of the combination of a text and an image from social media, thus it takes a text and an image as inputs, then it passes this inputs to our fact checking model. The output of this bot is a percentage that indicates the possibility that this corresponding news is fake."
    HELP = '''
    Commands:\n
    🔴 to start the bot and see the menu type /start \n
    🔴 for changing the language of bot type /bot_language\n
    🔴 type /about to learn about the bot and it's purpose\n
    '''
    ERROR = "error"
    TYPE_START_FIRST = "please type /start first!"
    ATHEISM = "Atheism"
    CLIMATE_CHANGE_CONCERN = "Climate Change Concern"
    DONALD_TRUMP = "Donald Trump"
    FEMINIST = "Feminist"
    HILLARY_CLINTON = "Hillary Clinton"
    LEGALIZATION_OF_ABORTION = "Legalization of Abortion"
    TARGET_SELECTION = "please choose a target!"

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
    ABOUT = "هدف این ربات بررسی صحت ترکیب یک متن و یک تصویر از رسانه های اجتماعی است، بنابراین یک متن و یک تصویر را به عنوان ورودی می گیرد، سپس این ورودی ها را به مدل بررسی واقعیت ما ارسال می کند. خروجی این ربات درصدی است که نشان دهنده احتمال جعلی بودن این خبر مربوطه است."
    HELP = '''
    دستور ها:\n
    🔴 برای شروع بات /start را تایپ کنید\n
    🔴 برای تغییر زبان بات /bot_language را تایپ کنید \n
    🔴 برای آشنایی با بات و هدف آن /about را تایپ کنید\n
    '''
    ERROR = "خطا"
    TYPE_START_FIRST = "را تایپ کنید \start لطفا ابتدا"
    ATHEISM = "کفر"
    CLIMATE_CHANGE_CONCERN = "نگرانی تغییرات آب و هوا"
    DONALD_TRUMP = "دونالد ترامپ"
    FEMINIST = "فمینیست"
    HILLARY_CLINTON = "هیلاری کلینتون"
    LEGALIZATION_OF_ABORTION = "قانونی شدن سقط جنین"
    TARGET_SELECTION = "لطفا یک عنوان را انتخاب کنید!"

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
    LANGUAGE_SELECTOR = {
        'farsi': FA, 'فارسی': FA,
        'english': EN, 'انگلیسی': EN
    }
    BOT_LANGUAGE = [EN.BOT_LANGUAGE, FA.BOT_LANGUAGE]