"""
Concerned with storing and retrieving books from a list
format of json file:
[
    {"name": "book1", "author": "author1", "read": true},
    {"name": "book2", "author": "author2", "read": true}
]
"""
import json

books_file = 'books.json'


def create_book_table():
    with open(books_file, "w") as file:
        json.dump([], file)


def get_all_books():   # return books list
    with open(books_file, 'r') as file:
        return json.load(file)


def add_book(name, author):
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, "w") as file:
        json.dump(books, file)


def mark_book_as_read(find_name):
    books = get_all_books()
    for book in books:
        if book['name'] == find_name:
            book['read'] = True
    _save_all_books(books)


def delete_book(delete_book_name):
    books = get_all_books()
    books = [book for book in books if book['name'] != delete_book_name]
    _save_all_books(books)

