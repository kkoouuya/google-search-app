from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi_csrf_protect import CsrfProtect
from fastapi_csrf_protect.exceptions import CsrfProtectError
from app.routers import auth, site
from app.schemas.auth import CsrfSettings, SuccessMSG


app = FastAPI()
app.include_router(auth.router)
app.include_router(site.router)
origins = ['http://localhost:3007']
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@CsrfProtect.load_config
def get_csrf_config():
  return CsrfSettings()


@app.exception_handler(CsrfProtectError)
def csrf_protect_exception_handler(request: Request, exc: CsrfProtectError):
  return JSONResponse(
    status_code=exc.status_code,
      content={ 'detail':  exc.message
    }
  )


@app.get('/', response_model=SuccessMSG)
def root():
  return {"message": "Hello World"}