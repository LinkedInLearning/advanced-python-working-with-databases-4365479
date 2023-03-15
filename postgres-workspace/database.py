from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Float, String, MetaData

engine = create_engine('postgresql+psycopg2://postgres:password@localhost/red30', 
	echo=True)
metadata = MetaData()

# sales_table = Table('sales', 
#       metadata,  
#       Column('order_num', Integer, primary_key=true),
#       Column('cust_name', String),
#       Column('prod_number', String),
#       Column('prod_name', String),
#       Column('quantity', Float),
#       Column('price', Float),
#       Column('discount', Float),
#       Column('order_total', Float))

sales_table = Table('sales', metadata, autoload_with=engine)

metadata.create_all(engine)