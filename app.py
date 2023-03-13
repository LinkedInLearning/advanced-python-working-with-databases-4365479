import sqlite3

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()



connection.commit()
connection.close()