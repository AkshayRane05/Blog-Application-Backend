from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = 'mysql+pymysql://root:admin@127.0.0.1:3306/test'

engine = create_engine(DATABASE_URL, echo=False)


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
