from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import NoResultFound
from app.models.models import FoodEntry
from app.schemas.food_entry import FoodEntryCreate, FoodEntryUpdate
from datetime import datetime

def create_food_entry(db: Session, food_entry: FoodEntryCreate):
    db_food_entry = FoodEntry(
        quantity_grams=food_entry.quantity_grams,
        date=food_entry.date or datetime.now(),
        user_id=food_entry.user_id,
        food_id=food_entry.food_id
    )
    db.add(db_food_entry)
    db.commit()
    db.refresh(db_food_entry)
    return (
        db.query(FoodEntry)
        .options(joinedload(FoodEntry.user), joinedload(FoodEntry.food))
        .filter(FoodEntry.id == db_food_entry.id)
        .first()
    )

def get_food_entry(db: Session, food_entry_id: int):
    return (
        db.query(FoodEntry)
        .options(joinedload(FoodEntry.user), joinedload(FoodEntry.food))
        .filter(FoodEntry.id == food_entry_id)
        .first()
    )

def get_food_entries(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(FoodEntry)
        .options(joinedload(FoodEntry.user), joinedload(FoodEntry.food))
        .offset(skip)
        .limit(limit)
        .all()
    )

def update_food_entry(db: Session, food_entry_id: int, food_entry_data: FoodEntryUpdate):
    food_entry = db.query(FoodEntry).filter(FoodEntry.id == food_entry_id).first()
    if not food_entry:
        return None
    if food_entry_data.quantity_grams is not None:
        food_entry.quantity_grams = food_entry_data.quantity_grams
    if food_entry_data.date is not None:
        food_entry.date = food_entry_data.date
    if food_entry_data.user_id is not None:
        food_entry.user_id = food_entry_data.user_id
    if food_entry_data.food_id is not None:
        food_entry.food_id = food_entry_data.food_id
    
    db.commit()
    db.refresh(food_entry)
    return (
        db.query(FoodEntry)
        .options(joinedload(FoodEntry.user), joinedload(FoodEntry.food))
        .filter(FoodEntry.id == food_entry.id)
        .first()
    )

def delete_food_entry(db: Session, food_entry_id: int):
    food_entry = (
        db.query(FoodEntry)
        .options(joinedload(FoodEntry.user), joinedload(FoodEntry.food))
        .filter(FoodEntry.id == food_entry_id)
        .first()
    )
    if not food_entry:
        return None
    db.delete(food_entry)
    db.commit()
    return food_entry
