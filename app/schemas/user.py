from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
