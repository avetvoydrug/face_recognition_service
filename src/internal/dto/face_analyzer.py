from pydantic import BaseModel

from internal.analyzer.enums import RaceEnum, EmotionEnum, GenderEnum

class FaceRegion(BaseModel):
    x: int
    y: int
    w: int
    h: int
    left_eye: tuple | None
    right_eye: tuple | None

class Gender(BaseModel):
    woman: float
    man: float

class Race(BaseModel):
    asian: float
    indian: float
    black: float
    white: float
    middle_eastern: float
    latino_hispanic: float

class Emotion(BaseModel):
    angry: float
    disgust: float
    fear: float
    happy: float
    sad: float
    surprise: float
    neutral: float

class FaceAnalyzeDetails(BaseModel):
    age: int | None
    region: FaceRegion | None
    face_confidence: float | None
    gender: Gender | None
    dominant_gender: GenderEnum | None
    race: Race | None
    dominant_race: RaceEnum | None
    emotion: Emotion | None
    dominant_emotion: EmotionEnum | None

class ErrorDetect(BaseModel):
    spoof: bool
    detect_failed: bool
    any_error: str | None = None