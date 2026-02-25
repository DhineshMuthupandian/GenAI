from fastapi import APIRouter
from fastapi_app.api.v1.endpoints import users, items

api_router = APIRouter(prefix="/api")

api_router.include_router(users.router, prefix="/v1/users", tags=["Users"])
api_router.include_router(items.router, prefix="/v1/items", tags=["Items"])