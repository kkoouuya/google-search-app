from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class ModelBase(BaseModel):
  is_deleted:int
  created_at: datetime
  updated_at: datetime
  version: int


class SiteBase(BaseModel):
  title: str
  url: str


class SiteUpdateRequest(SiteBase):
  site_id: UUID
  user_id: UUID


class Site(SiteUpdateRequest, ModelBase):
  word: str


class UserAuth(BaseModel):
  email: str
  password: str


class UserBase(UserAuth):
  username: Optional[str] = None


class UserUpdateRequest(UserBase):
  user_id: UUID


class UserGETResponse(UserUpdateRequest, ModelBase):
  pass


class FavoSite(BaseModel):
  email: str
  title: str
  url: str
  word: str