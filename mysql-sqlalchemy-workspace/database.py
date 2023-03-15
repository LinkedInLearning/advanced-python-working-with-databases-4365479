from sqlalchemy import Column, String, Integer, Numeric, create_engine
from sqlalchemy.orm import registry, Session

engine = create_engine(
	'mysql+mysqlconnector://root:password@localhost:3306/red30',
	echo=True)

mapper_registry = registry()
Base = mapper_registry.generate_base()

class Sale(Base):
	__tablename__ = 'sales'

	order_num = Column(Integer, primary_key=True)
	cust_name = Column(String)
	prod_number = Column(String)
	prod_name = Column(String)
	quantity = Column(Integer)
	price = Column(Numeric)
	discount = Column(Numeric)
	order_total = Column(Numeric)

	def __repr__(self):
		return "<Sale(order_num='{0}', cust_name='{1}', prod_name='{2}', quantity='{3}', order_total='{4}')>".format(self.order_num, self.cust_name, self.prod_name, self.quantity, self.order_total)

Base.metadata.create_all(engine)

with Session(engine, future=True) as session:
	sale_1 = Sale(order_num=1100935, cust_name="Spencer Educators", prod_number="DK204",
		prod_name="BYOD-300", quantity=2, price=89, discount=0, order_total=178)
	sale_2 = Sale(order_num=1100948, cust_name="Ewan Ladd", prod_number="TV810",
		prod_name="Understanding Automation", quantity=1, price=44.95, discount=0, order_total=44.95)
	sale_3 = Sale(order_num=1100963, cust_name="Stehr Group", prod_number="DS301",
		prod_name="DA-SA702 Drone", quantity=3, price=399, discount=.1, order_total=1077.3)
	sale_4 = Sale(order_num=1100971, cust_name="Hettinger and Sons", prod_number="DS306",
		prod_name="DA-SA702 Drone", quantity=12, price=250, discount=.5, order_total=1500)
	sale_5 = Sale(order_num=1100998, cust_name="Luz O'Donoghue", prod_number="TV809",
		prod_name="Understanding 3D Printing", quantity=1, price=42.99, discount=0, order_total=42.99)

	sales = [sale_1, sale_2, sale_3, sale_4, sale_5]

	session.bulk_save_objects(sales)

	session.flush()
	session.commit()
