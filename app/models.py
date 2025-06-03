from sqlalchemy import Column, String, ForeignKey, BigInteger, DateTime
#from .database import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import os
from dotenv import load_dotenv

load_dotenv()
Base = declarative_base()


class Job(Base):
    __tablename__ = "jobs"

    id = Column(BigInteger, primary_key=True, index=True)
    job_title = Column(String, index=True)

    # Relación con hired_employees
    employees = relationship("HiredEmployee", back_populates="job")


class Department(Base):
    __tablename__ = "departments"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String, nullable=False)

    # Relación con hired_employees
    employees = relationship("HiredEmployee", back_populates="department")


class HiredEmployee(Base):
    __tablename__ = "hired_employees"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    datetime = Column(DateTime, nullable=False)
    job_id = Column(BigInteger, ForeignKey("jobs.id"))
    department_id = Column(BigInteger, ForeignKey("departments.id"))

    # Relaciones
    job = relationship("Job", back_populates="employees")
    department = relationship("Department", back_populates="employees")


# Obtener las credenciales
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

SQLACHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port }/{db_name}"

engine = create_engine(SQLACHEMY_DATABASE_URL)
Base.metadata.create_all(bind=engine)
