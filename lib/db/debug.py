from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from models import Author, Book, Genre

# Creates the engine
engine = create_engine('sqlite:///info.db')

# Creates a session
Session = sessionmaker(bind=engine)
session = Session()
breakpoint()
# if __name__ == '__main__':
#     engine = create_engine("sqlite:///info.db")
#     session = Session(engine, future=True)
