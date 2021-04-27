from utils.database_connections import DatabaseConnections


def create_book_table():
    with DatabaseConnections('data.db') as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')


def get_all_books():
    with DatabaseConnections('data.db') as cursor:
        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor .fetchall()]  # [(name, author, read), ...]
    return books


def add_book(name, author):
    with DatabaseConnections('data.db') as cursor:
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))


def mark_book_as_read(find_name):
    with DatabaseConnections('data.db') as cursor:
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (find_name,))


def delete_book(delete_book_name):
    with DatabaseConnections('data.db') as cursor:
        cursor.execute('DELETE FROM books WHERE name=?', (delete_book_name,))
