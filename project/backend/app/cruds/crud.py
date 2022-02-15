from typing import Optional, Tuple
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.model import User, Site
from app.schemas.schemas import FavoSite
from app.auth_utils import AuthJwtCsrf
from uuid import UUID


auth = AuthJwtCsrf()


def site_serializer(site) -> dict:
  return {
    "site_id": site.site_id,
    "user_id": site.user_id,
    "title": site.title,
    "url": site.url,
    "word": site.word,
    "is_deleted": site.is_deleted,
    "version": site.version,
    "created_at": site.created_at,
    "updated_at": site.updated_at
  }


async def db_create_favo_site(db: AsyncSession, data: FavoSite) -> dict:
  user_id = data.get('user_id')
  title = data.get('title')
  url = data.get('url')
  word = data.get('word')
  print(f'user_id is {user_id}')
  
  result: Result = await db.execute(
    select(User).where(User.user_id == user_id)
  )
  user: Optional[Tuple[User]] = result.first()
  
  if user is None:
    raise HTTPException(
      status_code=404, detail="User not found, please correct user_id"
    )
    
  result: Result = await db.execute(
    select(Site).where(Site.user_id == user_id, Site.is_deleted == 0)
  )
  
  site: Optional[Tuple[Site]] = result.first()
  
  if site[0].title == title and site[0].url == url and site[0].word == word:
    raise HTTPException(
      status_code=400, detail="Site has already favorited"
    )
  
  site = Site()
  site.user_id = user_id
  site.title = title
  site.url = url
  site.word = word
  db.add(site)
  await db.commit()
  await db.refresh(site)
  print('site registration successfully')
  return site_serializer(site)


async def db_get_site(db: AsyncSession, site_id: UUID) -> Optional[Site]:
  result: Result = await db.execute(
    select(Site).filter(Site.site_id == site_id, Site.is_deleted == 0)
  )
  site: Optional[Tuple[Site]] = result.first()
  return site[0] if site is not None else None


async def db_unfavorite_site(db: AsyncSession, site: Site) -> dict:
  site.is_deleted = 1
  db.add(site)
  await db.commit()
  await db.refresh(site)
  return site_serializer(site)