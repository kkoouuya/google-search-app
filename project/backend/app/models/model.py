import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import UUIDType

Base = declarative_base()


class User(Base):
  __tablename__ = "users"
  
  user_id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
  username = Column(String(512), nullable=True)
  email = Column(String(512), unique=True, nullable=False)
  password = Column(String(512), nullable=False)
  is_deleted = Column(Integer, default=0, nullable=False)
  version = Column(Integer, default=0, autoincrement=True, nullable=False)
  created_at = Column(DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nullable=False)
  updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False)
  site = relationship('Site', backref='user')
  
  
class Site(Base):
  __tablename__ = "sites"
  
  site_id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
  user_id = Column(UUIDType(binary=False), ForeignKey('users.user_id',onupdate='CASCADE', ondelete='CASCADE'))
  title = Column(String(512), nullable=False)
  url = Column(String(512), nullable=False)
  word = Column(String(512), nullable=False)
  is_deleted = Column(Integer, default=0, nullable=False)
  version = Column(Integer, default=0, autoincrement=True, nullable=False)
  created_at = Column(DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nullable=False)
  updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False)