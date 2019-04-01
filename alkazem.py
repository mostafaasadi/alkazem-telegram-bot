import tempfile
from PIL import Image
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# Telegram API
# access  bot via token
updater = Updater(token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
dispatcher = updater.dispatcher


# on /start get user profile
def gp(bot, update):
    # download file
    fu = bot.get_user_profile_photos(update.message.from_user.id, limit=1)
    file = bot.get_file(fu.photos[0][-1].file_id)
    tf = tempfile.mkstemp('.png')
    file.download(tf[1])

    try:
        img = Image.open(tf[1]).convert('RGBA')
        wm = Image.open('hazrat.png').convert('RGBA')
        width, height = wm.size
        ns = 0.3
        size = (int(width * ns), int(height * ns))
        wm = wm.resize(size, Image.ANTIALIAS)
        img.alpha_composite(wm, (40, 450))
        img = img.convert('LA')
        img.save(tf[1])
    except Exception as e:
        print(e)
    bot.send_photo(update.message.chat_id, open(tf[1], 'rb'))


# get image from user
def gpd(bot, update):
    # download file
    file = bot.getFile(update.message.photo[-1].file_id)
    tf = tempfile.mkstemp('.png')
    file.download(tf[1])

    try:
        img = Image.open(tf[1]).convert('RGBA')
        wm = Image.open('hazrat.png').convert('RGBA')
        width, height = wm.size
        ns = 0.3
        size = (int(width * ns), int(height * ns))
        wm = wm.resize(size, Image.ANTIALIAS)
        img.alpha_composite(wm, (40, 450))
        img = img.convert('LA')
        img.save(tf[1])
    except Exception as e:
        print(e)
    bot.send_photo(update.message.chat_id, open(tf[1], 'rb'))


# help
def gpt(bot, update):
    bot.sendMessage(
        chat_id=update.message.chat_id,
        text='یک عکس ارسال کنید و یا برای استفاده از تصویر پروفایل از دستور /start استفاده کنید'
    )


def main():
    # handle dispatcher
    dispatcher.add_handler(CommandHandler('start', gp))
    dispatcher.add_handler(MessageHandler(Filters.photo, gpd))
    dispatcher.add_handler(MessageHandler(Filters.text, gpt))

    # run
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
