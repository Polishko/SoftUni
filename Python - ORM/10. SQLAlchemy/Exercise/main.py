from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "postgresql+psycopg2://postgres:password@localhost/sql_Alchemy_db3"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
