from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import os
from dotenv import load_dotenv



load_dotenv() #reads .env variables

URL_DATABASE= os.getenv("DATABASE_URL", "sqlite:///./app.db") #reads database URL, if no postgres, go to sqlite
#catch login fail
#if not URL_DATABASE: #catches mistakes for login to databse
    #raise RuntimeError("DATABASE_URL is not set. Check .env file.") #

# For SQLite we need this flag when used with multiple threads (FastAPI dev server)
connect_args = {"check_same_thread": False} if URL_DATABASE.startswith("sqlite") else {}

#runs engine (connection pool for DB)
engine = create_engine(URL_DATABASE, pool_pre_ping=True, connect_args=connect_args) 


#one DB session per request to avoid
# It saves if everything goes well, or cancels if something fails.
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


#Base class for ORM-model
Base=declarative_base()


def get_db():
    """Provide one database session per HTTP request (unit of work).

    Flow:
    - Create session at request start
    - Yield it to the endpoint so all DB work shares one transaction
    - If handler returns OK: commit once
    - If handler raises: rollback (no partial writes)
    - Always close the session (return connection to the pool)

    Why: avoids connection leaks, cross-request bleed, and half-saved changes.
    """
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
