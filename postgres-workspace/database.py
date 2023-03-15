from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base

engine = create_engine('postgresql+psycopg2://postgres:password@localhost/red30')

# class Sale(Base):
#       __tablename__='sales',
#       Column('order_num', Integer, primary_key=true),
#       Column('cust_name', String),
#       Column('prod_number', String),
#       Column('prod_name', String),
#       Column('quantity', Float),
#       Column('price', Float),
#       Column('discount', Float),
#       Column('order_total', Float))

Base = automap_base()

Base.prepare(autoload_with=engine)

Sales = Base.classes.sales






