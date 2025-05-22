
from fastapi import APIRouter, HTTPException, Query, UploadFile, File

from internal.api.v1.schemas.request.analyzer import FaceAnalyzeRequest
from internal.api.v1.schemas.response.analyzer import FaceAnalyzeResponse

from internal.dependencies.analyzer import FaceAnalyzerServiceDependency
from internal.analyzer.enums import DetectorModelsEnum, ActionNameEnum, LoggerRoleEnum
from internal.config import logger
from datetime import datetime


ANALYZER: APIRouter = APIRouter()


@ANALYZER.get("/check")
async def ping():
    return {
        "status": "ok"
    }

@ANALYZER.get("/face_analyze")
async def get_face_analyze(
    link: str, 
    service: FaceAnalyzerServiceDependency,
    actions: tuple[ActionNameEnum, ...] = Query(default=(ActionNameEnum.AGE, ActionNameEnum.EMOTION, ActionNameEnum.GENDER, ActionNameEnum.RACE)),
    anti_spoofing: bool = False,
    detector_backend: DetectorModelsEnum = DetectorModelsEnum.SSD
    ) -> FaceAnalyzeResponse:
    logger.info(f"{LoggerRoleEnum.API} Received Params: (actions={actions}; anti_spoofing={anti_spoofing}; detector_backend={detector_backend}; link={link})")
    result = await service.get_face_analyze(link=link, anti_spoofing=anti_spoofing, detector_backend=detector_backend, actions=actions)
    response = FaceAnalyzeResponse(faces=result)
    return response

@ANALYZER.post("/face_analyze_file")
async def analyze_face_file(
    service: FaceAnalyzerServiceDependency,
    image: UploadFile = File(...),
    actions: tuple[ActionNameEnum, ...] = Query(default=(ActionNameEnum.AGE, ActionNameEnum.EMOTION, ActionNameEnum.GENDER, ActionNameEnum.RACE)),
    anti_spoofing: bool = False,
    detector_backend: DetectorModelsEnum = DetectorModelsEnum.SSD
) -> FaceAnalyzeResponse:
    """
    Анализ лица на изображении, переданном как файл.
    """
    logger.info(f"{LoggerRoleEnum.API} Received params: (detector_backend={detector_backend}; anti_spoofing={anti_spoofing}; actions={actions})")
    start = datetime.now()
    contents = await image.read()

    result = await service.get_face_analyze_file(content=contents, detector_backend=detector_backend, actions=actions, anti_spoofing=anti_spoofing, start=start)
    response = FaceAnalyzeResponse(faces=result)
    end = datetime.now()
    logger.info(f"{LoggerRoleEnum.API} total execute {end - start}")
    return response