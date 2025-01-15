import os
import requests
import argparse
from dotenv import load_dotenv
from image_utils import download_image, get_file_extension


def download_image(url, save_path):

    response = requests.get(url, stream=True)
    response.raise_for_status()

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)


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


def fetch_and_save_apod_images(api_key, save_directory, count=1):

    images = fetch_apod_images_data(api_key, count)
    save_apod_images(images, save_directory)


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

        fetch_and_save_apod_images(nasa_api_key, args.save_directory, args.count)
    except Exception as e:
        print(f"Ошибка: {e}")
