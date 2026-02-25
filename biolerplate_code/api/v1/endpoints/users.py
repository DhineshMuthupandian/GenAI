from fastapi import APIRouter
from fastapi_app.schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    return {"id": 1, "name": user.name, "email": user.email}

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return {"id": user_id, "name": "Test User", "email": "test@email.com"}