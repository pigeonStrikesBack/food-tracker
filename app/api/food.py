from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.food import FoodCreate, FoodUpdate, FoodOut
from app.crud import food as crud_food
from app.dependencies import get_db

food_router  = APIRouter()

@food_router.post("/foods", response_model=FoodOut)
def create(food: FoodCreate, db: Session = Depends(get_db)):
    try:
        return crud_food.create_food(db, food)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@food_router.get("/foods", response_model=list[FoodOut])
def read_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_food.get_foods(db, skip, limit)

@food_router.get("/foods/{food_id}", response_model=FoodOut)
def read(food_id: int, db: Session = Depends(get_db)):
    food = crud_food.get_food(db, food_id)
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    return food

@food_router.put("/foods/{food_id}", response_model=FoodOut)
def update(food_id: int, food_data: FoodUpdate, db: Session = Depends(get_db)):
    food = crud_food.update_food(db, food_id, food_data)
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    return food

@food_router.delete("/foods/{food_id}", response_model=FoodOut)
def delete(food_id: int, db: Session = Depends(get_db)):
    food = crud_food.delete_food(db, food_id)
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    return food
