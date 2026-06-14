from fastapi import APIRouter, Depends, File, Form, UploadFile, HTTPException
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
    if resume.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Please upload a valid PDF file.")

    try:
        file_content = await resume.read()
        resume_text = extract_text_from_pdf(file_content)
    except Exception:
        raise HTTPException(status_code=400, detail="Could not read the PDF. Please try a different file.")

    if not resume_text:
        raise HTTPException(status_code=400, detail="The PDF appears to be empty or unreadable. Please try a different file.")

    try:
        result = evaluate_resume(job_description, prompt, resume_text)
    except Exception:
        raise HTTPException(status_code=503, detail="AI service is currently unavailable. Please try again later.")

    return EvaluateResponse(result=result)