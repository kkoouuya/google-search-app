from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, text
from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy_utils import UUIDType
import uuid
from datetime import datetime


class UserSite(Base):
  __tablename__ = "users_sites"
  
  user_id = Column(UUIDType(binary=False), ForeignKey('users.user_id'), primary_key=True)
  site_id = Column(UUIDType(binary=False), ForeignKey('sites.site_id'), primary_key=True)
  is_deleted = Column(Integer, default=0, nullable=False)
  version = Column(Integer, default=0, autoincrement=True, nullable=False)
  created_at = Column(DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nullable=False)
  updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False)
  
  user = relationship('User')
  site = relationship('Site')


class User(Base):
  __tablename__ = "users"
  
  user_id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
  username = Column(String(50), nullable=False)
  email = Column(String(50), unique=True, nullable=False)
  password = Column(String(50), nullable=False)
  is_deleted = Column(Integer, default=0, nullable=False)
  version = Column(Integer, default=0, autoincrement=True, nullable=False)
  created_at = Column(DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nullable=False)
  updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False)
  
  sites = relationship(
    'Site',
    secondary=UserSite.__tablename__,
    back_populates='users',
  )
  user_site = relationship('UserSite')
  
  
class Site(Base):
  __tablename__ = "sites"
  
  site_id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
  sitename = Column(String(1024), nullable=False)
  sitelink = Column(String(1024), nullable=False)
  word = Column(String(100), nullable=False)
  is_deleted = Column(Integer, default=0, nullable=False)
  version = Column(Integer, default=0, autoincrement=True, nullable=False)
  created_at = Column(DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nullable=False)
  updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False)
  
  users = relationship(
    'User',
    secondary=UserSite.__tablename__,
    back_populates='sites',
  )
  
  user_site = relationship('UserSite')
