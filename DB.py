from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



DB_URl = 'postgresql://postgres:Doolot23022005@localhost/fastapi2'

enginr = create_engine(DB_URl)

SessionLocal = sessionmaker(bind=enginr)

Base = declarative_base()

