from flask_restful import Resource, reqparse
from flask import current_app


class User(Resource):

    def __init__(self):
        self.get_parser = reqparse.RequestParser()
        self.get_parser.add_argument("username", type=str, required=False, location="args")
        self.get_parser.add_argument("role", type=str, required=False, location="args")

        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument("username", type=str, required=True, location="json")
        self.post_parser.add_argument("role", type=str, required=True, location="json")

    def get(self, user_ext_id=None):
        args = self.get_parser.parse_args()
        if user_ext_id is None:
            partners = current_app.db_wrapper.get_users(args["username"], args["role"])
            if partners:
                return {"users": partners}, 200
            return {"message": "users not found"}, 404
        else:
            partner = current_app.db_wrapper.get_user_by_id(user_ext_id)
            if partner:
                return {"user": partner}, 200
            return {"message": "user not found"}, 404

    def post(self):
        data = self.post_parser.parse_args()
        user = current_app.db_wrapper.create_user(data)
        return user
