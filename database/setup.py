import sqlite3

def default_db_setup():
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS restaurant(name Text, image Text)")
        cursor.execute("CREATE TABLE IF NOT EXISTS validation(pw_hash Text)")
        cursor.execute("CREATE TABLE IF NOT EXISTS tables(name Text PRIMARY KEY, seats INT DEFAULT 2, status Varchar(255) DEFAULT 'free', region TEXT DEFAULT 'unspecified')")
        db.commit()
