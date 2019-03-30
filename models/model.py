from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import ARRAY

Base = declarative_base()


class PartnerType(Base):
    __tablename__ = "partner_type"

    name = Column(String, primary_key=True)
    description = Column(String)


class PartnerIndividual(Base):
    __tablename__ = "partners_individual"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    description = Column(String, nullable=True)
    tags = Column(ARRAY(String))
    ext_id = Column(String, nullable=False)


class PartnerLegal(Base):
    __tablename__ = "partners_legal "

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    inn = Column(String, nullable=False)
    site_url = Column(String, nullable=False)
    description = Column(String, nullable=True)
    tags = Column(ARRAY(String))
    ext_id = Column(String, nullable=False)


class RelPartnerType(Base):
    __tablename__ ="rel_partner_type"

    partner_ext_id = Column(String, primary_key=True)
    partner_type = Column(String, ForeignKey("partner_type.name"), nullable=False)




