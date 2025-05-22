import os
import requests

from pathlib import Path

from internal.utils import ResolverPath

_CUR_DATA_DIR = "_temp"

def mk_temp_file_path() -> Path:
    path = ResolverPath()
    temp_dir = path.TEMP_DIR
    os.makedirs(temp_dir, exist_ok=True)

    filename = "temp_image.jpg"
    filepath = temp_dir / filename
    return filepath

def download_image_to_cur_data(image_url):
    """
    Загружает изображение по URL и сохраняет его в папку ./_cur_data.

    Args:
        image_url: URL изображения.

    Returns:
        Путь к скачанному файлу (внутри ./_cur_data), или None в случае ошибки.
    """
    try:
        filepath = mk_temp_file_path()
        response = requests.get(image_url, stream=True)
        response.raise_for_status()

        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        return str(filepath)
    
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при скачивании изображения: {e}")
        return None
    except Exception as e:
        print(f"Ошибка: {e}")
        return None


def delete_image_from_cur_data(filepath):
    """
    Удаляет файл изображения из папки ./_cur_data.

    Args:
        filepath: Полный путь к файлу, который нужно удалить.

    Returns:
        True, если файл успешно удален, False в случае ошибки.
    """
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            return True
        else:
            print(f"Файл не найден: {filepath}")
            return False
    except Exception as e:
        print(f"Ошибка при удалении файла: {e}")
        return False