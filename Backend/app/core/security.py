from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.firebase import verify_firebase_token, get_user_by_uid
from typing import Optional

security = HTTPBearer()


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Dependency to get current authenticated user from Firebase token
    """
    token = credentials.credentials

    # Verify Firebase token
    decoded_token = verify_firebase_token(token)

    if not decoded_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Get user information
    uid = decoded_token.get("uid")
    email = decoded_token.get("email")

    # Get custom claims (roles)
    custom_claims = decoded_token.get("custom_claims", {})
    role = custom_claims.get("role", "user")

    return {
        "uid": uid,
        "email": email,
        "role": role,
        "custom_claims": custom_claims
    }


async def require_role(required_role: str):
    """
    Dependency factory to check if user has required role
    """
    async def role_checker(current_user: dict = Depends(get_current_user)):
        user_role = current_user.get("role", "user")

        # Define role hierarchy
        role_hierarchy = {
            "admin": 3,
            "teacher": 2,
            "student": 1,
            "user": 0
        }

        user_level = role_hierarchy.get(user_role, 0)
        required_level = role_hierarchy.get(required_role, 0)

        if user_level < required_level:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Insufficient permissions. Required role: {required_role}"
            )

        return current_user

    return role_checker

# Specific role dependencies


async def require_admin(current_user: dict = Depends(get_current_user)):
    """Require admin role"""
    if current_user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user


async def require_teacher(current_user: dict = Depends(get_current_user)):
    """Require teacher role or higher"""
    role = current_user.get("role", "user")
    if role not in ["admin", "teacher"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Teacher access required"
        )
    return current_user


async def require_student(current_user: dict = Depends(get_current_user)):
    """Require student role or higher"""
    role = current_user.get("role", "user")
    if role not in ["admin", "teacher", "student"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Student access required"
        )
    return current_user
