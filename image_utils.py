import os
import requests

from dotenv import load_dotenv
from urllib.parse import urlsplit


def get_file_extension(url):

    filename = os.path.basename(urlsplit(url).path)
    return os.path.splitext(filename)[1]


def download_image(url, save_path):
    load_dotenv()
    api_key = os.getenv("NASA_API_KEY")
    if not api_key:
        raise ValueError("API-ключ NASA не найден. Убедитесь, что он указан в файле .env.")

    params = {
        'api_key': api_key
    }
    response = requests.get(url, params=params, stream=True)
    response.raise_for_status()

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)