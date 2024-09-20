import sqlite3


def set_password(md5_hash):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO validation(pw_hash) VALUES (?)", (md5_hash,))
        db.commit()


def check_password(md5_hash) -> bool:
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM validation WHERE pw_hash = ?", (md5_hash,))
        return cursor.fetchone() is not None
