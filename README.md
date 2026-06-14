# Resume Evaluator

A full-stack web application that evaluates resumes against job descriptions using AI.

## Project Structure

This repository contains the complete Resume Evaluator project across multiple branches:

| Branch | Description |
|--------|-------------|
| `main` | Stage 1 — Static HTML/CSS/JS prototype |
| `stage-2` | Stage 2–4 & 6 — React frontend with authentication and API integration |
| `stage-3` | Stage 3–5 & 6 — FastAPI backend with SQLite database and OpenAI integration |

## Tech Stack

**Frontend:** React, Vite, React Router, Axios  
**Backend:** FastAPI, SQLModel, SQLite, JWT Authentication  
**AI:** OpenAI GPT-4o-mini, pypdf  

## Features

- User registration and login with JWT authentication
- PDF resume upload and text extraction
- AI-powered resume evaluation against job descriptions
- Admin panel for user management
- Protected routes

## How to Run

**Backend:**
```bash
cd resume-evaluator-backend
source .venv/Scripts/activate
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd resume-evaluator-react
npm install
npm run dev
```
