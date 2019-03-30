from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Sequence
from sqlalchemy.types import ARRAY

Base = declarative_base()

PARTNER_INDIVIDUAL_ID = Sequence('partners_individual_id_seq', start=1000)
PARTNER_LEGAL_ID = Sequence('partners_legal_id_seq', start=1000)


class PartnerType(Base):

    __tablename__ = "partner_type"

    name = Column(String, primary_key=True)
    description = Column(String)


class PartnerIndividual(Base):

    __tablename__ = "partners_individual"

    id = Column(Integer, PARTNER_INDIVIDUAL_ID, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    description = Column(String, nullable=True)
    tags = Column(ARRAY(String))
    ext_id = Column(String, nullable=False)

    def to_json(self):
        return {"name": self.name,
                "email": self.email,
                "description": self.description,
                "tags": self.tags,
                "ext_id": self.ext_id,
                "partner_type": "INDIVIDUAL"}


class PartnerLegal(Base):

    __tablename__ = "partners_legal"

    id = Column(Integer, PARTNER_LEGAL_ID, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    inn = Column(String, nullable=False)
    site_url = Column(String, nullable=False)
    description = Column(String, nullable=True)
    tags = Column(ARRAY(String))
    ext_id = Column(String, nullable=False)

    def to_json(self):
        return {"name": self.name,
                "inn": self.inn,
                "site_url": self.site_url,
                "description": self.description,
                "tags": self.tags,
                "ext_id": self.ext_id,
                "partner_type": "LEGAL"}


class RelPartnerType(Base):
    __tablename__ ="rel_partner_type"

    partner_ext_id = Column(String, primary_key=True)
    partner_type = Column(String, ForeignKey("partner_type.name"), nullable=False)




