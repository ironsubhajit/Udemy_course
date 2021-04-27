import sqlite3


class DatabaseConnections:
    def __init__(self, host):
        self.host = host
        self.connection = sqlite3.connect(self.host)
        self.cursor = None

    def __enter__(self):
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
