from deepface import DeepFace

from internal.dto.face_analyzer import FaceRegion, FaceAnalyzeDetails, Gender, Race, Emotion, ErrorDetect
from internal.analyzer.enums import DetectorModelsEnum, LoggerRoleEnum
from internal.config import logger
# RetinaFace | Yolov8

# FastmtCNN - +- норм по возрасту и тёлок парсит
# RetinaFace - распазнаёт всех и анимэ отсеивает, но грузит на 100
# MediaPipe - как будто более реальна по возрасту, но нужна помощь
# Yolov8 правильный пол возраст более менее, распазнаёт анимэ -> использование гуд, но после отсейки анимэ | грузит не много проц, использовать с anti_spoofing=False
# Yunet - не распознаёт чб. Откидывает анимэ. Правильно пол определяет. Возраст круче всех
# Centerface - не оч. но пол правильный и возраст +- норм и ЧБ распознаёт    

def analyze_face(
        *, 
        img_path, 
        anti_spoofing: bool = False, 
        detector_backend: DetectorModelsEnum = DetectorModelsEnum.SSD, 
        actions: tuple = ("age", "gender", "race", "emotion")
        ) -> list[FaceAnalyzeDetails] | ErrorDetect:
    try:
        analyze_result = DeepFace.analyze(img_path=img_path, actions=actions, anti_spoofing=anti_spoofing, detector_backend=detector_backend)
        total_faces: list = []
        for face in analyze_result:
            logger.info(f"{LoggerRoleEnum.REPO} face={face}")
            face: FaceAnalyzeDetails = compile_result(face=face)
            total_faces.append(face)
    except Exception as e:
        logger.error(f"{__file__} err is:\n{e}")
        if str(e).startswith("Spoof"):
            return ErrorDetect(spoof=True, detect_failed=False)
        elif str(e).startswith("Face could not be detected"):
            return ErrorDetect(spoof=False, detect_failed=True)
        else:
            return ErrorDetect(spoof=False, detect_failed=False, any_error=str(e))
    return total_faces


def compile_result(face: dict):
    region_dict = face.pop("region", None)
    region_model = FaceRegion.model_validate(region_dict) if region_dict else None
    gender_dict = face.pop("gender", None)
    if gender_dict:
        woman = gender_dict.pop("Woman")
        man = gender_dict.pop("Man")
        gender_dict = dict(woman=woman, man=man)
    gender_model = Gender.model_validate(gender_dict) if gender_dict else None
    race_dict = face.pop("race", None)
    if race_dict:
        middle_eastern = race_dict.pop("middle eastern")
        latino_hispanic = race_dict.pop("latino hispanic")
        race_dict["latino_hispanic"] = latino_hispanic
        race_dict["middle_eastern"] = middle_eastern
    race_model = Race.model_validate(race_dict) if race_dict else None
    emotion_dict = face.pop("emotion", None)
    emotion_model = Emotion.model_validate(emotion_dict) if emotion_dict else None
    age = face.pop("age", None)
    face_confidence = face.pop("face_confidence", None)
    dominant_gender = face.pop("dominant_gender", None)
    dominant_race = face.pop("dominant_race", None)
    dominant_emotion = face.pop("dominant_emotion", None)
    face = FaceAnalyzeDetails(
        age=age,
        face_confidence=face_confidence,
        region=region_model, 
        gender=gender_model,
        dominant_gender=dominant_gender,
        race=race_model,
        dominant_race=dominant_race,
        emotion=emotion_model,
        dominant_emotion=dominant_emotion
        )
    return face