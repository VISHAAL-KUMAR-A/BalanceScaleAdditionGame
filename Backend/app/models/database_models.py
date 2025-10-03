from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, Float, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

class UserRole(str, enum.Enum):
    USER = "user"
    STUDENT = "student"
    TEACHER = "teacher"
    ADMIN = "admin"

class AuthProvider(str, enum.Enum):
    EMAIL = "email"
    GOOGLE = "google"

class DifficultyLevel(str, enum.Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    display_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=True)  # Null for Google users
    role = Column(Enum(UserRole), default=UserRole.USER, nullable=False)
    auth_provider = Column(Enum(AuthProvider), default=AuthProvider.EMAIL, nullable=False)
    firebase_uid = Column(String, unique=True, nullable=True, index=True)  # For Google users
    is_active = Column(Boolean, default=True, nullable=False)
    email_verified = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    game_sessions = relationship("GameSession", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User {self.email}>"

class GameSession(Base):
    __tablename__ = "game_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    difficulty = Column(Enum(DifficultyLevel), nullable=False)
    target_number = Column(Integer, nullable=False)
    user_answer = Column(JSON, nullable=True)  # Stores array of addends
    is_correct = Column(Boolean, nullable=False)
    attempts = Column(Integer, default=1)
    time_spent_seconds = Column(Integer, nullable=True)
    score = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    user = relationship("User", back_populates="game_sessions")

    def __repr__(self):
        return f"<GameSession {self.id} - User {self.user_id}>"

