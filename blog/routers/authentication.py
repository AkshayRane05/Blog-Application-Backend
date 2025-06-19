from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from blog.database import get_db
from blog.hashing import Hash
from blog.schemas import Token
from blog.models import User
from blog.token import create_access_token

router = APIRouter(
    tags=['Authentication']
)


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    statement = select(User).where(User.email == request.username)
    user = db.exec(statement).first()  # type: ignore
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=404, detail="Incorrect password")

    access_token = create_access_token(data={"sub": user.email})

    return Token(access_token=access_token, token_type="bearer")
