"""
Simplified FastAPI app for Render deployment
This version removes complex dependencies that might cause issues
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="College Design Programs API", version="0.1.0")

# CORS configuration
allowed_origins = os.getenv('ALLOWED_ORIGINS', '*').split(',')
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "College Design Programs API is running",
        "status": "healthy",
        "version": "0.1.0"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint for deployment platforms"""
    return {
        "status": "healthy",
        "timestamp": "2024-01-01T00:00:00Z",
        "version": "0.1.0",
        "service": "college-design-programs-api"
    }

@app.get("/api/colleges")
async def get_colleges():
    """Get sample colleges data"""
    return {
        "colleges": [
            {
                "id": 1,
                "name": "Art Institute of Chicago",
                "program": "Graphic Design",
                "location": "Chicago, IL",
                "country": "USA",
                "tuition": "$45,000",
                "duration": "4 years",
                "rating": 4.5
            },
            {
                "id": 2,
                "name": "Parsons School of Design",
                "program": "Fashion Design",
                "location": "New York, NY",
                "country": "USA",
                "tuition": "$52,000",
                "duration": "4 years",
                "rating": 4.8
            },
            {
                "id": 3,
                "name": "Rhode Island School of Design",
                "program": "Product Design",
                "location": "Providence, RI",
                "country": "USA",
                "tuition": "$48,000",
                "duration": "4 years",
                "rating": 4.7
            },
            {
                "id": 4,
                "name": "Central Saint Martins",
                "program": "Fashion Design",
                "location": "London",
                "country": "UK",
                "tuition": "£25,000",
                "duration": "3 years",
                "rating": 4.9
            },
            {
                "id": 5,
                "name": "Design Academy Eindhoven",
                "program": "Product Design",
                "location": "Eindhoven",
                "country": "Netherlands",
                "tuition": "€15,000",
                "duration": "4 years",
                "rating": 4.6
            }
        ]
    }

@app.get("/api/colleges/search")
async def search_colleges(
    program_type: str = None,
    location: str = None,
    budget_range: str = None,
    degree_level: str = None,
    limit: int = 50
):
    """Search colleges with filters"""
    # For now, return all colleges (filtering can be added later)
    colleges = [
        {
            "id": 1,
            "name": "Art Institute of Chicago",
            "program": "Graphic Design",
            "location": "Chicago, IL",
            "country": "USA",
            "tuition": "$45,000",
            "duration": "4 years",
            "rating": 4.5
        },
        {
            "id": 2,
            "name": "Parsons School of Design",
            "program": "Fashion Design",
            "location": "New York, NY",
            "country": "USA",
            "tuition": "$52,000",
            "duration": "4 years",
            "rating": 4.8
        },
        {
            "id": 3,
            "name": "Rhode Island School of Design",
            "program": "Product Design",
            "location": "Providence, RI",
            "country": "USA",
            "tuition": "$48,000",
            "duration": "4 years",
            "rating": 4.7
        },
        {
            "id": 4,
            "name": "Central Saint Martins",
            "program": "Fashion Design",
            "location": "London",
            "country": "UK",
            "tuition": "£25,000",
            "duration": "3 years",
            "rating": 4.9
        },
        {
            "id": 5,
            "name": "Design Academy Eindhoven",
            "program": "Product Design",
            "location": "Eindhoven",
            "country": "Netherlands",
            "tuition": "€15,000",
            "duration": "4 years",
            "rating": 4.6
        }
    ]
    
    # Simple filtering (can be enhanced later)
    if program_type and program_type != "Any":
        colleges = [c for c in colleges if program_type.lower() in c["program"].lower()]
    
    if location and location != "Any":
        colleges = [c for c in colleges if location.lower() in c["location"].lower()]
    
    return {"colleges": colleges[:limit]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
