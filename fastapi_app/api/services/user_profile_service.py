"""
User Profile Service - Business logic for user profile operations
"""

from sqlalchemy.orm import Session
from typing import List, Optional
import json

from database import models
from api.schemas.user_profile import UserProfileCreate, UserProfileUpdate


class UserProfileService:
    @staticmethod
    def create_user_profile(db: Session, profile_data: UserProfileCreate) -> models.UserProfile:
        """Create a new user profile"""
        
        # Check if profile with this email already exists
        existing = db.query(models.UserProfile).filter(
            models.UserProfile.email == profile_data.email
        ).first()
        
        if existing:
            # Update existing profile
            existing.name = profile_data.name
            existing.education_level = profile_data.education_level
            existing.program_interest = profile_data.program_interest
            existing.budget_range = profile_data.budget_range
            existing.location_preference = profile_data.location_preference
            existing.degree_level = json.dumps(profile_data.degree_level) if profile_data.degree_level else None
            existing.include_international = "true" if profile_data.include_international else "false"
            db.commit()
            db.refresh(existing)
            return existing
        
        # Create new profile
        new_profile = models.UserProfile(
            name=profile_data.name,
            email=profile_data.email,
            education_level=profile_data.education_level,
            program_interest=profile_data.program_interest,
            budget_range=profile_data.budget_range,
            location_preference=profile_data.location_preference,
            degree_level=json.dumps(profile_data.degree_level) if profile_data.degree_level else None,
            include_international="true" if profile_data.include_international else "false"
        )
        
        db.add(new_profile)
        db.commit()
        db.refresh(new_profile)
        return new_profile

    @staticmethod
    def get_user_profile(db: Session, email: str) -> Optional[models.UserProfile]:
        """Get user profile by email"""
        return db.query(models.UserProfile).filter(
            models.UserProfile.email == email
        ).first()

    @staticmethod
    def get_user_profile_by_id(db: Session, profile_id: int) -> Optional[models.UserProfile]:
        """Get user profile by ID"""
        return db.query(models.UserProfile).filter(
            models.UserProfile.id == profile_id
        ).first()

    @staticmethod
    def list_user_profiles(db: Session, limit: int = 100, offset: int = 0) -> List[models.UserProfile]:
        """List all user profiles with pagination"""
        return db.query(models.UserProfile).order_by(
            models.UserProfile.created_at.desc()
        ).offset(offset).limit(limit).all()

    @staticmethod
    def update_user_profile(db: Session, email: str, profile_data: UserProfileUpdate) -> Optional[models.UserProfile]:
        """Update user profile"""
        profile = db.query(models.UserProfile).filter(
            models.UserProfile.email == email
        ).first()
        
        if not profile:
            return None
        
        # Update only provided fields
        if profile_data.name is not None:
            profile.name = profile_data.name
        if profile_data.education_level is not None:
            profile.education_level = profile_data.education_level
        if profile_data.program_interest is not None:
            profile.program_interest = profile_data.program_interest
        if profile_data.budget_range is not None:
            profile.budget_range = profile_data.budget_range
        if profile_data.location_preference is not None:
            profile.location_preference = profile_data.location_preference
        if profile_data.degree_level is not None:
            profile.degree_level = json.dumps(profile_data.degree_level)
        if profile_data.include_international is not None:
            profile.include_international = "true" if profile_data.include_international else "false"
        
        db.commit()
        db.refresh(profile)
        return profile

    @staticmethod
    def delete_user_profile(db: Session, email: str) -> bool:
        """Delete user profile"""
        profile = db.query(models.UserProfile).filter(
            models.UserProfile.email == email
        ).first()
        
        if not profile:
            return False
        
        db.delete(profile)
        db.commit()
        return True

