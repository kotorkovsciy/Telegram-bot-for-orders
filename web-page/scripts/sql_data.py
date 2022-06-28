import sqlite3 as sql


class Database:
    def __init__(self, db_file):
        self.connection = sql.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.connection.execute("""CREATE TABLE IF NOT EXISTS "info_products" (
	                            "id"	INTEGER NOT NULL UNIQUE,
	                            "title"	TEXT NOT NULL,
	                            "status"	TEXT NOT NULL,
	                            "price"	INTEGER NOT NULL,
	                            "quantity"	INTEGER NOT NULL,
	                            PRIMARY KEY("id")
                            )""")

    async def read_prod(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM info_products LIMIT 10").fetchall()

    async def read_prod_more(self, page):
        with self.connection:
            return self.cursor.execute("SELECT * FROM info_products LIMIT ?, ?", (page*10, 10)).fetchall()

    async def quantity_prod(self):
        with self.connection:
            return self.cursor.execute("SELECT count(*) FROM info_products").fetchall()[0][0]

    async def write_prod(self, title, status, price, quantity):
        with self.connection:
            return self.cursor.execute("INSERT INTO info_products (title, status, price, quantity) VALUES (?, ?, ?, ?)", (title, status, price, quantity, ))
