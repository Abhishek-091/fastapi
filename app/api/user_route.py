from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.user import User
from app.repositories import user_repository

router = APIRouter()


class UserCreate(BaseModel):
    name: str
    email: EmailStr

@router.post("/create", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_repository.create_user(db=db, user=user)



@router.get("/{email}", response_model=User)
def read_user(email: str, db: Session = Depends(get_db)):
    db_user = user_repository.get_user(db=db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
