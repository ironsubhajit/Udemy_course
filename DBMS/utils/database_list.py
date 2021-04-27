"""
Concerned with storing and retriving books from a list
"""

books = []


def add_book(name, author): # add book to books list
    books.append({'name': name, 'author': author, 'read': False})


def show_books():   # return books list
    return books


def mark_book_as_read(find_name):    # find book from list and change read status to True
    for book_name in books:
        if book_name['name'] == find_name:
            book_name['read'] = True
            return f"List updated successfully!"
        else:
            return f"{find_name} is not in book list!"


def delete_book(delete_book_name):
    global books
    books = [book for book in books if book['name'] != delete_book_name]

# def delete_book(delete_book_name):
#    for book_name in books:
#        if book_name['name'] == delete_book_name:
#            books.remove(book_name)
#   return f"{delete_book_name} Book has been deleted from list."
