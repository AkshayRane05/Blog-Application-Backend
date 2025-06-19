from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select, Session
from .. import schemas
from ..database import get_db
from .. import models
from ..models import User
from ..hashing import Hash
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)


@router.post("/", response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get(id, db)
