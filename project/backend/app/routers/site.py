from typing import List, Optional
from fastapi import APIRouter, Response, Request, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi_csrf_protect import CsrfProtect
from sqlalchemy.ext.asyncio import AsyncSession
from app.cruds.site import db_create_favo_site, db_get_site, db_unfavorite_site, db_get_favorite_site
from app.schemas.site import SiteBase, FavoSite, Site
from app.auth_utils import AuthJwtCsrf
from app.scraper import Scraper
from app.db import db_get
from uuid import UUID


router = APIRouter()
auth = AuthJwtCsrf()
scraper = Scraper()


@router.post('/api/scrape/', response_model=List[SiteBase])
async def scrape_site(request: Request, keyword: Optional[str] =None):
  auth.verify_jwt(request)
  sites = scraper.google_search(keyword)
  return sites


@router.get('/api/favorite/', response_model=Optional[List[Site]])
async def get_favo_site(request: Request, db: AsyncSession = Depends(db_get)):
  new_token, subject = auth.verify_update_jwt(request)
  return await db_get_favorite_site(db, email=subject)


@router.post('/api/register/favosite', response_model=Site)
async def create_favo_site(request: Request, response: Response, data: FavoSite, csrf_protect:CsrfProtect = Depends(), db: AsyncSession = Depends(db_get)):
  csrf_token = csrf_protect.get_csrf_from_headers(request.headers)
  csrf_protect.validate_csrf(csrf_token)
  data = jsonable_encoder(data)
  favorite_site = await db_create_favo_site(db, data)
  return favorite_site


@router.put('/api/favorite/{site_id}', response_model=Optional[List[Site]])
async def unfavorite_site(request: Request, response: Response, site_id: UUID, csrf_protect:CsrfProtect = Depends(), db: AsyncSession = Depends(db_get)):
  csrf_token = csrf_protect.get_csrf_from_headers(request.headers)
  csrf_protect.validate_csrf(csrf_token)
  new_token, subject = auth.verify_update_jwt(request)
  site = await db_get_site(db, site_id=site_id)
  if site is None:
    raise HTTPException(status_code=404, detail="Site not found")
  await db_unfavorite_site(db, site)
  
  return await db_get_favorite_site(db, email=subject)