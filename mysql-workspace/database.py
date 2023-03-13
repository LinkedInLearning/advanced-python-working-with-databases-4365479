import mysql.connector as mysql

def connect(db_name):
	try:
		return mysql.connect(host="localhost",
							 database=db_name,
							 user='root',
							 password="password")
	except Error as e:
		print(e)

def add_project(cursor, project_title, project_description, tasks):
	pass

if __name__ == '__main__':
	db = connect("projects")

	cursor = db.cursor()

	tasks = ["Clean bathroom", "Clean kitchen", "Clean living room"]
	add_project(cursor, "Clean house", "Clean house by room", tasks)
	db.commit()

	cursor.execute("SELECT * FROM projects")
	project_records = cursor.fetchall()
	print(project_records)

	cursor.execute("SELECT * FROM tasks")
	tasks_records = cursor.fetchall()
	print(tasks_records)