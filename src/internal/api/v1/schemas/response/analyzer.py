from pydantic import BaseModel

from internal.dto.face_analyzer import FaceAnalyzeDetails, ErrorDetect


class FaceAnalyzeResponse(BaseModel):
    faces: list[FaceAnalyzeDetails] | ErrorDetect

