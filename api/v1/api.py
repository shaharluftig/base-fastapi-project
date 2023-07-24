from fastapi import APIRouter

from api.v1.routes.example import example_router

v1_router = APIRouter()

v1_router.include_router(example_router, prefix="/example")
