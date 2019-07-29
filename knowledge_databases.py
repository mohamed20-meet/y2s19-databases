from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name, topic, rating):
	Knowledge_object = Knowledge(name=name,topic=topic,rating=rating)
	session.add(Knowledge_object)
	session.commit()
	

def query_all_articles():
	k = session.query(Knowledge).all()
	return k
	

def query_article_by_topic(topic):
	k = session.query(Knowledge).filter_by(topic=topic).all()

	

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(topic=topic).delete()
	session.commit()

def delete_all_articles():
	session.query(Knowledge).delete()

def edit_article_rating(rating):
	Knowledge_object.rating=rating
	session.commit()


def update_topic_status(name, rating):
	update_topic_status("shawrma", "fruit")

	



add_article ("falafel","food",10)
add_article ("humes","food",6)
add_article ("shawrma","food",10)
delete_article_by_topic("food")
print (query_all_articles())


