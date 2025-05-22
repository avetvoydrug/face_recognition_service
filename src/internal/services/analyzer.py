from internal.repositories.analyzer import FaceAnalyzeRepository
from internal.dto.face_analyzer import FaceAnalyzeDetails, ErrorDetect
from internal.analyzer.utils import download_image_to_cur_data, delete_image_from_cur_data, mk_temp_file_path
from internal.analyzer.enums import DetectorModelsEnum

from internal.config import logger
from datetime import datetime

class FaceAnalyzerService:
    def __init__(self, repo: FaceAnalyzeRepository):
        self.repo: FaceAnalyzeRepository = repo
    
    async def get_face_analyze(
            self, 
            link: str, 
            anti_spoofing: bool, 
            detector_backend: DetectorModelsEnum, 
            actions: tuple = ("age", "gender", "race", "emotion")
            ) -> list[FaceAnalyzeDetails] | ErrorDetect:
        image_path = download_image_to_cur_data(image_url=link)
        result = await self.repo.get_face_analyze(img_path=image_path, anti_spoofing=anti_spoofing, detector_backend=detector_backend, actions=actions)
        bol = delete_image_from_cur_data(filepath=image_path)
        return result
    
    async def get_face_analyze_file(
            self, 
            start, 
            content: bytes, 
            anti_spoofing: bool, 
            detector_backend: DetectorModelsEnum, 
            actions: tuple = ("age", "gender", "race", "emotion")
            ) -> list[FaceAnalyzeDetails] | ErrorDetect:
        image_path = mk_temp_file_path()
        with open(image_path, "wb") as f:
            f.write(content)
        end_write = datetime.now()
        logger.info(f"SERVICE: - end write for {end_write - start}")
        result = await self.repo.get_face_analyze(img_path=image_path, anti_spoofing=anti_spoofing, detector_backend=detector_backend, actions=actions)
        bol = delete_image_from_cur_data(filepath=str(image_path))
        return result
