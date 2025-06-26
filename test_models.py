from app.models.models import User
from app.database import engine, Base

def test_user_model():
    # create all tables
    Base.metadata.create_all(bind=engine)
    print("✅ User model created successfully!")
    print("✅ Database tables created!")

if __name__ == "__main__":
    test_user_model()