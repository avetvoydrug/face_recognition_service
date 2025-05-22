from typing import Annotated

from fastapi import Depends

from internal.repositories.analyzer import FaceAnalyzeRepository
from internal.services.analyzer import FaceAnalyzerService


FaceAnalyzeRepositoryDependency = Annotated[FaceAnalyzeRepository, Depends(FaceAnalyzeRepository)]

def face_analyze_service_dep(repo: FaceAnalyzeRepositoryDependency):
    return FaceAnalyzerService(repo=repo)


FaceAnalyzerServiceDependency = Annotated[FaceAnalyzerService, Depends(face_analyze_service_dep)]