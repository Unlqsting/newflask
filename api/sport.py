from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource, reqparse # used for REST API building
from __init__ import db
from model.sport import sports

sport_api = Blueprint('sport_api', __name__,
                   url_prefix='/api/sport')

api = Api(sport_api)

class SportAPI(Resource):
    class _Create(Resource):
        def post(self):
            try: 
                "read data"
                body = request.form
                
                goal = body.get('goal') 
                diff = body.get('diff')
                time = body.get('time')
                
                uo = sports(goal, diff)
                
                create = uo.create()
                
                return jsonify(create.read())
            except Exception as e:
                return {'message':str(e)}
            
    class _Read(Resource):
        def get(self):
            goals = sports.query.all()    # read/extract all users from database
            json_ready = [ath.read() for ath in goals]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps




    api.add_resource(_Read, "/")
    api.add_resource(_Create, "/create")
                