#SQLALCHEMY in service layer lets python connect with MYSQL
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine,text
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase,sessionmaker
load_dotenv()
#we have all details like our username and passward and we dont want to
#expose passward when we upload it to git so we keep it in .env file
#we create url with all of our dtails to connect with the database without exposing our details
DATABASE_URL = URL.create(
    #mysql is system we are connected to and pymysql is the python driver
    #that knows how to communicate with mysql
    #sql alchemy uses that driver to establish the connection
    "mysql+pymysql",
    #it doesn't mean that we have manually opened one permanent connection
    #Instead ,SQLAlchemy uses the engine to manange database connections when our application needs them
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME")
)

engine = create_engine(DATABASE_URL)

#base is foundation of sqlalchemy models
class Base(DeclarativeBase):
    pass

#what is sessionmaker?
#It is a fn provided by sql alchemy that createsa factory for database sessions
SessionLocal=sessionmaker(bind=engine)#whenever needed a database session is created using this engine
db=SessionLocal() #This creates an actual session

#what is transaction?
 #it is complete cycle of a process from start to end . when a process is completed
 #we commit() the changes so we can make the changes permanent 
 #But for example something goes wrong in between then we can rollback using db.rollback()

