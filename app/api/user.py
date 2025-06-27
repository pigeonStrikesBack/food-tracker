from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserUpdate, UserOut
from app.crud import user as crud_user
from app.dependencies import get_db

user_router  = APIRouter(prefix="/users", tags=["Users"])

@user_router.post("/", response_model=UserOut)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db, user)

@user_router.get("/", response_model=list[UserOut])
def read_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_user.get_users(db, skip, limit)

@user_router.get("/{user_id}", response_model=UserOut)
def read(user_id: int, db: Session = Depends(get_db)):
    user = crud_user.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.put("/{user_id}", response_model=UserOut)
def update(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    user = crud_user.update_user(db, user_id, user_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.delete("/{user_id}", response_model=UserOut)
def delete(user_id: int, db: Session = Depends(get_db)):
    user = crud_user.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
