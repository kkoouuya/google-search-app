from fastapi import APIRouter, Response, Request, Depends
from fastapi.encoders import jsonable_encoder
from fastapi_csrf_protect import CsrfProtect
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.auth import Csrf
from app.schemas.schemas import UserGETResponse, UserAuth,SuccessMSG
from app.cruds.auth import db_login, db_signup
from app.auth_utils import AuthJwtCsrf
from app.db import db_get

router = APIRouter()
auth = AuthJwtCsrf()


@router.get('/api/csrftoken', response_model=Csrf)
async def get_csrf_token(csrf_protect:CsrfProtect = Depends()):
  csrf_token = csrf_protect.generate_csrf()
  res = {"csrf_token": csrf_token}
  return res


@router.post("/api/register", response_model=UserGETResponse)
async def signup(request: Request, user: UserAuth, csrf_protect: CsrfProtect = Depends(), db: AsyncSession = Depends(db_get)):
  # csrf_token = csrf_protect.get_csrf_from_headers(request.headers)
  # csrf_protect.validate_csrf(csrf_token)
  user = jsonable_encoder(user)
  new_user = await db_signup(db, user)
  return new_user


@router.post("/api/login", response_model=str)
async def login(request: Request, response: Response, user: UserAuth, csrf_protect: CsrfProtect = Depends(), db: AsyncSession = Depends(db_get)):
  # csrf_token = csrf_protect.get_csrf_from_headers(request.headers)
  # csrf_protect.validate_csrf(csrf_token)
  user = jsonable_encoder(user)
  token = await db_login(db, user)
  # response.set_cookie(
  #   key="access_token", value=f"Bearer {token}", httponly=True, samesite="none", secure=True
  # )
  return token
  # return {"message": "Successfully logged_in"}


@router.post("/api/logout", response_model=SuccessMSG)
def logout(request: Request, response: Response, csrf_protect: CsrfProtect = Depends()):
  # csrf_token = csrf_protect.get_csrf_from_headers(request.headers)
  # csrf_protect.validate_csrf(csrf_token)
  response.set_cookie(
    key="access_token", value="", httponly=True, samesite="none", secure=True
  )
  return {"message": "Successfully logged-out"}


@router.get("/api/user", response_model=UserGETResponse)
def get_user_refresh_jwt(request: Request, response: Response):
  new_token, subject = auth.verify_update_jwt(request)
  response.set_cookie(
    key="access_token", value=f"Bearer {new_token}", httponly=True, samesite="none", secure=True
  )
  return {"email": subject}