from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.user import User
from app.repositories import user_repository
from app.schemas.user_schema import UserCreate, UserOut

router = APIRouter()


@router.post("/create", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_repository.create_user(db=db, user=user)



@router.get("/{email}", response_model=UserOut)
def read_user(email: str, db: Session = Depends(get_db)):
    db_user = user_repository.get_user(db=db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
