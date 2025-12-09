"""
User Profile schemas for request/response validation
"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime


class UserProfileCreate(BaseModel):
    """Schema for creating a user profile"""
    name: str = Field(..., min_length=1, max_length=200)
    email: EmailStr
    education_level: str = Field(..., min_length=1)
    program_interest: str = Field(..., min_length=1)
    budget_range: str = Field(..., min_length=1)
    location_preference: str = Field(..., min_length=1)
    degree_level: Optional[List[str]] = Field(default=None)
    include_international: Optional[bool] = Field(default=True)


class UserProfileResponse(BaseModel):
    """Schema for user profile response"""
    id: int
    name: str
    email: str
    education_level: str
    program_interest: str
    budget_range: str
    location_preference: str
    degree_level: Optional[str] = None
    include_international: Optional[bool] = None
    created_at: datetime

    class Config:
        from_attributes = True


class UserProfileUpdate(BaseModel):
    """Schema for updating a user profile"""
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    education_level: Optional[str] = None
    program_interest: Optional[str] = None
    budget_range: Optional[str] = None
    location_preference: Optional[str] = None
    degree_level: Optional[List[str]] = None
    include_international: Optional[bool] = None

