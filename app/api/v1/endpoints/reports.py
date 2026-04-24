from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_reports():
    return [{"id": 1, "title": "Accessibility Report"}]