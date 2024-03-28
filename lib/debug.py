from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from db.models import Author, Book

if __name__ == '__main__':
    engine = create_engine("sqlite:///info.db")
    session = Session(engine, future=True)

    import ipdb; ipdb.set_trace()