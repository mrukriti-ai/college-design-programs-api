from sqlalchemy.orm import Session
from typing import List

from fastapi_app.database import models
from fastapi_app.api.schemas.college import CollegeSearchRequest

class CollegeService:
    @staticmethod
    def list_colleges(db: Session, limit: int = 50, offset: int = 0) -> List[models.College]:
        return (
            db.query(models.College)
            .order_by(models.College.name.asc())
            .offset(offset)
            .limit(limit)
            .all()
        )

    @staticmethod
    def get_college(db: Session, college_id: int) -> models.College | None:
        return db.query(models.College).filter(models.College.id == college_id).first()

    @staticmethod
    def search_colleges(db: Session, payload: CollegeSearchRequest) -> List[models.College]:
        q = db.query(models.College)

        if payload.program_type:
            q = q.filter(models.College.program_type == payload.program_type)

        # Budget filtering: include if any overlap between college tuition range and requested budget
        if payload.budget_range:
            if payload.budget_range == "Under 20k":
                q = q.filter(models.College.tuition_min <= 20000)
            elif payload.budget_range == "20k-40k":
                q = q.filter(models.College.tuition_min <= 40000, (models.College.tuition_max == None) | (models.College.tuition_max >= 20000))
            elif payload.budget_range == "40k-60k":
                q = q.filter(models.College.tuition_min <= 60000, (models.College.tuition_max == None) | (models.College.tuition_max >= 40000))
            elif payload.budget_range == "Over 60k":
                q = q.filter((models.College.tuition_max == None) | (models.College.tuition_max >= 60000))

        # Location filtering: simple country contains or continent group (basic mapping could be added later)
        if payload.location and payload.location != "Any":
            continent = payload.location
            if continent == "North America":
                q = q.filter(models.College.location_country.in_(["USA", "United States", "Canada", "Mexico"]))
            elif continent == "Europe":
                q = q.filter(models.College.location_country.in_(["UK", "United Kingdom", "Germany", "France", "Italy", "Spain", "Netherlands", "Sweden", "Denmark", "Finland", "Norway", "Belgium", "Portugal", "Switzerland", "Austria", "Poland", "Ireland"]))
            elif continent == "Asia":
                q = q.filter(models.College.location_country.in_(["India", "China", "Japan", "South Korea", "Singapore", "Hong Kong", "Taiwan", "Thailand", "Malaysia", "Indonesia", "Philippines", "Vietnam"]))
            elif continent == "Australia":
                q = q.filter(models.College.location_country.in_(["Australia", "New Zealand"]))

        return q.order_by(models.College.name.asc()).limit(200).all() 