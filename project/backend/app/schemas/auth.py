from pydantic import BaseModel
from decouple import config


CSRF_KEY = config('CSRF_KEY')


class CsrfSettings(BaseModel):
  secret_key: str = CSRF_KEY


class Csrf(BaseModel):
  csrf_token: str


class SuccessMSG(BaseModel):
  message: str
  
  

class Me(SuccessMSG):
  user_id: str