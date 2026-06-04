from fastapi import APIRouter, Depends
from app.schemas import EvaluateRequest, EvaluateResponse
from app.auth_utils import get_current_user

router = APIRouter()

@router.post("/evaluate", response_model=EvaluateResponse)
def evaluate(request: EvaluateRequest, current_user: str = Depends(get_current_user)):
    return EvaluateResponse(
        result=f"Evaluation requested by {current_user}. ChatGPT integration coming in Stage 5."
    )