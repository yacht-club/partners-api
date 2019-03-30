from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.model import *

from uuid import uuid4


class DBWrapper:
    def __init__(self, dbname, user, password, host, port, schema):
        self.engine = create_engine("postgres://{0}:{1}@{2}:{3}/{4}".format(user,
                                                                            password,
                                                                            host,
                                                                            port,
                                                                            dbname),
                                    connect_args={'options': '-csearch_path={}'.format(schema)})
        self.session = sessionmaker(bind=self.engine)()

    def get_partners(self, name):
        if name:
            legal_partners = self.session.query(PartnerLegal).\
                             filter(PartnerLegal.name.like("%{0}%".format(name))).all()
            individual_partners = self.session.query(PartnerIndividual).\
                                  filter(PartnerIndividual.name.like("%{0}%".format(name))).all()
        else:
            legal_partners = self.session.query(PartnerLegal).all()
            individual_partners = self.session.query(PartnerIndividual).all()

        return [p.to_json() for p in legal_partners + individual_partners]

    def create_partner(self, data):
        if data["partner_type"] == "LEGAL":
            return self._create_legal_partner(data)
        elif data["partner_type"] == "INDIVIDUAL":
            return self._create_individual_partner(data)
        else:
            raise Exception("Incorrect partner_type")

    def _create_legal_partner(self, data):
        name = data["name"]
        inn = data["inn"]
        site_url = data["site_url"]
        description = data.get("description")
        tags = data.get("tags", [])
        ext_id = str(uuid4())
        p = PartnerLegal(name=name, inn=inn, site_url=site_url, description=description, tags=tags, ext_id=ext_id)
        rel_p = RelPartnerType(partner_ext_id=ext_id, partner_type="LEGAL")

        self.session.add(p)
        self.session.add(rel_p)
        self.session.commit()

        return p.to_json()

    def _create_individual_partner(self, data):
        name = data["name"]
        description = data.get("description")
        tags = data.get("tags", [])
        email = data["email"]
        phone = data.get("phone")
        ext_id = str(uuid4())
        p = PartnerIndividual(name=name, email=email, description=description, tags=tags, phone=phone, ext_id=ext_id)
        rel_p = RelPartnerType(partner_ext_id=ext_id, partner_type="INDIVIDUAL")

        self.session.add(p)
        self.session.add(rel_p)
        self.session.commit()

        return p.to_json()

    def get_partner_by_id(self, ext_id):
        partner_type = self.session.query(RelPartnerType.partner_type).\
                       filter(RelPartnerType.partner_ext_id == ext_id).\
                       first()[0]

        if partner_type is None:
            return None

        if partner_type == "LEGAL":
            partner = self.session.query(PartnerLegal).filter(PartnerLegal.ext_id == ext_id).first().to_json()
        else:
            partner = self.session.query(PartnerIndividual).filter(PartnerIndividual.ext_id == ext_id).first().to_json()

        return partner

    def create_user(self, data):
        username = data["username"]
        role = data["role"]
        user_ext_id = str(uuid4())
        user = User(username=username, role=role, user_ext_id=user_ext_id)

        self.session.add(user)
        self.session.commit()

        return user.to_json()

    def get_users(self, username, role):
        users = self.session.query(User)
        if username:
            users = users.filter(User.username.like("%{0}%".format(username)))
        if role:
            users = users.filter(User.role.like("%{0}%".format(role)))

        return [user.to_json() for user in users.all()]

    def get_user_by_id(self, user_ext_id):
        user = self.session.query(User).filter(User.user_ext_id == user_ext_id).first()
        if user is None:
            return None

        return user.to_json()
