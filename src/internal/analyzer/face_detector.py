import face_recognition
from deepface import DeepFace
import cv2  # для загрузки изображений

def analyze_face(*, image_path: str)-> list[dict] | dict | None:
    """
    Анализирует лицо на изображении.

    Args:
        image_path: Путь к файлу изображения.

    Returns:
        Словарь с результатами анализа, или None в случае ошибки.
    """
    try:
        # 1. Обнаружение лиц и извлечение признаков
        img = cv2.imread(image_path)
        if img is None:
            return None # Если изображение не загрузилось

        face_locations = face_recognition.face_locations(img)  # Обнаружение лиц
        if not face_locations:
            return {"status": "не человек", "reason": "лицо не обнаружено"}

        results = []
        for (top, right, bottom, left) in face_locations:
            face_image = img[top:bottom, left:right]

            # 2. Классификация (простейший вариант: проверка размера лица)
            face_height = bottom - top
            face_width = right - left

            if face_width < 50 or face_height < 50:  # Пример грубого фильтра
                results.append({"status": "не реальный человек", "reason": "слишком маленькое лицо"})
                continue

            # 3. Определение пола и возраста (используем deepface)
            try:
                analysis = DeepFace.analyze(img_path=face_image, actions=['age', 'gender'],enforce_detection=False)
                gender = analysis[0]['dominant_gender']
                age = analysis[0]['age']
                results.append({
                    "status": "человек",
                    "gender": gender,
                    "age": age,
                })
            except Exception as e:
                results.append({"status": "человек", "gender": "неизвестно", "age": "неизвестно", "reason": f"Ошибка при определении пола/возраста: {e}"})

        return results
    except Exception as e:
        print(f"Общая ошибка: {e}")
        return None