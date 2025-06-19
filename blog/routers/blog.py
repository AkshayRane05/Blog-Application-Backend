from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select, Session

from . import oauth2
from .. import schemas
from ..database import get_db
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.get("/", response_model=list[schemas.ShowBlog])
def get_all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.get("/{id}", response_model=schemas.ShowBlog)
def get_blog(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get(id, db)


@router.delete("/{id}")
def delete_blog(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)


@router.put("/{id}", status_code=status.HTTP_200_OK)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)
