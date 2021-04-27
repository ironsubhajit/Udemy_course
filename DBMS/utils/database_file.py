"""
Concerned with storing and retriving books from a list
format of csv file:

name,author,read\n
"""

books_file = 'books.txt'


def create_book_table():
    with open(books_file, "w"):
        pass


def add_book(name, author):
    with open(books_file, 'a') as f:
        f.write(f"{name}, {author}, 0\n")


def show_books():   # return books list
    with open(books_file, 'r') as file:
        lines = [line.strip().split(",") for line in file.readlines()]

    return[
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]


def _save_all_books(books):
    with open(books_file, "w") as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def mark_book_as_read(find_name):
    books = show_books()
    for book in books:
        if book['name'] == find_name:
            book['read'] = '1'
    _save_all_books(books)


def delete_book(delete_book_name):
    books = show_books()
    books = [book for book in books if book['name'] != delete_book_name]
    _save_all_books(books)

