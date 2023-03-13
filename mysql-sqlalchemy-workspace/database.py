from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import registry, create_engine

engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/projects',
	echo=True)