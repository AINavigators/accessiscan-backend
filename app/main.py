from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router

from app.db.session import create_db_and_tables #Change appropriately
from app.models.user import User
from app.models.inspection import Inspection
from app.models.detection import Detection
from app.models.report import Report
from app.models.image import Image  

app = FastAPI(
    title="AccessiScan API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change later for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}