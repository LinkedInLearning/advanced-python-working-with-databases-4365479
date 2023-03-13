import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///users.db', echo=True)

users_to_insert = [{'first_name': 'Sarah', 'last_name': 'Perry', 
'email_address': 'sarah.perry@gmail.com'}, {'first_name': 'Felix', 'last_name': 
'Martin', 'email_address': 'felix_martin@gmail.com'}, {'first_name': 'John', 
'last_name': 'Patrick', 'email_address': 'johnny.patrick@outlook.com'}, {'first_name': 
'Jessica', 'last_name': 'Jones', 'email_address': 'jess.jones@hotwire.com'}, 
{'first_name': 'Percy', 'last_name': 'Colton', 'email_address': 'percy_c@outlook.com'}]

metadata = sqlalchemy.MetaData()

users_table = sqlalchemy.Table("users",
	metadata,
	sqlalchemy.Column("user_id", sqlalchemy.Integer, primary_key=True),
	sqlalchemy.Column("first_name", sqlalchemy.String),
	sqlalchemy.Column("last_name", sqlalchemy.String),
	sqlalchemy.Column("email_address", sqlalchemy.String)
	)

metadata.create_all(engine)

with engine.connect() as conn:
	conn.execute(sqlalchemy.insert(users_table).values(users_to_insert))
	for row in conn.execute(sqlalchemy.select(users_table)):
		print(row)
	conn.commit()

