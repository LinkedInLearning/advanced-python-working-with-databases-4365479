import psycopg2

conn = psycopg2.connect(database="red30",
	user="postgres",
	password="password",
	host="localhost",
	port="5432")

cursor = conn.cursor()

cursor.execute('''CREATE TABLE SALES(ORDER_NUM INT PRIMARY KEY,
	CUST_NAME TEXT,
	PROD_NUMBER TEXT,
	PROD_NAME TEXT,
	QUANTITY INT,
	PRICE REAL,
	DISCOUNT REAL,
	ORDER_TOTAL REAL);''')

conn.commit()
conn.close()