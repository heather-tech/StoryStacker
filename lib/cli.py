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
            break
        else:
            print("Please select a valid option!")
# Author Menu
def author_menu(library):
    while True:
        print("\nAuthor Management")
        print("1. Create Author")
        print("2. Delete Author")
        print("3. List Authors")
        print("4. Go Back")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter author name: ")
            library.create_author(name)
            print("Author created!")
        elif choice == '2':
            author_id = int(input("Enter author ID to delete: "))
            library.delete_author(author_id)
            print("Author deleted!")
        elif choice == '3':
            authors = library.get_all_authors()
            for author in authors:
                print(f"Author ID: {author.id}, Name: {author.name}")
        elif choice == '4':
            break
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
            book_id = int(input("Enter book ID to delete: "))
            library.delete_book(book_id)
            print("Book deleted!")
        elif choice == '3':
            books = library.get_all_books()
            for book in books:
                if book.author:
                    print(f"Book ID: {book.id}, Title: {book.title}, Author: {book.author.name}")
                else:
                    print(f"Book ID: {book.id}, Title: {book.title}, Author: Unknown")
                # print(f"Book ID: {book.id}, Title: {book.title}, Author: {book.author.name}")
        elif choice == '4':
            break
        else:
            print("Please select a valid option.")

if __name__ == '__main__':
    main_menu()