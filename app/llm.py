import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def evaluate_resume(job_description: str, prompt: str, resume_text: str) -> str:
    system_message = (
        "You are an expert HR assistant. When given a job description and a resume, "
        "evaluate how well the candidate matches the requirements. "
        "Structure your response as: "
        "(1) Match Score (0-10), "
        "(2) Key Strengths, "
        "(3) Gaps, "
        "(4) Overall Recommendation."
    )

    user_message = f"""Job Description:
{job_description}

Resume:
{resume_text}
"""
    if prompt:
        user_message += f"\nAdditional Instructions: {prompt}"

    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ],
        max_tokens=1000,
    )

    return response.choices[0].message.content