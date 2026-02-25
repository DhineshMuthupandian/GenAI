from fastapi import FastAPI
from fastapi_app.api.api import api_router
from fastapi_app.core.config import settings

app = FastAPI(title=settings.APP_NAME)

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "FastAPI App Running"}