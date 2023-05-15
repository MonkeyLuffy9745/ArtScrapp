from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

class Repository():
    def get_engine(host, username):
        host = 'localhost'
        username = 'artscrapp'
        password = 'azerty'
        dbname = 'artscrapp'
        return create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}/{dbname}')
    
    def connect():
        engine = Repository.get_engine()
        Repository.Session = scoped_session(sessionmaker(bind=engine))
        
    def disconnect():
        Repository.Session.remove()
        
    def store(table):
        Repository.Session.add(table)
        Repository.Session.commit()
        return table
    
    def update(table):
        Repository.Session.commit()
        return table
    
    def delete(table):
        Repository.Session.delete(table)
        Repository.Session.commit()