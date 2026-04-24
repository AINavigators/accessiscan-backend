from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_inspections():
    return [{"id": 1, "site": "Station A", "status": "draft"}]