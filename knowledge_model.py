from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__='article'
	primary_key = Column(Integer, primary_key=True)
	name = Column(String)
	topic = Column(String)
	rating = Column(Integer)
	def __repr__(self):
		return ("Knowledge Name: {}\n"
				"Knowledge Topic: {}\n"
				"Knowledge rating: {}").format(
					self.name,
					self.topic,
					self.rating)
a=Knowledge(name="shawrma",topic="food",rating="10")
print (a)

	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

	