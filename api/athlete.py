from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from __init__ import db
from model.athletes import Athlete

athlete_api = Blueprint('athlete_api', __name__,
                   url_prefix='/api/athlete')

api = Api(athlete_api)

class AthleteAPI(Resource):
    # resources
    class _Create(Resource):
        pass # Create

    class _Read(Resource):
        def get(self):
            athletes = Athlete.query.all()    # read/extract all users from database
            json_ready = [ath.read() for ath in athletes]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps




    api.add_resource(_Read, "/")



