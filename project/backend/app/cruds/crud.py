from typing import List, Optional, Tuple
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
  email = data.get('email')
  title = data.get('title')
  url = data.get('url')
  word = data.get('word')
  
  result: Result = await db.execute(
    select(User.user_id).where(User.email == email)
  )
  user_id: Optional[Tuple[UUID]] = result.first()
  print(user_id)
  print(user_id[0])
  print(type(user_id))
  
  if user_id is None:
    raise HTTPException(
      status_code=404, detail="User not found, please correct user_id"
    )
    
  result: Result = await db.execute(
    select(Site).where(Site.user_id == user_id[0], Site.title == title, Site.url == url, Site.word == word, Site.is_deleted == 0)
  )
  
  site: Optional[Tuple[Site]] = result.first()
  
  if site is None:
    site = Site()
    site.user_id = user_id[0]
    site.title = title
    site.url = url
    site.word = word
    db.add(site)
    await db.commit()
    await db.refresh(site)
    return site_serializer(site)
  else:
    raise HTTPException(
      status_code=400, detail="Site has already favorited"
    )


async def db_get_site(db: AsyncSession, site_id: UUID) -> Optional[List[Site]]:
  result: Result = await db.execute(
    select(Site).filter(Site.site_id == site_id, Site.is_deleted == 0)
  )
  site: Optional[List[Site]] = result.first()
  return site[0] if site is not None else None


async def db_get_favorite_site(db: AsyncSession, email: str) -> Optional[List[Site]]:
  result: Result = await db.execute(
    select(Site).filter(
      Site.user_id == 
      (select(User.user_id).filter(User.email == email)),
      Site.is_deleted == 0
    )
  )
  site: Optional[List[Site]] = result.all()
  items = []
  for si in site:
    for s in si:
      items.append(site_serializer(s))
  return items if site is not None else None


async def db_unfavorite_site(db: AsyncSession, site: Site) -> dict:
  site.is_deleted = 1
  db.add(site)
  await db.commit()
  await db.refresh(site)
  return site_serializer(site)