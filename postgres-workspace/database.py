import psycopg2

def insert_sale(cur, order_num, cust_name, prod_number, prod_name, quantity, price, 
	discount):
	order_total = quantity * price
	if discount != 0:
		order_total = order_total * discount
	sale_data = {
	'order_num' : order_num,
	'cust_name' : cust_name,
	'prod_number' : prod_number,
	'prod_name' : prod_name,
	'quantity' : quantity,
	'price' : price,
	'discount' : discount,
	'order_total' : order_total
	}

	cur.execute('''INSERT INTO sales VALUES (%(order_num)s, 
		%(cust_name)s, %(prod_number)s, %(prod_name)s, %(quantity)s, 
		%(price)s, %(discount)s, %(order_total)s)''', sale_data)

if __name__ == "__main__":
   conn = psycopg2.connect(database="red30",
                  user = "postgres",
                  password = "password",
                  host = "localhost", 
                  port = "5432")
   cursor = conn.cursor()
   print("Input sale data:\n")
   order_num = int(input("What is the order number?\n"))
   cust_name = input("What is the customer's name?\n")
   prod_number = input("What is the product number?\n")
   prod_name = input("What is the product name?\n")
   quantity = float(input("How many were bought?\n"))
   price = float(input("What is the price of the product?\n"))
   discount = float(input("What is the discount, if there is one?\n"))
   print("Inputting sale data:\n")
   insert_sale(cursor, order_num, cust_name, prod_number, prod_name, quantity, price, discount)
   conn.commit()
   conn.close()





   