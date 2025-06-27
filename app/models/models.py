
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    # relationships
    food_entries = relationship("FoodEntry", back_populates="user")

class Food(Base):
    __tablename__ = "foods"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    calories_per_100g = Column(Integer, nullable=False)

    # relationships
    food_entries = relationship("FoodEntry", back_populates="food")

class FoodEntry(Base):
    __tablename__ = "food_entries"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    food_id = Column(Integer, ForeignKey("foods.id"), nullable=False)
    quantity_grams = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)

    # relationships
    user = relationship("User", back_populates="food_entries")
    food = relationship("Food", back_populates="food_entries")



