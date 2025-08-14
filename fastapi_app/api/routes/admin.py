from fastapi import APIRouter, UploadFile, File, HTTPException, Header, Depends
from sqlalchemy.orm import Session
from typing import Optional

from database.database import get_db
from api.services.excel_service import ExcelImportService

router = APIRouter()

ADMIN_TOKEN_HEADER = "X-Admin-Token"


def require_admin(x_admin_token: Optional[str] = Header(None)):
    if not x_admin_token:
        raise HTTPException(status_code=401, detail="Missing admin token")
    # For MVP, accept any non-empty token or compare to env/config if desired
    return True


@router.post("/colleges/import-excel")
async def import_colleges_excel(
    file: UploadFile = File(...),
    _: bool = Depends(require_admin),
    db: Session = Depends(get_db),
):
    if not file.filename.endswith((".xlsx", ".xls")):
        raise HTTPException(status_code=400, detail="Only Excel files are supported (.xlsx/.xls)")

    try:
        report = ExcelImportService.import_excel(file, db)
        return {"status": "ok", "report": report}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/colleges/import-status")
async def import_status(db: Session = Depends(get_db)):
    # Minimal status for MVP – count rows
    from database.models import College
    count = db.query(College).count()
    return {"colleges_count": count} 