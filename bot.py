import logging, random

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

list_start_word = []
list_start_word.append("Yo")
list_start_word.append("Oi")
list_start_word.append("Eh")
list_start_word.append("Wahlao")
list_start_word.append("LMAO")
list_start_word.append("Aiyo")

list_end_word = []
list_end_word.append("bro")
list_end_word.append("sis")
list_end_word.append("sia")
list_end_word.append("lor")
list_end_word.append("LOL")
list_end_word.append("ah")


def start(update, context):
    update.message.reply_text('Do you have anything you want to tell me bro?')


def help(update, context):
    update.message.reply_text('Just tell me anything bro.')


def echo(update, context):
    start = random.choice(list_start_word)
    end = random.choice(list_end_word)
    message = update.message.text
    response = ""
    sentence_ending_punctuation = ['!', '?', '.']
    if message[-1] in sentence_ending_punctuation:
        response = start + " " + update.message.text[0].lower(
        ) + update.message.text[1:-1] + " " + end + update.message.text[-1]
    else:
        response = start + " " + \
            update.message.text[0].lower(
            ) + update.message.text[1:] + " " + end
    update.message.reply_text(response)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("5079545952:AAGbgve-h1_aYM3iMtNFrcrD3qTKXuDVLHo", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()