from flask_restful import Resource
from flask import current_app

    
class Partner(Resource):

    def get(self):

        partners = current_app.db_wrapper.get_partners()
        res = []
        for partner in partners:
            res.append({"name": partner.name, "email": partner.email})

        return {"partners": res}
