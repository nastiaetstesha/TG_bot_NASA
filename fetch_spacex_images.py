import os
import requests
import argparse

from dotenv import load_dotenv
from urllib.parse import urlsplit, unquote
from image_utils import download_image, get_file_extension


def get_spacex_image_urls(launch_id="latest"):
    base_url = "https://api.spacexdata.com/v5/launches/"
    url = f"{base_url}{launch_id}"

    response = requests.get(url)
    response.raise_for_status()

    launch_data = response.json()
    images = launch_data.get("links", {}).get("flickr", {}).get("original", [])
    if not images:
        raise ValueError("Фотографии не найдены.")

    return images


def save_spacex_images(images, save_directory, launch_id=None):
    for index, image_url in enumerate(images, start=1):
        extension = get_file_extension(image_url)
        file_name = f"spacex_{launch_id or 'latest'}_{index}{extension}"
        save_path = os.path.join(save_directory, file_name)
        download_image(image_url, save_path)


if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser(description="Скачивает фотографии SpaceX.")
    parser.add_argument("--launch_id", type=str, help="ID запуска SpaceX (если не указан, используется последний запуск).", default=None)
    parser.add_argument("--save_directory", type=str, help="Папка для сохранения фотографий.", default="images")

    args = parser.parse_args()

    try:
        images = get_spacex_image_urls(launch_id=args.launch_id)

        save_spacex_images(images, save_directory=args.save_directory, launch_id=args.launch_id)

    except FileNotFoundError as e:
        print(f"Ошибка: Директория не найдена — {e}")

    except ValueError as e:
        print(f"Ошибка: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API SpaceX: {e}")
