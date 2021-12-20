import sqlite3


def execute(sql, params=None):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()

    if params is not None:
        cur.execute(sql, params)
    else:
        cur.execute(sql)

    conn.commit()
    conn.close()


def fetch(sql, params=None):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()

    if params is not None:
        cur.execute(sql, params)
    else:
        cur.execute(sql)

    rows = cur.fetchall()
    conn.close()

    return rows


def connect():
    query = "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, year INTEGER, isbn INTEGER)"
    execute(query)


def insert(title, author, year, isbn):
    query = "INSERT INTO books (title, author, year, isbn) VALUES (:title, :author, :year, :isbn)"
    execute(
        query, {"title": title, "author": author, "year": year, "isbn": isbn}
    )


def view():
    query = "SELECT * FROM books"

    return fetch(query)


def search(title=None, author=None, year=None, isbn=None):
    params = 0
    query = "SELECT * FROM books WHERE "

    if title is not None:
        query = query + f"title = '{title}'"
        params += 1

    if author is not None and params > 0:
        query = query + f" AND author = '{author}'"
    elif author is not None and params == 0:
        query = query + f"author = '{author}'"
        params += 1

    if year is not None and params > 0:
        query = query + f" AND year = {year}"
    elif year is not None and params == 0:
        query = query + f"year = {year}"
        params += 1

    if isbn is not None and params > 0:
        query = query + f" AND isbn = {isbn}"
    elif isbn is not None and params == 0:
        query = query + f"isbn = {isbn}"

    return fetch(query)


def delete(id):
    query = "DELETE FROM books WHERE id = :id"
    execute(query, {"id": id})


def update(id, title, author, year, isbn):
    query = "UPDATE books SET title = :title, author = :author, year = :year, isbn = :isbn WHERE id = :id"
    execute(
        query,
        {
            "title": title,
            "author": author,
            "year": year,
            "isbn": isbn,
            "id": id,
        },
    )


connect()

# print(view())
