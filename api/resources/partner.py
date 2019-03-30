from flask_restful import Resource, reqparse
from flask import current_app, request

from json import loads


class Partner(Resource):

    def __init__(self):
        self.get_parser = reqparse.RequestParser()

        self.get_parser.add_argument("name", type=str, required=False, location="args")

    def get(self, partner_ext_id=None):
        args = self.get_parser.parse_args()
        if partner_ext_id is None:
            partners = current_app.db_wrapper.get_partners(args["name"])
            if partners:
                return {"partners": partners}, 200
            return {"message": "partners not found"}, 404
        else:
            partner = current_app.db_wrapper.get_partner_by_id(partner_ext_id)
            if partner:
                return {"partner": partner}, 200
            return {"message": "partner not found"}, 404

    def post(self):
        data = loads(request.data)
        res = current_app.db_wrapper.create_partner(data)
        return res
