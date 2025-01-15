import os
import requests


def get_file_extension(url):

    filename = os.path.basename(urlsplit(url).path)
    return os.path.splitext(filename)[1]


def download_image(url, save_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)