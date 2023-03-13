import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///movies.db', echo=True)
