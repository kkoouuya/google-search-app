from typing import List, Optional
from fastapi import APIRouter, Response, Request, Depends
from fastapi.encoders import jsonable_encoder
from fastapi_csrf_protect import CsrfProtect
from sqlalchemy.ext.asyncio import AsyncSession
from app.cruds.crud import db_create_favo_site
from app.schemas.schemas import SiteBase, FavoSite, Site
from app.auth_utils import AuthJwtCsrf
from app.scraper import Scraper
from app.db import db_get


router = APIRouter()
auth = AuthJwtCsrf()
scraper = Scraper()


@router.get('/api/scrape/', response_model=List[SiteBase])
async def get_site(request: Request, keyword: Optional[str] =None):
  auth.verify_jwt(request)
  sites = scraper.google_search(keyword)
  return sites


@router.post('/api/favorite', response_model=Site)
async def create_favo_site(request: Request, response: Response, data: FavoSite, csrf_protect:CsrfProtect = Depends(), db: AsyncSession = Depends(db_get)):
  csrf_token = csrf_protect.get_csrf_from_headers(request.headers)
  csrf_protect.validate_csrf(csrf_token)
  data = jsonable_encoder(data)
  favorite_site = await db_create_favo_site(db, data)
  return favorite_site