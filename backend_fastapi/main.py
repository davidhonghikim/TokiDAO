from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.core.db import mongo_db_connection # Added import
from app.core.config import settings # Added import

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="TokiDAO API",
    description="API for the TokiDAO project - a gamified plant and mushroom database.",
    version="0.1.0"
)

@app.on_event("startup")
async def startup_event():
    print("TokiDAO API starting up...")
    await mongo_db_connection.connect_to_mongo() # Integrated DB connection
    if settings.MONGODB_URI:
        print(f"MongoDB URI (from settings): {settings.MONGODB_URI[:20]}... (truncated for display)")
    else:
        print("MONGODB_URI not found in settings.")
    # print(f"Secret Key (from settings): {settings.SECRET_KEY[:10]}... (truncated for display)")

@app.on_event("shutdown")
async def shutdown_event():
    await mongo_db_connection.close_mongo_connection() # Integrated DB close
    print("TokiDAO API shutting down...")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the TokiDAO API!"}

@app.get("/health", tags=["Health Check"])
async def health_check():
    return {"status": "healthy"}

# Placeholder for future API routers
# from app.api.v1 import api_router as api_v1_router
# app.include_router(api_v1_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    # This is for direct execution, e.g., debugging. 
    # For production, use a process manager like Gunicorn with Uvicorn workers.
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
