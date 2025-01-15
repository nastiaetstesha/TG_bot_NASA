# Проект: Загрузка фотографий из NASA и SpaceX

## Описание
Этот проект позволяет загружать фотографии из различных источников, включая SpaceX, APOD (Astronomy Picture of the Day) и EPIC (Earth Polychromatic Imaging Camera) API от NASA. Скрипты используют API для получения фотографий, которые сохраняются в указанные пользователем директории.

## Установка
1. **Клонируйте репозиторий или загрузите файлы.**
   ```bash
   git clone https://github.com/nastiaetstesha/TG_bot_NASA.git
   cd TG
   ```

2. **Создайте виртуальное окружение и активируйте его.**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Для macOS/Linux
   .venv\Scripts\activate   # Для Windows
   ```

3. **Установите зависимости.**
   ```bash
   pip install -r requirements.txt
   ```

4. **Создайте файл `.env` в корневой директории и добавьте ваш API-ключ NASA.**
   ```
   NASA_API_KEY=your_actual_api_key_here
   ```

## Скрипты

### 1. `fetch_spacex_images.py`
Этот скрипт загружает фотографии запусков SpaceX.

#### Использование:
```bash
python fetch_spacex_images.py --launch_id <launch_id> --save_directory <directory>
```

- `--launch_id`: ID запуска. Если не указан, будет использован последний запуск.
- `--save_directory`: Папка для сохранения фотографий (по умолчанию `images`).

#### Пример:
```bash
python fetch_spacex_images.py --launch_id latest --save_directory images
```

### 2. `fetch_nasa_apod_images.py`
Этот скрипт загружает фотографии из сервиса APOD от NASA.

#### Использование:
```bash
python fetch_nasa_apod_images.py --save_directory <directory> --count <number>
```

- `--save_directory`: Папка для сохранения фотографий (по умолчанию `apod_images`).
- `--count`: Количество фотографий для скачивания (по умолчанию `1`).

#### Пример:
```bash
python fetch_nasa_apod_images.py --save_directory nasa_images --count 5
```

### 3. `fetch_nasa_epic_images.py`
Этот скрипт загружает фотографии Земли из сервиса EPIC от NASA.

#### Использование:
```bash
python fetch_nasa_epic_images.py --save_directory <directory> --count <number>
```

- `--save_directory`: Папка для сохранения фотографий (по умолчанию `epic_images`).
- `--count`: Количество фотографий для скачивания (по умолчанию `5`).

#### Пример:
```bash
python fetch_nasa_epic_images.py --save_directory epic_images --count 10
```

## Общие функции
Общие функции, такие как `download_image` и `get_file_extension`, вынесены в файл `image_utils.py`. Эти функции обеспечивают повторное использование кода.

## Зависимости
- Python 3.7+
- Модули:
  - `requests`
  - `python-dotenv`
  - `argparse`

Установить зависимости можно с помощью команды:
```bash
pip install -r requirements.txt
```

## Примечания
- Убедитесь, что ваш API-ключ NASA активен. Если его нет, вы можете получить его [здесь](https://api.nasa.gov/).
- Убедитесь, что директории для сохранения фотографий существуют или будут созданы автоматически.


