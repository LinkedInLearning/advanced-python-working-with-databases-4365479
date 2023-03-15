from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import registry, relationship, Session

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

class Task(Base):
	__tablename__ = 'tasks'
	task_id = Column(Integer, primary_key=True)
	project_id = Column(Integer, ForeignKey('projects.project_id'))
	description = Column(String(length=50))

	project = relationship("Project")

	def __repr__(self):
		return "<Task(description='{0}')>".format(self.description)

Base.metadata.create_all(engine)

with Session(engine) as session:
	organize_closet_project = Project(title='Organize closet', 
		description='Organize closet by color and style')

	session.add(organize_closet_project)

	session.flush()

	tasks = [
	Task(project_id=organize_closet_project.project_id,
		description='Decide what clothes to donate'),
	Task(project_id=organize_closet_project.project_id,
		description='Organize summer clothes'),
	Task(project_id=organize_closet_project.project_id,
		description='Organize winter clothes')
	]

	session.bulk_save_objects(tasks)

	session.commit()













