from database.models import Article
from repositories.repository import Repository

class ArticleRepository(Repository):
    def get_all():
        return ArticleRepository.Session.query(Article).all()
    
    def get(id):
        return ArticleRepository.Session.query(Article).filter_by(id=id).first()