import sqlite3


def create_table(table_name, number_of_seats, table_region):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO tables(name, seats, region) VALUES (?, ?, ?)", (table_name, number_of_seats, table_region))
        db.commit()

def table_exists(table_name) -> bool:
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM tables WHERE name = ?", (table_name,))
        result = cursor.fetchone()
        return result is not None