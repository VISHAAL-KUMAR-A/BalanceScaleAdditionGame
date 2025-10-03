from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    display_name: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    uid: str
    role: str = "user"
    created_at: Optional[datetime] = None
    email_verified: bool = False


class UserRoleUpdate(BaseModel):
    role: str


class TokenResponse(BaseModel):
    token: str
    user: UserResponse


class UserProfile(BaseModel):
    uid: str
    email: str
    display_name: Optional[str] = None
    role: str
    custom_claims: Optional[dict] = {}
