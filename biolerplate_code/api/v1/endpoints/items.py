from fastapi import APIRouter
from fastapi_app.schemas.item import ItemCreate, ItemResponse

router = APIRouter()

@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate):
    return {"id": 1, "title": item.title, "description": item.description}

@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    return {"id": item_id, "title": "Sample", "description": "Demo item"}