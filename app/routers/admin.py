from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from app.models import User
from app.schemas import UserResponse
from app.auth_utils import require_admin
from app.database import get_session

router = APIRouter()

@router.get("/users", response_model=list[UserResponse])
def list_users(admin=Depends(require_admin), session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return [UserResponse(email=u.email, role=u.role) for u in users]

@router.patch("/users/{email}/role")
def update_role(email: str, body: dict, admin=Depends(require_admin), session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.email == email)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.role = body.get("role")
    session.add(user)
    session.commit()
    return {"message": f"Role updated to {user.role}"}

@router.delete("/users/{email}")
def delete_user(email: str, admin=Depends(require_admin), session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.email == email)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"message": "User deleted"}