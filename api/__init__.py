from flask import Flask, current_app
from flask_restful import Api
from flask_cors import CORS
from api.resources import Partner, User
from db_wrapper import DBWrapper

from config import DATABASE, USER, PASSWORD, HOST, PORT, SCHEMA


def create_app():
    app = Flask(__name__)

    cors = CORS(app, resources={r"*": {"origins": "*"}})

    with app.app_context():
        current_app.db_wrapper = DBWrapper(DATABASE, USER, PASSWORD, HOST, PORT, SCHEMA)

    api = Api(app)
    api.add_resource(Partner, "/partners", "/partners/<string:partner_ext_id>")
    api.add_resource(User, "/users", "/users/<string:user_ext_id>")

    return app
