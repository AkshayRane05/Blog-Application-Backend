from sqlmodel import Field, SQLModel, Relationship
from typing import Optional


class Blog(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    body: str
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

    creator: Optional["User"] = Relationship(back_populates="blogs")


class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    email: str
    password: str

    blogs: list[Blog] = Relationship(back_populates="creator")
