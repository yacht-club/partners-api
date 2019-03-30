from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer
BASE = declarative_base()


class Model(BASE):
    __tablename__ = "testtable"
    id = Column(Integer, primary_key=True)
