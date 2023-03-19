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

if __name__ == "__main__":
    Database.create_table_books()
