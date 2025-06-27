from app.database import SessionLocal
from app.models.models import User

# Create a new DB session
db = SessionLocal()

# Create a new user
new_user = User(username="testuser", email="test@mypatience.cum")

# Add + save
db.add(new_user)
db.commit()

print("✔️ User Added!")