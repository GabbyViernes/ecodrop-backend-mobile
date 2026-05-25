from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.db.session import Base
from datetime import datetime

class User(Base):
    # Mapping to Django's default auth_user table
    __tablename__ = "auth_user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False) # Django uses 'password'
    first_name = Column(String)
    last_name = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    date_joined = Column(DateTime, default=datetime.utcnow)
