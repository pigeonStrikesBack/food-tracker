from datetime import datetime
from pydantic import BaseModel
from app.schemas.user import UserOut
from app.schemas.food import FoodOut
from typing import Optional


class FoodEntryBase(BaseModel):
    quantity_grams: int
    date: Optional[datetime] = None
    user_id: int
    food_id: int

class FoodEntryCreate(FoodEntryBase):
    pass

class FoodEntryUpdate(BaseModel):
    quantity_grams: int | None = None
    date: datetime | None = None
    user_id: int | None = None
    food_id: int | None = None

class FoodEntryOut(BaseModel):
    id: int
    quantity_grams: int
    date: datetime
    user: UserOut
    food: FoodOut

    class Config:
        orm_mode = True
