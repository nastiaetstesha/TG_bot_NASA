import os
import requests
import argparse

from dotenv import load_dotenv
from image_utils import download_image, get_file_extension


def fetch_apod_images_data(api_key, count=1):

    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": api_key,
        "count": count
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


def save_apod_images(images, save_directory):

    for index, image_info in enumerate(images, start=1):
        image_url = image_info.get("url")
        if not image_url or not image_url.startswith("http"):
            raise ValueError(f"Некорректный URL изображения: {image_url}")

        extension = os.path.splitext(image_url)[-1]
        file_name = f"nasa_apod_{index}{extension}"
        save_path = os.path.join(save_directory, file_name)
        download_image(image_url, save_path)


if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser(description="Скачивает фотографии APOD от NASA.")
    parser.add_argument("--save_directory", type=str, help="Папка для сохранения фотографий.", default="apod_images")
    parser.add_argument("--count", type=int, help="Количество изображений для скачивания.", default=1)

    args = parser.parse_args()

    try:
        nasa_api_key = os.getenv("NASA_API_KEY")
        if not nasa_api_key:
            raise ValueError("API-ключ NASA не найден. Убедитесь, что он указан в файле .env.")

        images = fetch_apod_images_data(nasa_api_key, args.count)
        save_apod_images(images, args.save_directory)

    except FileNotFoundError as e:
        print(f"Ошибка: Директория не найдена — {e}")

    except ValueError as e:
        print(f"Ошибка: Некорректное значение — {e}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API NASA: {e}")
