from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.security_db import get_current_user_from_token
from app.core.database import get_db
from app.models.database_models import User, GameSession, DifficultyLevel
from app.models.game_schemas import (
    GameConfigRequest,
    GameConfigResponse,
    SubmitAnswerRequest,
    SubmitAnswerResponse,
    GameProgressResponse,
    GameSessionResponse
)
import random
from typing import List

router = APIRouter()

def generate_game_config(difficulty: DifficultyLevel) -> dict:
    """Generate game configuration based on difficulty level"""
    configs = {
        DifficultyLevel.EASY: {
            "min_value": 1,
            "max_value": 10,
            "target_range": (5, 20),
            "max_addends": 3,
            "hints_enabled": True
        },
        DifficultyLevel.MEDIUM: {
            "min_value": 1,
            "max_value": 20,
            "target_range": (10, 50),
            "max_addends": 4,
            "hints_enabled": True
        },
        DifficultyLevel.HARD: {
            "min_value": 1,
            "max_value": 50,
            "target_range": (20, 100),
            "max_addends": 5,
            "hints_enabled": False
        }
    }
    
    config = configs[difficulty]
    target_number = random.randint(*config["target_range"])
    
    return {
        "target_number": target_number,
        "difficulty": difficulty,
        "min_value": config["min_value"],
        "max_value": config["max_value"],
        "max_addends": config["max_addends"],
        "hints_enabled": config["hints_enabled"]
    }

def calculate_score(is_correct: bool, difficulty: DifficultyLevel, time_spent: int = None, attempts: int = 1) -> int:
    """Calculate score based on correctness, difficulty, time, and attempts"""
    if not is_correct:
        return 0
    
    base_scores = {
        DifficultyLevel.EASY: 10,
        DifficultyLevel.MEDIUM: 20,
        DifficultyLevel.HARD: 30
    }
    
    score = base_scores[difficulty]
    
    # Bonus for speed (if completed in under 30 seconds)
    if time_spent and time_spent < 30:
        score += 5
    
    # Penalty for multiple attempts
    score = max(score - (attempts - 1) * 2, 1)
    
    return score

@router.post("/config", response_model=GameConfigResponse)
async def get_game_config(
    request: GameConfigRequest,
    current_user: User = Depends(get_current_user_from_token)
):
    """
    Generate a new game configuration based on difficulty level.
    Returns target number and game parameters.
    """
    config = generate_game_config(request.difficulty)
    return config

@router.post("/submit", response_model=SubmitAnswerResponse)
async def submit_answer(
    request: SubmitAnswerRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token)
):
    """
    Submit an answer for validation and save game session.
    Returns feedback and score.
    """
    user_sum = sum(request.user_answer)
    is_correct = user_sum == request.target_number
    difference = user_sum - request.target_number
    
    # Generate feedback
    if is_correct:
        feedback = "Perfect! You balanced the scale! 🎉"
    elif abs(difference) <= 2:
        feedback = "So close! Try adjusting by a small amount." if difference > 0 else "Almost there! Add a bit more."
    elif difference > 0:
        feedback = f"Too heavy! Your sum is {abs(difference)} more than the target. Remove some weight."
    else:
        feedback = f"Too light! Your sum is {abs(difference)} less than the target. Add more weight."
    
    # Calculate score
    score = calculate_score(
        is_correct,
        request.difficulty,
        request.time_spent_seconds,
        1  # Default to 1 attempt for now
    )
    
    # Save game session to database
    game_session = GameSession(
        user_id=current_user.id,
        difficulty=request.difficulty,
        target_number=request.target_number,
        user_answer=request.user_answer,
        is_correct=is_correct,
        attempts=1,
        time_spent_seconds=request.time_spent_seconds,
        score=score
    )
    
    db.add(game_session)
    db.commit()
    db.refresh(game_session)
    
    return {
        "is_correct": is_correct,
        "user_sum": user_sum,
        "target_number": request.target_number,
        "difference": difference,
        "feedback": feedback,
        "score": score,
        "session_id": game_session.id
    }

@router.get("/progress", response_model=GameProgressResponse)
async def get_progress(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token)
):
    """
    Get user's game progress and statistics.
    """
    # Get all sessions for the user
    sessions = db.query(GameSession).filter(
        GameSession.user_id == current_user.id
    ).all()
    
    if not sessions:
        return {
            "total_games": 0,
            "correct_games": 0,
            "accuracy_percentage": 0.0,
            "total_score": 0,
            "average_time_seconds": 0.0,
            "difficulty_stats": {
                "easy": {"played": 0, "correct": 0, "accuracy": 0.0},
                "medium": {"played": 0, "correct": 0, "accuracy": 0.0},
                "hard": {"played": 0, "correct": 0, "accuracy": 0.0}
            },
            "recent_sessions": []
        }
    
    total_games = len(sessions)
    correct_games = sum(1 for s in sessions if s.is_correct)
    total_score = sum(s.score for s in sessions)
    
    # Calculate average time (only for sessions with time data)
    times = [s.time_spent_seconds for s in sessions if s.time_spent_seconds]
    average_time = sum(times) / len(times) if times else 0.0
    
    # Difficulty stats
    difficulty_stats = {}
    for difficulty in ["easy", "medium", "hard"]:
        diff_sessions = [s for s in sessions if s.difficulty.value == difficulty]
        diff_correct = sum(1 for s in diff_sessions if s.is_correct)
        difficulty_stats[difficulty] = {
            "played": len(diff_sessions),
            "correct": diff_correct,
            "accuracy": (diff_correct / len(diff_sessions) * 100) if diff_sessions else 0.0
        }
    
    # Recent sessions (last 5)
    recent = sorted(sessions, key=lambda x: x.created_at, reverse=True)[:5]
    recent_sessions = [
        {
            "id": s.id,
            "difficulty": s.difficulty.value,
            "target_number": s.target_number,
            "is_correct": s.is_correct,
            "score": s.score,
            "created_at": s.created_at.isoformat()
        }
        for s in recent
    ]
    
    return {
        "total_games": total_games,
        "correct_games": correct_games,
        "accuracy_percentage": (correct_games / total_games * 100) if total_games > 0 else 0.0,
        "total_score": total_score,
        "average_time_seconds": average_time,
        "difficulty_stats": difficulty_stats,
        "recent_sessions": recent_sessions
    }

@router.get("/history", response_model=List[GameSessionResponse])
async def get_game_history(
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token)
):
    """
    Get user's game history (recent sessions).
    """
    sessions = db.query(GameSession).filter(
        GameSession.user_id == current_user.id
    ).order_by(GameSession.created_at.desc()).limit(limit).all()
    
    return sessions

