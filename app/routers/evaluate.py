from fastapi import APIRouter, Depends, File, Form, UploadFile
from app.schemas import EvaluateResponse
from app.auth_utils import get_current_user
from app.pdf_utils import extract_text_from_pdf
from app.llm import evaluate_resume

router = APIRouter()

@router.post("/evaluate", response_model=EvaluateResponse)
async def evaluate(
    job_description: str = Form(...),
    prompt: str = Form(""),
    resume: UploadFile = File(...),
    current_user: str = Depends(get_current_user),
):
    file_content = await resume.read()
    resume_text = extract_text_from_pdf(file_content)
    result = evaluate_resume(job_description, prompt, resume_text)
    return EvaluateResponse(result=result)