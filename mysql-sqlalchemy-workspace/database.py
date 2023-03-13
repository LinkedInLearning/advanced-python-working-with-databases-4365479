from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import registry

engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/projects',
	echo=True)