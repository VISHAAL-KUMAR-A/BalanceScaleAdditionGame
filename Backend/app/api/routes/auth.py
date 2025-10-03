from fastapi import APIRouter, HTTPException, status, Depends
from app.models.user import UserResponse, UserProfile, UserRoleUpdate
from app.core.security import get_current_user, require_admin
from app.core.firebase import get_user_by_uid, set_custom_user_claims

router = APIRouter()


@router.post("/verify-token", response_model=UserProfile)
async def verify_token(current_user: dict = Depends(get_current_user)):
    """
    Verify Firebase token and return user profile
    This endpoint is called by frontend to validate session
    """
    return UserProfile(**current_user)


@router.get("/me", response_model=UserProfile)
async def get_current_user_profile(current_user: dict = Depends(get_current_user)):
    """
    Get current authenticated user profile
    """
    return UserProfile(**current_user)


@router.post("/set-role/{uid}")
async def set_user_role(
    uid: str,
    role_update: UserRoleUpdate,
    current_user: dict = Depends(require_admin)
):
    """
    Set custom role for a user (Admin only)
    Available roles: user, student, teacher, admin
    """
    valid_roles = ["user", "student", "teacher", "admin"]

    if role_update.role not in valid_roles:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid role. Must be one of: {', '.join(valid_roles)}"
        )

    # Get user to verify they exist
    user = get_user_by_uid(uid)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    # Set custom claims
    success = set_custom_user_claims(uid, {"role": role_update.role})

    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to set user role"
        )

    return {
        "message": f"Role '{role_update.role}' set successfully for user {uid}",
        "uid": uid,
        "role": role_update.role
    }


@router.get("/users/{uid}")
async def get_user_info(
    uid: str,
    current_user: dict = Depends(require_admin)
):
    """
    Get user information by UID (Admin only)
    """
    user = get_user_by_uid(uid)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return {
        "uid": user.uid,
        "email": user.email,
        "display_name": user.display_name,
        "email_verified": user.email_verified,
        "disabled": user.disabled,
        "custom_claims": user.custom_claims
    }
