from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.food_entry import FoodEntryCreate, FoodEntryUpdate, FoodEntryOut
from app.crud import food_entry as crud_food_entry
from app.dependencies import get_db

food_entry_router  = APIRouter(prefix="/food-entries", tags=["Food Entries"])

@food_entry_router.post("/", response_model=FoodEntryOut)
def create(food_entry: FoodEntryCreate, db: Session = Depends(get_db)):
    try:
        return crud_food_entry.create_food_entry(db, food_entry)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@food_entry_router.get("/", response_model=list[FoodEntryOut])
def read_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_food_entry.get_food_entries(db, skip, limit)

@food_entry_router.get("/{food_entry_id}", response_model=FoodEntryOut)
def read(food_entry_id: int, db: Session = Depends(get_db)):
    entry = crud_food_entry.get_food_entry(db, food_entry_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Food Entry not found")
    return entry

@food_entry_router.put("/{food_entry_id}", response_model=FoodEntryOut)
def update(food_entry_id: int, food_entry_data: FoodEntryUpdate, db: Session = Depends(get_db)):
    entry = crud_food_entry.update_food_entry(db, food_entry_id, food_entry_data)
    if not entry:
        raise HTTPException(status_code=404, detail="Food Entry not found")
    return entry

@food_entry_router.delete("/{food_entry_id}", response_model=FoodEntryOut)
def delete(food_entry_id: int, db: Session = Depends(get_db)):
    entry = crud_food_entry.delete_food_entry(db, food_entry_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Food Entry not found")
    return entry
