import os
import requests
import argparse

from dotenv import load_dotenv
from image_utils import download_image, get_file_extension


def get_epic_image_metadata(api_key):

    url = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {
        "api_key": api_key
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


def generate_epic_image_url(image_info):
    base_url = "https://api.nasa.gov/EPIC/archive/natural"

    date = image_info['date'].split(' ')[0]
    year, month, day = date.split('-')

    image_name = image_info['image']

    return f"{base_url}/{year}/{month}/{day}/png/{image_name}.png"


def save_epic_images(images, save_directory):

    for index, image_info in enumerate(images, start=1):
        image_url = generate_epic_image_url(image_info)
        extension = get_file_extension(image_url)
        file_name = f"nasa_epic_{index}{extension}"
        save_path = os.path.join(save_directory, file_name)
        download_image(image_url, save_path)


if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser(description="Скачивает фотографии EPIC от NASA.")
    parser.add_argument("--save_directory", type=str, help="Папка для сохранения фотографий.", default="epic_images")
    parser.add_argument("--count", type=int, help="Количество изображений для скачивания.", default=5)

    args = parser.parse_args()

    nasa_api_key = os.getenv("NASA_API_KEY")
    if not nasa_api_key:
        raise ValueError("API-ключ NASA не найден. Убедитесь, что он указан в файле .env.")

    images = get_epic_image_metadata(nasa_api_key)
    if len(images) < args.count:
        raise ValueError(f"Запрошено {args.count} снимков, но доступно только {len(images)}.")

    try:
        save_epic_images(images[:args.count], args.save_directory)

    except FileNotFoundError as e:
        print(f"Ошибка: Директория не найдена — {e}")