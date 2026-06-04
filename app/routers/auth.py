from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas import RegisterRequest, LoginRequest, UserResponse, TokenResponse
from app.auth_utils import hash_password, verify_password, create_access_token, get_current_user
from app import store

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(request: RegisterRequest):
    if request.email in store.users:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    hashed = hash_password(request.password)
    store.users[request.email] = {
        "email": request.email,
        "hashed_password": hashed,
        "role": "user"
    }
    return UserResponse(email=request.email, role="user")

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest):
    user = store.users.get(request.email)
    if not user or not verify_password(request.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    token = create_access_token(request.email)
    return TokenResponse(access_token=token)

@router.get("/me", response_model=UserResponse)
def get_me(current_user: str = Depends(get_current_user)):
    user = store.users.get(current_user)
    return UserResponse(email=user["email"], role=user["role"])