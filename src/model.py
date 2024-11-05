
from sqlalchemy import create_engine, Column, Float
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from uuid import uuid4


DATABASE_URL = "postgresql://postgres:Ahmed%4078@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Product(Base):
    __tablename__ = "test_products"
    guid = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    price = Column(Float, nullable=False)


Base.metadata.create_all(bind=engine)
