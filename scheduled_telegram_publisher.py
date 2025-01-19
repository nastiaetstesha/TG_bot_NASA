import os
import time
import random
import argparse

from dotenv import load_dotenv
from telegram import Bot


def publish_to_telegram_channel(token, channel_id, image_path):

    bot = Bot(token=token)
    with open(image_path, 'rb') as image:
        bot.send_photo(chat_id=channel_id, photo=image)


def get_images_from_directory(directory):

    return [os.path.join(directory, file) for file in os.listdir(directory) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]


def publish_images_periodically(token, channel_id, directories, delay):

    all_images = []
    for directory in directories:
        all_images.extend(get_images_from_directory(directory))

    if not all_images:
        raise ValueError("В указанных директориях не найдено изображений.")

    while True:
        random.shuffle(all_images)

        for image_path in all_images:
            try:
                publish_to_telegram_channel(token, channel_id, image_path)
                print(f"Изображение отправлено: {image_path}")
            except FileNotFoundError:
                print(f"Файл не найден: {image_path}. Пропускаем.")

            time.sleep(delay)


if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser(description="Публикует изображения в Telegram канал с заданной периодичностью.")
    parser.add_argument("--delay", type=int, help="Задержка между публикациями в секундах (по умолчанию 4 часа).", default=4 * 60 * 60)
    parser.add_argument("--directories", type=str, nargs='+', help="Список директорий с изображениями.", default=[
        "/Users/egorsemin/Practice/TG/epic_images",
        "/Users/egorsemin/Practice/TG/nasa_images",
        "/Users/egorsemin/Practice/TG/images"
    ])

    args = parser.parse_args()

    token = os.getenv("TG_ACCESS_TOKEN")
    channel_id = os.getenv("TG_CHANNEL_ID")

    if not token or not channel_id:
        raise ValueError("TG_ACCESS_TOKEN или TG_CHANNEL_ID не указаны в .env файле")

    try:
        publish_images_periodically(token, channel_id, args.directories, args.delay)
    except KeyboardInterrupt:
        raise KeyboardInterrupt("Остановка публикации.")
