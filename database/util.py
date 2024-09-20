import sqlite3


def run_command():
    with sqlite3.connect(r"D:\Programmierung\Android\Projects\yummy\in-house-api\restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tables(name Text, seats INT DEFAULT 2, status Varchar(255) DEFAULT 'free', region TEXT DEFAULT 'unspecified')")
        db.commit()

if __name__ == '__main__':
    run_command()