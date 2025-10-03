from fastapi import APIRouter, Depends
from app.core.security import get_current_user, require_admin, require_teacher, require_student
from app.models.user import UserProfile

router = APIRouter()


@router.get("/dashboard")
async def get_dashboard(current_user: dict = Depends(get_current_user)):
    """
    Protected route - any authenticated user
    """
    return {
        "message": f"Welcome to your dashboard, {current_user['email']}!",
        "user": current_user,
        "access_level": "user"
    }


@router.get("/student/games")
async def get_student_games(current_user: dict = Depends(require_student)):
    """
    Protected route - requires student role or higher
    """
    return {
        "message": "Student games endpoint",
        "user": current_user,
        "games": [
            {"id": 1, "name": "Balance Scale Addition", "difficulty": "easy"},
            {"id": 2, "name": "Balance Scale Addition", "difficulty": "medium"},
            {"id": 3, "name": "Balance Scale Addition", "difficulty": "hard"}
        ]
    }


@router.get("/student/progress")
async def get_student_progress(current_user: dict = Depends(require_student)):
    """
    Protected route - student's game progress
    """
    return {
        "message": "Student progress endpoint",
        "user_id": current_user['uid'],
        "progress": {
            "games_played": 10,
            "accuracy": 85,
            "level": 3
        }
    }


@router.get("/teacher/students")
async def get_teacher_students(current_user: dict = Depends(require_teacher)):
    """
    Protected route - requires teacher role or higher
    """
    return {
        "message": "Teacher students endpoint",
        "teacher": current_user,
        "students": [
            {"id": "student1", "name": "John Doe", "progress": 75},
            {"id": "student2", "name": "Jane Smith", "progress": 90}
        ]
    }


@router.get("/teacher/assignments")
async def get_teacher_assignments(current_user: dict = Depends(require_teacher)):
    """
    Protected route - teacher's assignments
    """
    return {
        "message": "Teacher assignments endpoint",
        "teacher_id": current_user['uid'],
        "assignments": [
            {"id": 1, "title": "Addition Practice", "due_date": "2025-10-10"},
            {"id": 2, "title": "Advanced Addition", "due_date": "2025-10-15"}
        ]
    }


@router.get("/admin/users")
async def get_all_users(current_user: dict = Depends(require_admin)):
    """
    Protected route - requires admin role
    """
    return {
        "message": "Admin users endpoint",
        "admin": current_user,
        "users": [
            {"uid": "user1", "email": "user1@example.com", "role": "student"},
            {"uid": "user2", "email": "user2@example.com", "role": "teacher"},
            {"uid": "user3", "email": "user3@example.com", "role": "admin"}
        ]
    }


@router.get("/admin/stats")
async def get_system_stats(current_user: dict = Depends(require_admin)):
    """
    Protected route - admin system statistics
    """
    return {
        "message": "Admin statistics endpoint",
        "stats": {
            "total_users": 150,
            "total_students": 120,
            "total_teachers": 25,
            "total_admins": 5,
            "games_played_today": 340
        }
    }
