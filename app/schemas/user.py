from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

class UserProfileBase(BaseModel):
    display_name: Optional[str] = None
    phone_number: Optional[str] = None
    total_eco_points: int = 0

class UserProfileCreate(UserProfileBase):
    pass

class UserProfileUpdate(BaseModel):
    display_name: Optional[str] = None
    phone_number: Optional[str] = None

class UserProfile(UserProfileBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True

class UserWithProfile(User):
    profile: Optional[UserProfile] = None

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
