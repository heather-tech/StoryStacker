from helpers import Library

# Main Menu
def main_menu():
    library = Library()

    while True:
        print("\nWelcome To StoryStacker!")
        print("1. Manage Authors")
        print("2. Manage Books")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            author_menu(library)
        elif choice == '2':
            book_menu(library)
        elif choice == '3':
            print("Goodbye!")
            break # Exit loop 
        else:
            print("Please select a valid option!")

# Author Menu
def author_menu(library):
    while True:
        print("\n---------------------------------")
        print("\nAuthor Management")
        print("1. Create Author")
        print("2. Delete Author")
        print("3. List Authors")
        print("4. View Author Details")
        print("5. Go Back")

        choice = input("Select an option: ")
        # CREATE AUTHOR
        if choice == '1':
            print("\n---------------------------------")
            name = input("Enter author name: ")
            library.create_author(name)
            print("Author created!")
        # DELETE AUTHOR
        elif choice == '2':
            print("\n---------------------------------")
            print("Select an author to delete:")
            authors = library.get_all_authors()
            for i, author in enumerate(authors, 1):
                print(f"{i}. {author.name}")
            author_index = int(input("Enter author number to delete: ")) - 1
            if 0 <= author_index < len(authors):
                library.delete_author(authors[author_index].id)
                print("Author deleted!")
            else:
                print("Invalid author number!")
        # LIST ALL AUTHORS
        elif choice == '3':
            print("\n---------------------------------")
            authors = library.get_all_authors()
            for i, author in enumerate(authors, 1):
                print(f"{i}. {author.name}")
        # VIEW AUTHOR DETAILS - CHOOSE FROM LIST
        elif choice == '4':
            print("\n---------------------------------")
            authors = library.get_all_authors()
            for i, author in enumerate(authors, 1):
                print(f"{i}. {author.name}")
            author_index = int(input("Enter author number to view details: "))
            if 1 <= author_index <= len(authors):
                author = authors[author_index - 1]
                print("\n---------------------------------")
                print(f"Author Details:")
                print(f"Name: {author.name}")
                print("Books Written:")
                for i, book in enumerate(author.books, 1):
                    print(f"{i}. Title: {book.title} | Genre: {book.genre.name}")
            else:
                print("Invalid author number.")
        # RETURN TO MAIN MENU
        elif choice == '5':
            print("\n---------------------------------")
            break  # Return to main menu
        else:
            print("Please select a valid option.")

# Book Menu
def book_menu(library):
    while True:
        print("\n---------------------------------")
        print("\nBook Management")
        print("1. Create Book")
        print("2. Delete Book")
        print("3. List Books")
        print("4. Go Back")

        choice = input("Select an option: ")
        # CREATE BOOK
        if choice == '1':
            print("\n---------------------------------")
            title = input("Enter book title: ")
            author_name = input("Enter author name: ")
            existing_author = library.find_author_by_name(author_name)
            if existing_author:
                author_id = existing_author.id
            else:
                author_id = library.create_author(author_name).id
                print("Author created!")
            genres = library.get_all_genres()
            print("\nAvailable Genres:")
            for i, genre in enumerate(genres, 1):
                print(f"{i}. {genre.name}")
            genre_choice = input("Select genre: ")
            try:
                genre_index = int(genre_choice) - 1
                if 0 <= genre_index < len(genres):
                    library.create_book(title, author_id, genres[genre_index].id)
                    print("Book created!")
                else:
                    print("Invalid genre number.")
            except ValueError:
                print("Please enter a valid number.")
        # DELETE BOOK
        elif choice == '2':
            print("\n---------------------------------")
            books = library.get_all_books()
            print("\nSelect Book to Delete:")
            for i, book in enumerate(books, 1):
                if book.author:
                    print(f"{i}. {book.title} by {book.author.name} ({book.genre.name})")
                else:
                    print(f"{i}. {book.title} by Unknown ({book.genre.name})")
            book_choice = input("Enter book number to delete: ")
            try:
                book_index = int(book_choice) - 1
                if 0 <= book_index < len(books):
                    library.delete_book(books[book_index].id)
                    print("Book deleted!")
                else:
                    print("Invalid book number.")
            except ValueError:
                print("Please enter a valid number.")
        # LIST ALL BOOKS
        elif choice == '3':
            print("\n---------------------------------")
            books = library.get_all_books()
            for i, book in enumerate(books, 1):
                if book.author:
                    print(f"{i}. Title: {book.title}\n    Author: {book.author.name}\n    Genre: {book.genre.name}")
                else:
                    print(f"{i}. Title: {book.title}\n    Author: Unknown\n    Genre: {book.genre.name}")
        # RETURN TO MAIN MENU
        elif choice == '4':
            print("\n---------------------------------")
            break # Return to main menu
        else:
            print("Please select a valid option.")


if __name__ == '__main__':
    main_menu()