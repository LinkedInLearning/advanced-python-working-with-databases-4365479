import sqlite3

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

release_year = (1985,)

cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)

print(cursor.fetchall())

connection.commit()
connection.close()