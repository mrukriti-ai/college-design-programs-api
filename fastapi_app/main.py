from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi_app.api.routes import health, colleges, admin
from fastapi_app.database.database import Base, engine

# Create tables on startup if not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="College Design Programs API", version="0.1.0")

# CORS for Streamlit (default localhost:8501)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health.router, prefix="/api", tags=["health"]) 
app.include_router(colleges.router, prefix="/api/colleges", tags=["colleges"]) 
app.include_router(admin.router, prefix="/api/admin", tags=["admin"]) 


@app.get("/", tags=["health"]) 
async def root():
    return {"message": "College Design Programs API is running"} 