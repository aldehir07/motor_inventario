from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)

@router.get("")
def health():
    """
    Verifica que la API se encuentre disponible
    """

    return {
        "status": "ok"
    }