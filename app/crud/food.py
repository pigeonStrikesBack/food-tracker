# app/crud/food.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from app.models.models import Food
from app.schemas.food import FoodCreate, FoodUpdate

def create_food(db: Session, food: FoodCreate):
    existing_food = db.query(Food).filter(Food.name == food.name).first()
    if existing_food:
        raise ValueError("Food with this name already exists")
    db_food = Food(
        name=food.name,
        calories_per_100g=food.calories_per_100g
    )
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food

def get_food(db: Session, food_id: int):
    return db.query(Food).filter(Food.id == food_id).first()

def get_foods(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Food).offset(skip).limit(limit).all()

def update_food(db: Session, food_id: int, food_data: FoodUpdate):
    food = db.query(Food).filter(Food.id == food_id).first()
    if not food:
        return None
    if food_data.name is not None:
        food.name = food_data.name
    if food_data.calories_per_100g is not None:
        food.calories_per_100g = food_data.calories_per_100g
    db.commit()
    db.refresh(food)
    return food

def delete_food(db: Session, food_id: int):
    food = db.query(Food).filter(Food.id == food_id).first()
    if not food:
        return None
    db.delete(food)
    db.commit()
    return food
