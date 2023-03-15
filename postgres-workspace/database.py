from sqlalchemy import create_engine, select
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.orm import registry, Session, relationship

engine = create_engine('postgresql://postgres:password@localhost/library')

mapper_registry = registry()

Base = mapper_registry.generate_base()

class Author(Base):
	__tablename__ = 'authors'
	author_id = Column(Integer, primary_key=True)
	first_name = Column(String)
	last_name = Column(String)
	def __repr__(self):
		return "<Author(author_id='{0}', first_name='{1}', last_name='{2}')>" \
			.format(self.author_id, self.first_name, self.last_name)

class Book(Base):
	__tablename__ = 'books'
       
	book_id = Column(Integer, primary_key=True)
	title = Column(String)
	number_of_pages = Column(Integer)

	def __repr__(self):
		return "<Book(book_id='{0}', title='{1}', number_of_pages='{2}')>" \
			.format(self.book_id, self.title, self.number_of_pages)

class BookAuthor(Base):
	__tablename__ = 'bookauthors'

	bookauthor_id = Column(Integer, primary_key=True)
	author_id = Column(Integer, ForeignKey('authors.author_id'))
	book_id = Column(Integer, ForeignKey('books.book_id'))

	author = relationship("Author")
	book = relationship("Book")

	def __repr__(self):
		return "<BookAuthor (bookauthor_id='{0}', author_id='{1}', book_id='{2}', first_name='{3}', last_name='{4}', title='{5}')>" \
			.format(self.bookauthor_id, self.author_id, self.book_id, self.author.first_name, self.author.last_name, self.book.title)

Base.metadata.create_all(engine)


def add_book(title, number_of_pages, first_name, last_name):
	author = Author(first_name=first_name, last_name=last_name)
	book = Book(title=title, number_of_pages=number_of_pages)

	with Session(engine) as session:
		existing_book = session.execute(select(Book).filter(Book.title==title, Book.number_of_pages==number_of_pages)).scalar()
		if existing_book is not None:
			print("Book exists! Not adding book")
			return

		print("Book does not exist. Adding book")
		session.add(book)
		existing_author = session.execute(select(Author).filter(Author.first_name==first_name, Author.last_name==last_name)).scalar()

		if existing_author is not None:
			print("Author exists! Not adding author")
			session.flush()
			pairing=BookAuthor(author_id=existing_author.author_id, book_id=book.book_id)
		else:
			print("Author does not exist. Adding author")
			session.add(author)
			session.flush()
			pairing = BookAuthor(author_id=author.author_id, book_id=book.book_id)

		session.add(pairing)
		session.commit()
		print("New pairing added!" + str(pairing))

if __name__ == "__main__":
	print("Input new book:\n")
	title = input("What is the title of the book?\n")
	number_of_pages = int(input("How many pages are in the book?\n"))
	first_name = input("What is the first name of the author?\n")
	last_name = input("What is the last name of the author?\n")
	print("Inputting book data:\n")

	add_book(title, number_of_pages, first_name, last_name)

	print("Done!")
