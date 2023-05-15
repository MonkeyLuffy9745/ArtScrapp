from database.models import Website
from repositories.repository import Repository

class WebsiteRepository(Repository):
    def get_all():
        return WebsiteRepository.Session.query(Website).all()
    
    def get(id):
        return WebsiteRepository.Session.query(Website).filter_by(id=id).first()