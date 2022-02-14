from sqlalchemy import create_engine
from models.model import Base

DB_URL = "mysql+pymysql://root@mysql:3306/googleserachapp?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
  Base.metadata.drop_all(bind=engine)
  Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
  reset_database()