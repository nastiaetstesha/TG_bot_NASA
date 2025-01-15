# Проект: Загрузка фотографий из NASA и SpaceX

## Описание
Этот проект позволяет загружать фотографии из различных источников, включая SpaceX, APOD (Astronomy Picture of the Day) и EPIC (Earth Polychromatic Imaging Camera) API от NASA. Скрипты используют API для получения фотографий, которые сохраняются в указанные пользователем директории.

## Установка
1. **Клонируйте репозиторий или загрузите файлы.**
   ```bash
   git clone https://github.com/nastiaetstesha/TG_bot_NASA.git
   cd /path/to/project
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


# Scheduled Telegram Publisher

## Описание
Скрипт предназначен для автоматической публикации изображений в Telegram-канал с заданной периодичностью. Поддерживает публикацию изображений из нескольких директорий, перемешивая их случайным образом после каждой итерации.

---

## Установка

### 1. Клонируйте репозиторий и перейдите в папку проекта:
```bash
cd /path/to/project
```

### 2. Установите зависимости:
```bash
pip install -r requirements.txt
```

### 3. Создайте файл `.env` в корне проекта:
Добавьте токен вашего бота и ID канала:
```env
TG_ACCESS_TOKEN=your_telegram_bot_token
TG_CHANNEL_ID=your_channel_id
```

- **TG_ACCESS_TOKEN**: Токен доступа бота Telegram (получите через [BotFather](https://core.telegram.org/bots#botfather)).
- **TG_CHANNEL_ID**: ID вашего Telegram-канала (например, `@YourChannelUsername` или `-100XXXXXXXXXX` для приватных каналов).

---

## Использование

Запустите скрипт с помощью команды:
```bash
python scheduled_telegram_publisher.py [OPTIONS]
```

### Аргументы:
- `--delay`: Задержка между публикациями в секундах (по умолчанию 4 часа, 14400 секунд).
- `--directories`: Список директорий, содержащих изображения для публикации.

### Примеры:
1. Публикация изображений каждые 4 часа из стандартных директорий:
   ```bash
   python scheduled_telegram_publisher.py
   ```

2. Публикация каждые 2 часа из указанной директории:
   ```bash
   python scheduled_telegram_publisher.py --delay 7200 --directories /path/to/dir1
   ```

3. Публикация каждые 6 часов из нескольких директорий:
   ```bash
   python scheduled_telegram_publisher.py --delay 21600 --directories /path/to/dir1 /path/to/dir2
   ```

---

## Примечания
- Скрипт автоматически игнорирует файлы, которые не являются изображениями (`.jpg`, `.jpeg`, `.png`).
- Telegram не принимает файлы больше 20 MB. Такие файлы будут пропущены.

---

## Остановка скрипта
Для остановки скрипта нажмите `Ctrl+C`.



