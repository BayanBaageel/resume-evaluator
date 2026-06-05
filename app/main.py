from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, evaluate, admin
from app.database import create_db


app = FastAPI(title="Resume Evaluator API")

@app.on_event("startup")
def on_startup():
    create_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(evaluate.router, tags=["evaluate"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])

@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}