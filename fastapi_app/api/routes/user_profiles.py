"""
User Profile API Routes
Handles user profile creation, retrieval, and management
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from database.database import get_db
from api.schemas.user_profile import UserProfileCreate, UserProfileResponse, UserProfileUpdate
from api.services.user_profile_service import UserProfileService

router = APIRouter()


@router.post("/", response_model=UserProfileResponse, status_code=201)
async def create_user_profile(
    profile_data: UserProfileCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new user profile or update existing one
    
    If a profile with the same email exists, it will be updated.
    """
    profile = UserProfileService.create_user_profile(db, profile_data)
    return profile


@router.get("/", response_model=List[UserProfileResponse])
async def list_user_profiles(
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    """List all user profiles with pagination"""
    profiles = UserProfileService.list_user_profiles(db, limit=limit, offset=offset)
    return profiles


@router.get("/{email}", response_model=UserProfileResponse)
async def get_user_profile(
    email: str,
    db: Session = Depends(get_db)
):
    """Get user profile by email"""
    profile = UserProfileService.get_user_profile(db, email)
    if not profile:
        raise HTTPException(status_code=404, detail="User profile not found")
    return profile


@router.get("/id/{profile_id}", response_model=UserProfileResponse)
async def get_user_profile_by_id(
    profile_id: int,
    db: Session = Depends(get_db)
):
    """Get user profile by ID"""
    profile = UserProfileService.get_user_profile_by_id(db, profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="User profile not found")
    return profile


@router.put("/{email}", response_model=UserProfileResponse)
async def update_user_profile(
    email: str,
    profile_data: UserProfileUpdate,
    db: Session = Depends(get_db)
):
    """Update user profile"""
    profile = UserProfileService.update_user_profile(db, email, profile_data)
    if not profile:
        raise HTTPException(status_code=404, detail="User profile not found")
    return profile


@router.delete("/{email}", status_code=204)
async def delete_user_profile(
    email: str,
    db: Session = Depends(get_db)
):
    """Delete user profile"""
    success = UserProfileService.delete_user_profile(db, email)
    if not success:
        raise HTTPException(status_code=404, detail="User profile not found")
    return None

