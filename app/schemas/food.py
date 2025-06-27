from pydantic import BaseModel

class FoodBase(BaseModel):
    name: str
    calories_per_100g: int

class FoodCreate(FoodBase):
    pass

class FoodUpdate(BaseModel):
    name: str | None = None
    calories_per_100g: int | None = None

class FoodOut(FoodBase):
    id: int

    class Config:
        orm_mode = True
