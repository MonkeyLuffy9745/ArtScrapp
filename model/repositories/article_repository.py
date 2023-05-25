from ..models import Article
from .repository import Repository

class ArticleRepository(Repository):
    def get_all():
        return ArticleRepository.Session.query(Article).all()
    
    def get_by_link(link):
        return ArticleRepository.Session.query(Article).filter_by(link=link).first()
    
    def get(id):
        return ArticleRepository.Session.query(Article).filter_by(id=id).first()