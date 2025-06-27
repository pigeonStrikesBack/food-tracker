from sqlalchemy import inspect
from app.models.models import User
from app.database import engine, Base

def test_database_setup():
    """Test that all models create tables correctly"""
    Base.metadata.create_all(bind=engine)
    
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    
    expected_tables = ["users", "foods", "food_entries"]  # Add "foods", "food_entries" later
    
    for table in expected_tables:
        assert table in tables
        print(f"✅ {table} table created successfully!")

if __name__ == "__main__":
    test_database_setup()