import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

def get_db_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "food_tracker.db")

# SQLite database file (will be created automatically)
DATABASE_URL = f"sqlite:///{get_db_path()}"

# Create engine (connection to database)
engine = create_engine(DATABASE_URL, connect_args={
    "check_same_thread": False
})

# Session factory (for database operations later)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base class for your models
Base = declarative_base()
