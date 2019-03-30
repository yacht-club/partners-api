from flask_restful import Resource


class Partner(Resource):

    def get(self):
        return "Partner"
