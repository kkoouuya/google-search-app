from typing import Optional, Tuple
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.model import User
from app.schemas.schemas import UserAuth
from app.auth_utils import AuthJwtCsrf


auth = AuthJwtCsrf()


def user_serializer(user) -> dict:
  return {
    "user_id": user.user_id,
    "username": user.username,
    "email": user.email,
    "password": user.password,
    "is_deleted": user.is_deleted,
    "version": user.version,
    "created_at": user.created_at,
    "updated_at": user.updated_at
  }


async def db_signup(db: AsyncSession, data: UserAuth) -> dict:
  email = data.get('email')
  password = data.get('password')
  result: Result = await db.execute(
    select(User).where(User.email == email)
  )
  overlaped_email = result.first()
  
  if overlaped_email is not None:
    raise HTTPException(status_code=400, detail="Email is already be used")
  if not password or len(password) < 6:
    raise HTTPException(status_code=400, detail="Password too short")
  
  user = User()
  user.email = email
  user.password = auth.generate_hashed_pw(password)
  db.add(user)
  await db.commit()
  await db.refresh(user)
  print('Registration Successfully')
  
  return user_serializer(user)


async def db_login(db: AsyncSession, data: UserAuth) -> str:
  email = data.get('email')
  password = data.get('password')
  
  result: Result = await db.execute(
    select(User).where(User.email == email)
  )
  user: Optional[Tuple[User]] = result.first()
  if user is None:
    raise HTTPException(
      status_code=401, detail="Invalid email"
    )
  if not auth.verify_pw(password, user[0].password):
    raise HTTPException(
      status_code=401, detail="Invalid password"
    )
  token = auth.encode_jwt(user[0].email)
  return token