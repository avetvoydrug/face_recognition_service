from pydantic import BaseModel


class FaceAnalyzeRequest(BaseModel):
    link: str