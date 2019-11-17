import sqlite3

with sqlite3.connect('scandi.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE posts")
    c.execute("CREATE TABLE posts(title TEXT, description TEXT)")
    c.execute('INSERT INTO posts VALUES("Pancakes", "This is how you do this")')
    c.execute('INSERT INTO posts VALUES("Soup", "This is how you do this")')