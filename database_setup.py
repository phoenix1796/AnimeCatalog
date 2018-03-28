import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'
    name = Column(
    String(80), unique=True,nullable=False)
    summary = Column(
        String(500), nullable=False)
    id = Column(
        Integer, primary_key = True
    )
    items = relationship('CatalogItem')
    @property
    def serialize(self):
        print(self.items)
        return {
            'id': self.id,
            'name': self.name,
            'summary': self.summary,
            'anime':[i.serialize for i in self.items]
        }

class CatalogItem(Base):
    __tablename__ = 'catalog_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    summary = Column(String(250))
    category_id = Column(
        Integer, ForeignKey('category.id')
    )
    category = relationship(Category,cascade="all, delete-orphan", single_parent="true")
    @property
    def serialize(self):
        return {
            'name': self.name,
            'summary':self.summary,
            'id': self.id,
            'category': self.category.name
        }

engine = create_engine(
    'sqlite:///catalog.db')
Base.metadata.create_all(engine)