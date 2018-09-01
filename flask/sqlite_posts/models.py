import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))
DB_LINK = path.join(ROOT, 'database.db')


def create_post(n, c):
    con = sql.connect(DB_LINK)
    cur = con.cursor()
    cur.execute('INSERT INTO posts (name, content) VALUES (?, ?)', (n, c))
    con.commit()
    con.close()


def get_posts():
    con = sql.connect(DB_LINK)
    cur = con.cursor()
    cur.execute('SELECT * FROM posts')
    posts = cur.fetchall()
    return posts
