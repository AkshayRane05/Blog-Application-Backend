from sqlmodel import Session, select
from .. import models, schemas
from ..models import Blog
from fastapi import HTTPException, status


def get_all(db: Session):
    blogs = db.exec(select(models.Blog)).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title,
                           body=request.body, user_id=1)  # type: ignore
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id: int, db: Session):
    statement = select(Blog).where(Blog.id == id)  # type: ignore
    blog = db.exec(statement).first()  # type: ignore

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")

    db.delete(blog)
    db.commit()
    return {"message": f"Blog with id: {id} has been deleted."}


def update(id: int, request: schemas.Blog, db: Session):
    statement = select(Blog).where(Blog.id == id)  # type: ignore
    blog = db.exec(statement).first()  # type: ignore

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    blog.title = request.title
    blog.body = request.body

    db.add(blog)
    db.commit()
    db.refresh(blog)
    return {"message": f"Blog with id: {id} has been updated."}


def get(id: int, db: Session):
    blog = db.exec(select(Blog).where(Blog.id == id)).first()  # type: ignore

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog
