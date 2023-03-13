import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///users.db', echo=True)

users_to_insert = [{'first_name': 'Sarah', 'last_name': 'Perry', 'email_address': 
'sarah.perry@gmail.com'}, {'first_name': 'Felix', 'last_name': 'Martin', 
'email_address': 'felix_martin@gmail.com'}, {'first_name': 'John', 'last_name': 
'Patrick', 'email_address': 'johnny.patrick@outlook.com'}, {'first_name': 'Jessica', 
'last_name': 'Jones', 'email_address': 'jess.jones@hotwire.com'}, {'first_name': 
'Percy', 'last_name': 'Colton', 'email_address': 'percy_c@outlook.com'}]

with engine.connect() as conn:
	conn.execute(sqlalchemy.text('''CREATE TABLE IF NOT EXISTS Users (user_id 
		integer primary key autoincrement, first_name text, last_name text, 
		email_address text)'''))

	conn.execute(sqlalchemy.text('''INSERT INTO Users (first_name, last_name, 
		email_address) VALUES (:first_name, :last_name, 
		:email_address)'''), users_to_insert)

	result = conn.execute(sqlalchemy.text('''SELECT * FROM Users'''))
	for row in result:
		print(row)
		
	conn.commit()
