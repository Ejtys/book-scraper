import sqlite3


class Database:
    DATABASE_FILE ='data.sqlite'


    """Execute a query on database."""
    @classmethod
    def execute(cls, query: str, values:tuple = None, file_name: str =DATABASE_FILE) -> None:
        conn = sqlite3.connect(file_name)
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_key=on;')
        if values:
            cur.execute(query, values)
        else:
            cur.execute(query)
        
        conn.commit()
        conn.close()

    """General fetch method helping with getting entries from database."""
    @classmethod
    def fetch_all(cls, table_name, limit:int = None, offset:int=None, file_name:str = DATABASE_FILE) -> list[tuple]:
        conn = sqlite3.connect(file_name)
        cur = conn.cursor()
        if limit and offset:
            cur.execute(f"SELECT * FROM {table_name} LIMIT {limit} OFFSET {offset};")
        elif limit:
            cur.execute(f"SELECT * FROM {table_name} LIMIT {limit};")
        elif offset:
            cur.execute(f"SELECT * FROM {table_name} OFFSET {offset};")
        else:
            cur.execute(f"SELECT * FROM {table_name};")
        result = cur.fetchall()
        conn.commit()
        cur.close()
        return result

    """Fetch directly from query."""
    @classmethod
    def query_fetch(cls, query:str, file_name:str = DATABASE_FILE) -> list[tuple]:
        conn = sqlite3.connect(file_name)
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
        conn.commit()
        cur.close()
        return result

    """Creates new table if not exists."""
    @classmethod
    def create_table_books(cls):
        QUERY = """CREATE TABLE IF NOT EXISTS books(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL UNIQUE,
                        price_cents INTEGER NOT NULL,
                        description TEXT NOT NULL,
                        category TEXT NOT NULL
        );
        """
        Database.execute(QUERY)

    """Printing table in terminal"""
    @classmethod
    def print_table(cls, table_name: str) -> None:
        for x in Database.fetch_all('books'):
            print(x)



if __name__ == "__main__":
    Database.create_table_books()
    Database.print_table('books')
    print(Database.query_fetch("SELECT count(*) from books where title = 'Harry Potter';")[0][0])