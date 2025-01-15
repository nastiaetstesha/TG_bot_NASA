import os
from dotenv import load_dotenv
from telegram.bot import Bot


def publish_to_telegram_channel(token, channel_id, text):

    bot = Bot(token=token)
    bot.send_message(chat_id=channel_id, text=text)


if __name__ == "__main__":
    load_dotenv()

    token = os.getenv("TG_ACCESS_TOKEN")
    channel_id = os.getenv("TG_CHANNEL_ID")

    if not token or not channel_id:
        raise ValueError("TG_ACCESS_TOKEN или TG_CHANNEL_ID не указаны в .env файле")

    # Текст для публикации
    message_text = "Hello"

    try:
        publish_to_telegram_channel(token, channel_id, message_text)
        print("Сообщение успешно отправлено в канал!")
    except Exception as e:
        print(f"Ошибка отправки сообщения: {e}")
