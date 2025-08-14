from pydantic import BaseModel, Field
from typing import Optional

PROGRAM_TYPES = (
    "Graphic Design",
    "UX/UI",
    "Fashion",
    "Product Design",
    "Architecture",
    "Animation",
)

BUDGET_RANGES = (
    "Under 20k",
    "20k-40k",
    "40k-60k",
    "Over 60k",
)

LOCATIONS = (
    "North America",
    "Europe",
    "Asia",
    "Australia",
    "Any",
)


class CollegeSearchRequest(BaseModel):
    program_type: Optional[str] = Field(default=None)
    budget_range: Optional[str] = Field(default=None)
    location: Optional[str] = Field(default=None)


class CollegeResponse(BaseModel):
    id: int
    name: str
    location_city: str
    location_country: str
    program_name: str
    program_type: str
    degree_level: str
    tuition_min: float | None = None
    tuition_max: float | None = None
    application_deadline: Optional[str] = None
    program_description: Optional[str] = None
    admission_requirements: Optional[str] = None
    contact_email: Optional[str] = None
    website_url: Optional[str] = None

    class Config:
        from_attributes = True 