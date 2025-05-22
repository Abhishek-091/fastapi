from sqlalchemy import Column, Integer, String
from app.database.session import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, name = "id")
    name = Column(String, index=True, name = "user_name")
    email = Column(String, unique=True, index=True, name = "user_email")
