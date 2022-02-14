from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class ModelBase(BaseModel):
  is_deleted:int
  created_at: datetime
  updated_at: datetime
  version: int


class SiteBase(BaseModel):
  sitename: str
  sitelink: str
  word: str


class SiteUpdateRequest(SiteBase):
  id: UUID


class Site(SiteUpdateRequest, ModelBase):
  pass


class UserBase(BaseModel):
  username: str
  email: str
  password: str


class UserUpdateRequest(UserBase):
  user_id: UUID


class UserGETResponse(UserUpdateRequest, ModelBase):
  pass


class UserSite(ModelBase):
  user_id: UUID
  site_id: UUID