from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_restful import reqparse
from helpers import *

app = Flask(__name__)
api = Api(app, prefix="/api/v1")

parser = reqparse.RequestParser()
parser.add_argument("sentence", type=str, help="sentence or words should be unicode text", location='form')


class Refined(Resource):
    def get(self):
        return {"message": "Welcome to Refined API.", "status": 200}

    def post(self):
        args = parser.parse_args()

        text = args["sentence"]
        if text:
            result = get_refined(text)
            return jsonify(result)
        else:
            return {"sentence parameter is missing": 404}


api.add_resource(Refined, "/refined")


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', threaded=False, processes=1)
