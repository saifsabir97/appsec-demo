import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (name, password) VALUES (?, ?)",
            ('admin', 'admin')
            )

connection.commit()
connection.close()
