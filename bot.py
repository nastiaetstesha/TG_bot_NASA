import os
from dotenv import load_dotenv
from telegram.bot import Bot
from telegram.error import TelegramError


def publish_to_telegram_channel(token, channel_id, text=None, image_path=None):

    bot = Bot(token=token)
    if text:
        bot.send_message(chat_id=channel_id, text=text)

    if image_path:
        with open(image_path, 'rb') as image:
            bot.send_photo(chat_id=channel_id, photo=image)



if __name__ == "__main__":
    load_dotenv()

    token = os.getenv("TG_ACCESS_TOKEN")
    channel_id = os.getenv("TG_CHANNEL_ID")

    if not token or not channel_id:
        raise ValueError("TG_ACCESS_TOKEN или TG_CHANNEL_ID не указаны в .env файле")

    message_text = "Hello"
    image_path = "nasa_images/nasa_apod1.jpg"

    try:
        publish_to_telegram_channel(token, channel_id, text=message_text, image_path=image_path)
        print("Сообщение успешно отправлено в канал!")
    except TelegramError as e:
        print(f"Ошибка отправки сообщения в Telegram: {e}")
