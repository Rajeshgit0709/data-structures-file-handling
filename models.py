from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import declarative_base

engine = create_engine("mysql+pymysql://1234:1234@localhost:3307/mydb")
Base = declarative_base()

class User(Base):
    __tablename__ = 'simple_users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    full_name = Column(String(100), nullable=False)
    age = Column(Integer)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())

Base.metadata.create_all(engine)
