from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import health, colleges, admin, user_profiles
from database.database import Base, engine

# Create tables on startup if not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="College Design Programs API", version="0.1.0")

# CORS configuration for production deployment
import os

# Get allowed origins from environment variable or use defaults
allowed_origins = os.getenv('ALLOWED_ORIGINS', 'http://localhost:8501,http://localhost:3000').split(',')

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health.router, prefix="/api", tags=["health"]) 
app.include_router(colleges.router, prefix="/api/colleges", tags=["colleges"]) 
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])
app.include_router(user_profiles.router, prefix="/api/user-profiles", tags=["user-profiles"]) 


@app.get("/", tags=["health"]) 
async def root():
    return {"message": "College Design Programs API is running"}

@app.get("/health", tags=["health"])
async def health_check():
    """Health check endpoint for deployment platforms"""
    return {
        "status": "healthy",
        "timestamp": "2024-01-01T00:00:00Z",
        "version": "0.1.0"
    } 