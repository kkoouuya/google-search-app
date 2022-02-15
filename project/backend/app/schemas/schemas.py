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
  sitename: str
  sitelink: str
  word: str


class SiteUpdateRequest(SiteBase):
  id: UUID


class Site(SiteUpdateRequest, ModelBase):
  pass


class UserAuth(BaseModel):
  email: str
  password: str


class UserBase(UserAuth):
  username: Optional[str] = None


class UserUpdateRequest(UserBase):
  user_id: UUID


class UserGETResponse(UserUpdateRequest, ModelBase):
  pass


class UserSite(ModelBase):
  user_id: UUID
  site_id: UUID