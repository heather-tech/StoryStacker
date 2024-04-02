from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Author, Book, Genre

engine = create_engine("sqlite:///db/info.db")
session = Session(engine, future=True)

class Library:

    # Create
    def create_author(self, name):
        author = Author(name=name)
        session.add(author)
        session.commit()
        return author

    def create_book(self, title, author_id, genre_id):
        book = Book(title=title, author_id=author_id, genre_id=genre_id)
        session.add(book)
        session.commit()

        author = session.query(Author).get(author_id)
        if not author:
            print("Author not found.")

        if not author.books:
            author.book.append(book)
            session.commit()

        return book
        

    def create_genre(self, genre_name, book=None):
        genre = Genre(name = genre_name)
        if book:
            genre.books.append(book)
        session.add(genre)
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

    def delete_genre(self, genre_id):
        genre = session.query(Genre).get(genre_id)
        if genre:
            session.delete(genre)
            session.commit()

    # Get All
    def get_all_authors(self):
        return session.query(Author).all()

    def get_all_books(self):
        return session.query(Book).all()

    def get_all_genres(self):
        return session.query(Genre).all()
    
    
    
    # Find By...
    def find_author_by_name(self, name):
        return session.query(Author).filter_by(name=name).first()
    
    def find_author_by_id(self, author_id):
        return session.query(Author).filter_by(id=author_id).first()

    def find_book_by_title(self, title):
        return session.query(Book).filter_by(title=title).first()
    
    def find_book_by_id(self, book_id):
        book = session.query(Book).filter_by(id=book_id).first()
        return book
    
    def find_genre_by_name(self, name):
        return session.query(Genre).filter_by(name=name).first()
    
    def find_genre_by_id(self, genre_id):
        genre = session.query(Genre).filter_by(id=genre_id).first()
        return genre
