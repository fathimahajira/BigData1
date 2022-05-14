"""
Name: Hajira Fathima
Date: May 14 2022
Class: CIS 2532 NET01
Description: Program that demonstrates relational databases and SQL.
"""

import sqlite3
import os.path
import pandas as pd

path = "C:\\Users\\COD_User\\Desktop\\ch17\\"
database = path + 'books.db'
connection = sqlite3.connect(database)
#print("Connection Successful",connection)
#connection = sqlite3.connect('books.db')

pd.options.display.max_columns = 10
print(pd.read_sql('SELECT * FROM authors', connection, index_col=['id']))
print(pd.read_sql('SELECT * FROM titles', connection))
df = pd.read_sql('SELECT * FROM author_ISBN', connection)
print(df.head())
print(pd.read_sql('SELECT first, last FROM authors', connection))
print(pd.read_sql("""SELECT title, edition, copyright FROM titles WHERE copyright > '2016'""", connection))
print(pd.read_sql("""SELECT id, first, last FROM authors WHERE last LIKE 'D%'""", connection, index_col=['id']))
print(pd.read_sql("""SELECT id, first, last FROM authors WHERE first LIKE '_b%'""", connection, index_col=['id']))
print(pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection))
print(pd.read_sql("""SELECT id, first, last FROM authors ORDER BY last, first""", connection, index_col=['id']))
print(pd.read_sql("""SELECT id, first, last FROM authors ORDER BY last DESC, first ASC""", connection, index_col=['id']))
print(pd.read_sql("""SELECT isbn, title, edition, copyright FROM titles WHERE title LIKE '%How to Program' ORDER BY title""", connection))
print(pd.read_sql("""SELECT first, last, isbn FROM authors INNER JOIN author_ISBN ON authors.id = author_ISBN.id ORDER BY last, first""", connection).head())

cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Sue', 'Red')""")
print(pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id']))

cursor = cursor.execute("""UPDATE authors SET last='Black' WHERE last='Red' AND first='Sue'""")
print(cursor.rowcount)
print(pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id']))

cursor = cursor.execute('DELETE FROM authors WHERE id=6')
print(cursor.rowcount)
print(pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id']))
