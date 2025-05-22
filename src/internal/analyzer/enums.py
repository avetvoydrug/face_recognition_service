from enum import Enum

class StrEnum(str, Enum):
    def __str__(self) -> str:
        return str.__str__(self)

    def __repr__(self, *args, **kwargs):
        return str.__repr__(self)


class DetectorModelsEnum(StrEnum):
    OpenCV = 'opencv' 
    SSD = 'ssd' 
    Dlib = 'dlib' 
    MtCNN = 'mtcnn'
    FastmtCNN = 'fastmtcnn'
    RetinaFace = 'retinaface' 
    Mediapipe = 'mediapipe'
    Yolov8 = 'yolov8'
    Yunet = 'yunet'
    Centerface = 'centerface'

class ActionNameEnum(StrEnum):
    AGE = "age"
    GENDER = "gender"
    RACE = "race"
    EMOTION = "emotion"

class GenderEnum(StrEnum):
    WOMAN = "Woman"
    MAN = "Man"

class RaceEnum(StrEnum):
    ASIAN = "asian"
    INDIAN = "indian"
    BLACK = "black"
    WHITE = "white"
    MIDDLE_EASTERN = "middle eastern"
    LATINO_HISPANIC = "latino hispanic"

class EmotionEnum(StrEnum):
    ANGRY = "angry"
    DISGUST = "disgust"
    FEAR = "fear"
    HAPPY = "happy"
    SAD = "sad"
    SURPRISE = "surprise"
    NEUTRAL = "neutral"

class LoggerRoleEnum(StrEnum):
    API = "API: -"
    REPO = "REPOSITORY: -"
    SERVICE = "SERVICE: -"