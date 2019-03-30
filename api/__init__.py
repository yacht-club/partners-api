from flask import Flask, current_app
from flask_restful import Api

from api.resources import Partner


def create_app():

    app = Flask(__name__)

    api = Api(app)
    api.add_resource(Partner, "/test")

    return app
