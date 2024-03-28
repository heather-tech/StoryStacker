from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Author, Book

engine = create_engine("sqlite:///db/info.db")
session = Session(engine, future=True)

class Library:

    # Create
    def create_author(self, name):
        author = Author(name=name)
        session.add(author)
        session.commit()

    def create_book(self, title, author_id):
        book = Book(title=title, author_id=author_id)
        session.add(book)
        session.commit()

    # Delete 
    def delete_author(self, author_id):
        author = session.query(Author).get(author_id)
        if author:
            session.delete(author)
            session.commit()

    def delete_book(self, book_id):
        book = session.query(Book).get(book_id)
        if book:
            session.delete(book)
            session.commit()

    # Get All
    def get_all_authors(self):
        return session.query(Author).all()

    def get_all_books(self):
        return session.query(Book).all()
    
    # Find By...
    def find_author_by_name(self, name):
        return session.query(Author).filter_by(name=name).first()

    def find_book_by_title(self, title):
        return session.query(Book).filter_by(title=title).first()
    
    def find_book_by_id(self, book_id):
        book = session.query(Book).filter_by(id=book_id).first()
        return book