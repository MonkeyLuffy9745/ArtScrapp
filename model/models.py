from sqlalchemy import Column, String, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Model = declarative_base()

class Website(Model):
    __tablename__="websites"
    id = Column(Integer, primary_key=True, autoincrement=True)
    libelle = Column(String(50), nullable=False, unique=True)
    link = Column(String(255), nullable=False, unique=True)
    articles = relationship("Article", back_populates="website", cascade="all, delete, delete-orphan")
    
    def __json__(self):
        return {
            'id': self.id,
            'libelle': self.libelle,
            'link': self.link,
        }
    
    
class Article(Model):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(25), nullable=False)
    link = Column(String(255), nullable=False, unique=True)
    description = Column(Text)
    created_at = Column(String(25))
    website_id = Column(Integer, ForeignKey('websites.id'), nullable=False)
    website = relationship('Website', back_populates="articles")
    
    def __json__(self):
        return {
            'id': self.id,
            'title':self.title,
            'link': self.link,
            'description':self.description,
            'website_id':self.website_id
        }
