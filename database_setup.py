import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    """Class to store User information

    Attributes:
        id (int): Unique user id for the user.
        name (str): User name for the user.
        email (str): Email Id associated with the user.
        picture (str, Optional): URL for the profile pic of user.'
    """
    __tablename__ = 'user'

    id = Column(
        Integer, primary_key=True
    )
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    picture = Column(String(255))


class Category(Base):
    """Class to store Category information

    Attributes:
        id (int): Unique Category id
        name (str): Category name
        summary (str): Summary of each category
        user_id (int): Foreign Key, UserId for the creator of this category
        user (obj): Foreign key relation object
        items ([obj]): One(Category) to Many(Items) relation object ,
                        for items belonging to a Category
    """
    __tablename__ = 'category'
    name = Column(
        String(80), unique=True, nullable=False)
    summary = Column(
        String(500), nullable=False)
    id = Column(
        Integer, primary_key=True
    )
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    items = relationship(
        'CatalogItem', cascade="all, delete-orphan", single_parent="true")

    @property
    def serialize(self):
        """
        Serialize Category
        & all the items belonging to the category
        """
        return {
            'id': self.id,
            'name': self.name,
            'summary': self.summary,
            'anime': [i.serialize for i in self.items]
        }


class CatalogItem(Base):
    """Class to store CatalogItem information

    Attributes:
        id (int): Unique Item id
        name (str): Item name
        summary (str): Summary of each item
        user_id (int): Foreign Key, UserId for the creator of this item
        user (obj): Foreign key relation object
        items ([obj]): Many(Items) to One(Category) relation object ,
                        for items belonging to a Category
    """
    __tablename__ = 'catalog_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    summary = Column(String(250))
    category_id = Column(
        Integer, ForeignKey('category.id')
    )
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """
        Serialize the item ,
        to ease conversion to json
        """
        return {
            'name': self.name,
            'summary': self.summary,
            'id': self.id,
            'category': self.category.name
        }


if __name__ == '__main__':
    engine = create_engine(
        'sqlite:///catalog.db')
    Base.metadata.create_all(engine)
