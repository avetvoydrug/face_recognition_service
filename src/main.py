from fastapi import FastAPI

from internal.api.router import router

app: FastAPI = FastAPI()

app.include_router(router=router)

# fastapi dev src/main.py