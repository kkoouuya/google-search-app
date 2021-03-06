from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

ASYNC_DB_URL = "mysql+aiomysql://root@mysql:3306/googleserachapp?charset=utf8"

async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
async_session = sessionmaker(autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession)


async def db_get():
  async with async_session() as session:
    yield session