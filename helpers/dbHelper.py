from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CatalogItem, User


# db setup
engine = create_engine("sqlite:///catalogWithUsers.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def getAllCategories():
    return session.query(Category).with_entities(Category.name).all()


def getCategoryByName(name):
    print(name)
    return session.query(Category).filter_by(name=name).one()


def getItemsByCategory(category):
    return session.query(CatalogItem).filter_by(category_id=category.id).all()


def getItemByName(item_name):
    return session.query(CatalogItem).filter_by(name=item_name).one()


def createUser(login_session):
    newUser = User(name=login_session['username'],
                   email=login_session['email'],
                   picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    return session.query(User).filter_by(id=user_id).one()


def getUserId(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None
