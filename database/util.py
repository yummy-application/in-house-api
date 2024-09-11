import sqlite3


def clear_db():
    with sqlite3.connect(r"D:\Programmierung\Android\Projects\yummy\in-house-api\restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("DROP TABLE IF EXISTS restaurant")
        db.commit()

if __name__ == '__main__':
    clear_db()