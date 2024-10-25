from fastapi import APIRouter

router = APIRouter()

@router.get("/matches/")
def get_matches():
    return {"message": "Список матчей еще не реализован"}
