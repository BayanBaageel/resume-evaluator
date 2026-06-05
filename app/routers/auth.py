from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel import Session, select
from app.schemas import RegisterRequest, LoginRequest, UserResponse, TokenResponse
from app.auth_utils import hash_password, verify_password, create_access_token, get_current_user
from app.database import get_session
from app.models import User

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(request: RegisterRequest, session: Session = Depends(get_session)):
    existing = session.exec(select(User).where(User.email == request.email)).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    hashed = hash_password(request.password)
    user = User(email=request.email, hashed_password=hashed, role="user")
    session.add(user)
    session.commit()
    session.refresh(user)
    return UserResponse(email=user.email, role=user.role)

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.email == request.email)).first()
    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    token = create_access_token(request.email)
    return TokenResponse(access_token=token)

@router.get("/me", response_model=UserResponse)
def get_me(current_user: str = Depends(get_current_user), session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.email == current_user)).first()
    return UserResponse(email=user.email, role=user.role)