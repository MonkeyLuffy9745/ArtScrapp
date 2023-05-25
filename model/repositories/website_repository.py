from ..models import Website
from .repository import Repository

class WebsiteRepository(Repository):
    def get_all():
        return WebsiteRepository.Session.query(Website).all()
    
    def get_by_libelle(libelle: str):
        return WebsiteRepository.Session.query(Website).filter_by(libelle=libelle).first()
        
    
    def get(id):
        return WebsiteRepository.Session.query(Website).filter_by(id=id).first()