import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from pytube import YouTube

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# Define the start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to the YouTube Downloader bot! Please send me a YouTube video URL to download.")

# Define the download command handler
def download(update: Update, context: CallbackContext) -> None:
    url = update.message.text
    try:
        yt = YouTube(url)
        video = yt.streams.first()
        video.download()
        update.message.reply_text("Video downloaded successfully!")
    except Exception as e:
        update.message.reply_text(f"Error downloading video: {str(e)}")

def main() -> None:
    # Create the Updater and pass in your bot's token
    updater = Updater(os.environ.get('BOT_TOKEN'))

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add the command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("download", download))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
