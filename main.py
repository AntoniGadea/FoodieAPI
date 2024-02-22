from fastapi import FastAPI
from app.api.endpoints.order import router as order_router

app = FastAPI()

app.include_router(order_router, prefix="/order")