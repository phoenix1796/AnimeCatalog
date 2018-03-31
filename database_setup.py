import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(
        Integer, primary_key=True
    )
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    picture = Column(String(255))


class Category(Base):
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
        print(self.items)
        return {
            'id': self.id,
            'name': self.name,
            'summary': self.summary,
            'anime': [i.serialize for i in self.items]
        }


class CatalogItem(Base):
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
        return {
            'name': self.name,
            'summary': self.summary,
            'id': self.id,
            'category': self.category.name
        }


if __name__ == '__main__':
    engine = create_engine(
        'sqlite:///catalogWithUsers.db')
    Base.metadata.create_all(engine)
