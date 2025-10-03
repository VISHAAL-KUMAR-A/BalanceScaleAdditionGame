from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import datetime
from enum import Enum

class DifficultyLevel(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

class GameConfigRequest(BaseModel):
    difficulty: DifficultyLevel

class GameConfigResponse(BaseModel):
    target_number: int
    difficulty: DifficultyLevel
    min_value: int
    max_value: int
    max_addends: int
    hints_enabled: bool

class SubmitAnswerRequest(BaseModel):
    target_number: int
    user_answer: List[int] = Field(..., min_items=1, max_items=10)
    difficulty: DifficultyLevel
    time_spent_seconds: Optional[int] = None

    @validator('user_answer')
    def validate_answer(cls, v):
        if not all(isinstance(x, int) and x > 0 for x in v):
            raise ValueError('All addends must be positive integers')
        return v

class SubmitAnswerResponse(BaseModel):
    is_correct: bool
    user_sum: int
    target_number: int
    difference: int
    feedback: str
    score: int
    session_id: int

class GameProgressResponse(BaseModel):
    total_games: int
    correct_games: int
    accuracy_percentage: float
    total_score: int
    average_time_seconds: float
    difficulty_stats: dict
    recent_sessions: List[dict]

class GameSessionResponse(BaseModel):
    id: int
    difficulty: str
    target_number: int
    user_answer: Optional[List[int]]
    is_correct: bool
    attempts: int
    time_spent_seconds: Optional[int]
    score: int
    created_at: datetime

    class Config:
        from_attributes = True

