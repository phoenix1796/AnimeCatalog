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
    @property
    def serialize(self):
        return {
            'name': self.name,
            'summary': self.description,
            'id': self.id
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
            'summary':self.description,
            'id': self.id,
        }

engine = create_engine(
    'sqlite:///catalog.db')
Base.metadata.create_all(engine)