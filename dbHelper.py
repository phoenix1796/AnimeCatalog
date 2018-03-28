from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CatalogItem


#db setup
engine = create_engine("sqlite:///catalog.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def getAllCategories():
    return session.query(Category).with_entities(Category.name).all()

def getCategoryByName(name):
    print(name)
    return session.query(Category).filter_by(name = name).one()

def getItemsByCategory(category):
    return session.query(CatalogItem).filter_by(category_id = category.id)

def getItemByName(item_name):
    return session.query(CatalogItem).filter_by(name = item_name).one()