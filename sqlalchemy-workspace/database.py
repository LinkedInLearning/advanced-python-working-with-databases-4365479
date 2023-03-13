import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///movies.db', echo=True)

with engine.connect() as conn:
	result = conn.execute(sqlalchemy.text("SELECT * FROM Movies"))
	for row in result:
		print(row)
	
