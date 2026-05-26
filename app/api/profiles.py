from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User, UserProfile
from app.schemas.user import UserProfile as UserProfileSchema, UserProfileUpdate, UserWithProfile
from app.core.config import settings

router = APIRouter(prefix="/api/v1/users", tags=["profiles"])

@router.get("/{user_id}/profile", response_model=UserProfileSchema)
async def get_user_profile(user_id: int, db: Session = Depends(get_db)):
    """
    Get the profile of a logged-in user.
    Returns user profile with display_name, phone_number, and total_eco_points.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    profile = db.query(UserProfile).filter(UserProfile.user_id == user_id).first()
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User profile not found"
        )
    
    return profile

@router.put("/{user_id}/profile", response_model=UserProfileSchema)
async def update_user_profile(
    user_id: int,
    profile_update: UserProfileUpdate,
    db: Session = Depends(get_db)
):
    """
    Update the user's profile information (display_name, phone_number).
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    profile = db.query(UserProfile).filter(UserProfile.user_id == user_id).first()
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User profile not found"
        )
    
    # Update only provided fields
    if profile_update.display_name is not None:
        profile.display_name = profile_update.display_name
    if profile_update.phone_number is not None:
        profile.phone_number = profile_update.phone_number
    
    db.commit()
    db.refresh(profile)
    return profile

@router.patch("/{user_id}/profile", response_model=UserProfileSchema)
async def patch_user_profile(
    user_id: int,
    profile_update: UserProfileUpdate,
    db: Session = Depends(get_db)
):
    """
    Partially update the user's profile information.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    profile = db.query(UserProfile).filter(UserProfile.user_id == user_id).first()
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User profile not found"
        )
    
    # Update only provided fields
    update_data = profile_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(profile, field, value)
    
    db.commit()
    db.refresh(profile)
    return profile

@router.get("/{user_id}", response_model=UserWithProfile)
async def get_user_with_profile(user_id: int, db: Session = Depends(get_db)):
    """
    Get user information along with their profile.
    Returns response like: "Welcome back, [Display Name]! You have 50 points."
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user
