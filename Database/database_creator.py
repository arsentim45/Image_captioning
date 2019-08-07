import sqlite3


def creator():
    conn = sqlite3.connect("main_database.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""CREATE TABLE pictures (link, description)""")
        conn.commit()
    except sqlite3.OperationalError:
        print('Database already exist')


if __name__ == '__main__':
    creator()