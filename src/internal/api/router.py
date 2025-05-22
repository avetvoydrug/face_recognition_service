from fastapi import APIRouter

from internal.api.v1.router import V1_ROUTER


router: APIRouter = APIRouter()
router.include_router(router=V1_ROUTER)