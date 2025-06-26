# Food Tracker - Sprint 1: Database Models

## 🎯 Sprint Goal
Create the core SQLAlchemy models for your food tracking application. This is your foundation - everything else builds on this.

## 📁 Project Structure to Create
```
food_tracker/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── models.py        ← YOUR MODELS GO HERE
│   └── database.py          ← Database connection setup
├── requirements.txt         ← List your dependencies
└── test_models.py          ← Test your models work
```

## 🛠️ Setup Instructions

### 1. Create Virtual Environment
```bash
# Create virtual environment
python -m venv food_tracker_env

# Activate it (Windows)
food_tracker_env\Scripts\activate

# Activate it (Mac/Linux)
source food_tracker_env/bin/activate
```

### 2. Install Dependencies
```bash
pip install sqlalchemy
pip freeze > requirements.txt
```

### 3. Create Project Structure
Create all the folders and `__init__.py` files as shown above.

## 📊 Models to Implement

You need to create **3 SQLAlchemy models** that represent these SQL tables:

### User Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
```

### Food Table (Global - Shared by all users)
```sql
CREATE TABLE foods (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    calories_per_100g INTEGER NOT NULL
);
```

### Food Entries Table (User's tracking log)
```sql
CREATE TABLE food_entries (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    food_id INTEGER NOT NULL,
    quantity_grams INTEGER NOT NULL,
    date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (food_id) REFERENCES foods(id)
);
```

## 🔗 Relationships to Implement

- **User** ↔ **FoodEntry**: One-to-Many (one user has many food entries)
- **Food** ↔ **FoodEntry**: One-to-Many (one food appears in many food entries)
- **FoodEntry** connects User and Food with additional data (quantity, date)

## ✅ Success Criteria

Your sprint is complete when:

- [ ] All three models are defined in `app/models/models.py`
- [ ] Models have proper SQLAlchemy relationships
- [ ] Database connection is set up in `app/database.py`
- [ ] You can import your models without errors
- [ ] You can create database tables from your models
- [ ] You understand what each relationship does

## 🧪 Testing Your Work

Create a simple `test_models.py` file to verify your models work:

```python
# This should run without errors when your models are correct
from app.models.models import User, Food, FoodEntry
from app.database import engine, Base

# Create all tables
Base.metadata.create_all(bind=engine)
print("✅ Models created successfully!")
```

## 📚 Key Concepts to Research

Before coding, make sure you understand:
- What is `declarative_base()` in SQLAlchemy?
- Difference between `ForeignKey()` and `relationship()`
- What does `back_populates` do?
- SQLAlchemy Column types (Integer, String, Date)

## 🚫 What NOT to Include Yet

- Password handling (too complex for now)
- Data validation (Pydantic comes later)
- API endpoints (FastAPI comes later)
- Authentication (later sprint)

## 🎓 Learning Objectives

By completing this sprint, you'll understand:
- How Python classes become database tables
- Foreign key relationships in ORMs
- Basic project structure for Python applications
- Foundation concepts for building APIs

## 📝 Code Review Checklist

When you're ready for review, make sure:
- Your code is readable and well-commented
- You can explain what each model represents
- You understand the relationships between models
- Your project structure matches the requirements
- You can run your test script successfully

## 🚀 Next Steps (After Code Review)

After this sprint, we'll move on to:
- Setting up FastAPI
- Creating API endpoints
- Adding CRUD operations
- Implementing authentication

---

**Remember**: Quality over speed. Take time to understand each concept. This foundation supports your entire application!

**Ready to code? Stop reading, start building! 💪**