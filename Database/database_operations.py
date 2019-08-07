import sqlite3


def add_photo(link, description):
    conn = sqlite3.connect("main_database.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO pictures VALUES (?,?) """, (link, description))
    conn.commit()


def get_photos():
    conn = sqlite3.connect("main_database.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM pictures""")
    rows = cursor.fetchall()
    return rows


if __name__ == '__main__':
    get_photos()