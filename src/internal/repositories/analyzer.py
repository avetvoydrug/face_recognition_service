from internal.analyzer.face_analyze import analyze_face
from internal.analyzer.enums import DetectorModelsEnum
from internal.dto.face_analyzer import FaceAnalyzeDetails, ErrorDetect

class FaceAnalyzeRepository:
    def __init__(self) -> None:
        pass

    async def get_face_analyze(self, img_path, anti_spoofing: bool, detector_backend: DetectorModelsEnum, actions: tuple = ("age", "gender", "race", "emotion")) -> list[FaceAnalyzeDetails] | ErrorDetect:
        total_faces: list[FaceAnalyzeDetails] | ErrorDetect = analyze_face(img_path=img_path, anti_spoofing=anti_spoofing, detector_backend=detector_backend, actions=actions)
        return total_faces