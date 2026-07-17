from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mssql+pyodbc://sa:GumGum88_@localhost:1433/crud_db_python?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()