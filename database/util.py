import sqlite3


def run_command():
    with sqlite3.connect(r"D:\Programmierung\Android\Projects\yummy\in-house-api\restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM tables")
        db.commit()

def cursor_dict_factory(cursor, row):
    dictionary = {}
    for index, column in enumerate(cursor.description):
        dictionary[column[0]] = row[index]
    return dictionary
if __name__ == '__main__':
    run_command()