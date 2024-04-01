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
        print("\nAuthor Management")
        print("1. Create Author")
        print("2. Delete Author")
        print("3. List Authors")
        print("4. View Author Details")
        print("5. Go Back")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter author name: ")
            library.create_author(name)
            print("Author created!")
        elif choice == '2':
            author_id = int(input("Enter author number to delete: "))
            library.delete_author(author_id)
            print("Author deleted!")
        elif choice == '3':
            authors = library.get_all_authors()
            for i, author in enumerate(authors, 1):
                print(f"{i}. {author.name}")
        elif choice == '4':
            author_id = int(input("Enter author number to view details: "))
            author = library.find_author_by_id(author_id)
            if author:
                print(f"Author Details:")
                print(f"Name: {author.name}")
                print("Books Written:")
                for i, book in enumerate(author.books, 1):
                    print(f"{i}. {book.title}")
            else:
                print("Author not found.")
        elif choice == '5':
            break # Return to main menu
        else:
            print("Please select a valid option.")

# Book Menu
def book_menu(library):
    while True:
        print("\nBook Management")
        print("1. Create Book")
        print("2. Delete Book")
        print("3. List Books")
        print("4. Go Back")

        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author_name = input("Enter author name: ")
            author = library.find_author_by_name(author_name)
            if author:
                library.create_book(title, author.id)
                print("Book created!")
            else:
                print("Author not found. Please create the author first.")
        elif choice == '2':
            book_id = int(input("Enter book number to delete: "))
            library.delete_book(book_id)
            print("Book deleted!")
        elif choice == '3':
            books = library.get_all_books()
            for i, book in enumerate(books, 1):
                if book.author:
                    print(f"{i}. {book.title} by {book.author.name} ({book.genre.name})")
                else:
                    print(f"{i}. {book.title} by Unknown ({book.genre.name})")
        elif choice == '4':
            break # Return to main menu
        else:
            print("Please select a valid option.")

if __name__ == '__main__':
    main_menu()