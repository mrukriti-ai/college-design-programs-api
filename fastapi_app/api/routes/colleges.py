from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from sqlalchemy.orm import Session

from database.database import get_db
from api.schemas.college import CollegeSearchRequest, CollegeResponse
from api.services.college_service import CollegeService

router = APIRouter()

@router.get("/", response_model=List[CollegeResponse])
async def list_colleges(
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    return CollegeService.list_colleges(db, limit=limit, offset=offset)


@router.get("/{college_id}", response_model=CollegeResponse)
async def get_college(college_id: int, db: Session = Depends(get_db)):
    college = CollegeService.get_college(db, college_id)
    if not college:
        raise HTTPException(status_code=404, detail="College not found")
    return college


@router.post("/search", response_model=List[CollegeResponse])
async def search_colleges(payload: CollegeSearchRequest, db: Session = Depends(get_db)):
    return CollegeService.search_colleges(db, payload) 