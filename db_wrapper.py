from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.model import *


class DBWrapper:
    def __init__(self, dbname, user, password, host, port, schema):
        self.engine = create_engine("postgres://{0}:{1}@{2}:{3}/{4}".format(user,
                                                                            password,
                                                                            host,
                                                                            port,
                                                                            dbname),
                                    connect_args={'options': '-csearch_path={}'.format(schema)})
        self.session = sessionmaker(bind=self.engine)()

    def get_partners(self):
        return self.session.query(PartnerIndividual).all()
