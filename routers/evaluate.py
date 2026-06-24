from fastapi import APIRouter, Depends

from auth_utils import get_current_user
from schemas import EvaluateRequest, EvaluateResponse

router = APIRouter()


@router.post("/evaluate", response_model=EvaluateResponse)
def evaluate(request: EvaluateRequest, current_user: str = Depends(get_current_user)):
    return EvaluateResponse(
        result="Evaluation requested by "
        + current_user
        + ". ChatGPT integration coming in Stage 5.")
