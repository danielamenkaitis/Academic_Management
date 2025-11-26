from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# URL de conexão: substitua user, password e dbname
DATABASE_URL =  os.getenv("DATABASE_URL")

# Cria o engine (motor de conexão)
engine = create_engine(DATABASE_URL, echo=True)

# Cria a sessão para interagir com o banco
SessionLocal = sessionmaker(bind=engine)
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos ORM
Base = declarative_base()


