from sqlalchemy import Column, Integer, String, Float, Text, DateTime, Date, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import relationship
from .database import Base

class College(Base):
    __tablename__ = "colleges"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    location_city = Column(String, nullable=False)
    location_country = Column(String, nullable=False, index=True)
    program_name = Column(String, nullable=False)
    program_type = Column(String, nullable=False, index=True)
    degree_level = Column(String, nullable=False)
    tuition_min = Column(Float)
    tuition_max = Column(Float)
    application_deadline = Column(Date, nullable=True)
    program_description = Column(Text, nullable=True)
    admission_requirements = Column(Text, nullable=True)
    contact_email = Column(String, nullable=True)
    website_url = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.current_timestamp())
    updated_at = Column(DateTime, onupdate=func.current_timestamp())

    __table_args__ = (
        UniqueConstraint("name", "program_name", "location_country", name="uq_college_program_country"),
    )

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    education_level = Column(String, nullable=False)
    program_interest = Column(String, nullable=False)
    budget_range = Column(String, nullable=False)
    location_preference = Column(String, nullable=False)
    degree_level = Column(Text, nullable=True)  # JSON string for list of degree levels
    include_international = Column(String, nullable=True, default="true")  # Store as string
    created_at = Column(DateTime, server_default=func.current_timestamp())

class UserFavorite(Base):
    __tablename__ = "user_favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String, nullable=False, index=True)
    college_id = Column(Integer, ForeignKey("colleges.id"), nullable=False)
    created_at = Column(DateTime, server_default=func.current_timestamp())

    college = relationship("College")

    __table_args__ = (
        UniqueConstraint("user_email", "college_id", name="uq_favorite_user_college"),
    ) 