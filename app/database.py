from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv



load_dotenv() #reads .env credentials
URL_DATABASE= os.getenv("DATABASE_URL")
if not DATABASE_URL: #catches mistakes for login to databse
    raise RuntimeError("DATABASE_URL is not set. Check .env file.") #

engine = create_engine(URL_DATABASE) #runs engine

SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)


#Base class for ORM-model
Base=declarative_base()


