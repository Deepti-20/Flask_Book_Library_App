   
from sqlalchemy import (
    Column, 
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from models import User, Base

conn_string = "sqlite:///test.sqlite3"
engine = create_engine(conn_string)
Base.metadata.create_all(engine) # here we create all tables
Session = sessionmaker(bind=engine)
session = Session()

# Now we are ready to use the model

new_user = User(name="test")
session.add(new_user)
session.commit()

