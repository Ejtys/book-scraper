from database import Database

class BookData:
    TABLE_NAME: str = "books"

    @classmethod
    def insert(cls, title:str, price_cents:int, description:str, category:str):
        Database.execute(f"""INSERT INTO {BookData.TABLE_NAME} (title, price_cents, description, category) 
                                VALUES (?, ?, ?, ?)""", (title, price_cents, description, category))

    @classmethod
    def get_all(cls):
        pass



if __name__ == '__main__':
    BookData.insert('Harry Potter', 1200, 'Book about magical boy in magical school.', 'fantasy')