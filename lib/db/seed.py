from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Author, Book, Genre

# Creates the engine
engine = create_engine('sqlite:///info.db')

# Creates a session
Session = sessionmaker(bind=engine)
session = Session()

# Faker
faker = Faker()

# Create instances of classes 
def seed_data():
    # Clears database before reseeding. 
    authors = session.query(Author).all()
    for author in authors:
        session.delete(author)
    books = session.query(Book).all()
    for book in books:
        session.delete(book)
    genres = session.query(Genre).all()
    for genre in genres:
        session.delete(genre)

    # Authors
    for _ in range(5):
        author = Author(name=faker.name())
        session.add(author)
        session.commit()
    print("Number of authors inserted:", session.query(Author).count())

    # List of genre names
    genre_names = ['Fantasy', 'Mystery', 'Romance', 'Thriller', 'Science Fiction', 'Young Adult', 'Fiction', 'Historical Fiction', 'Drama', 'Poetry', 'Humor', 'Folklore', 'Biography', 'Self-Help', 'Adventure']

    #Genres
    for genre_name in genre_names:
        genre = Genre(name=genre_name)
        session.add(genre)
        session.commit()
    print("Number of genres inserted:", session.query(Genre).count())
        

    # Books
    authors = session.query(Author).all()
    genres = session.query(Genre).all()
    for _ in range(10):
        book = Book(title=faker.catch_phrase(), author=faker.random_element(authors), genre=faker.random_element(genres))
        session.add(book)
        session.commit()
    print("Number of books inserted:", session.query(Book).count())


if __name__ == "__main__":
    seed_data()
    session.close()