from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Author, Book

# Creates the engine
engine = create_engine('sqlite:///info.db')

# Creates a session
Session = sessionmaker(bind=engine)
session = Session()

# Faker
faker = Faker()

# Create instances of classes 
def seed_data():

    # Authors
    for _ in range(5):
        author = Author(name=faker.name())
        session.add(author)
    session.commit()
    print("Number of authors inserted:", session.query(Author).count())

    # Books
    authors = session.query(Author).all()
    for _ in range(10):
        book = Book(title=faker.catch_phrase(), author=faker.random_element(authors))
        session.add(book)
    session.commit()
    print("Number of books inserted:", session.query(Book).count())


if __name__ == "__main__":
    seed_data()
    session.close()