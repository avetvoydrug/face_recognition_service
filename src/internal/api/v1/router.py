from fastapi import APIRouter

from internal.api.v1.analyzer import ANALYZER

V1_ROUTER: APIRouter = APIRouter(prefix="/v1")
V1_ROUTER.include_router(router=ANALYZER)