from utils import database_json

user_choice = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice:"""


def menu():
    database_json.create_book_table()
    user_input = input(user_choice)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command. please try again.")

        user_input = input(user_choice)
    else:
        exit(0)


def prompt_add_book():
    name = input("enter book name: ")
    author = input("enter author name: ")
    database_json.add_book(name, author)


def list_books():
    books = database_json.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")


def prompt_read_book():
    book_name = input("Enter The Book Name You just finished reading: ")
    database_json.mark_book_as_read(book_name)


def prompt_delete_book():
    book_name = input("Enter The Book Name to be deleted: ")
    database_json.delete_book(book_name)
    print(f"{book_name} has been deleted.")


try:
    menu()
except RuntimeWarning:
    pass
finally:
    print("quit successfully".title())