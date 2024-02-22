from fastapi import APIRouter

router = APIRouter()

@router.get("/create_item")
async def create_item():
    return {"name": "Hello"}

@router.get("/delete_item")
async def create_item():
    return {"name": "Hello"}