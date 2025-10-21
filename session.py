from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://1234:1234@localhost:3307/mydb", pool_size=5, max_overflow=10)
SessionLocal = sessionmaker(bind=engine)

def get_session():
    return SessionLocal()
