from sqlmodel import Session, select
from .. import models, schemas
from ..models import Blog
from fastapi import HTTPException, status
from ..hashing import Hash
from ..models import User


def create(request: schemas.User, db: Session):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )  # type: ignore
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get(id: int, db: Session):
    statement = select(User).where(User.id == id)
    user = db.exec(statement).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
