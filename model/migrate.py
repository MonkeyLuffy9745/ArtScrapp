#!../.venv/bin/python3
from sqlalchemy.orm import configure_mappers
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy_utils.functions import create_database, database_exists
from models import Model

host = 'localhost'
username = 'artscrapp'
password = 'azerty'
dbname = 'artscrapp'
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}/{dbname}')
Session = sessionmaker(bind=engine)

if not database_exists(engine.url):
    create_database(engine.url)
    
configure_mappers()
Model.metadata.create_all(engine)
print("Database created successfully")