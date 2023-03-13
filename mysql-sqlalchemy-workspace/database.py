from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import registry

engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/projects',
	echo=True)

mapper_registry = registry()
#mapper_registry.metadata

Base = mapper_registry.generate_base()

class Project(Base):
	__tablename__ = 'projects'
	project_id = Column(Integer, primary_key=True)
	title = Column(String(length=50))
	description = Column(String(length=50))

	def __repr__(self):
		return "<Project(title='{0}, description='{1}')>".format(
			self.title, self.description)