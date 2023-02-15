from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource, reqparse # used for REST API building
from __init__ import db
from model.sport import sports

sport_api = Blueprint('sport_api', __name__,
                   url_prefix='/api/sport')

api = Api(sport_api)

class SportAPI(Resource):
    class _Create(Resource):
        def add(self):
            try: 
                "read data"
                body = request.get_json()
                
                Uid = body.get('Uid')
                Goal = body.get('Goal')
                Diff = body.get('Diff')
                Date = body.get('date')
                Status = body.get('status')
                
                uo = sports(Uid, Goal, Diff, Date, Status)
                
                goal = uo.create()
                
                return jsonify(goal.read())
            except Exception as e:
                return {'message':str(e)}
            
    class _Read(Resource):
        def get(self):
            goals = sports.query.all()    # read/extract all users from database
            json_ready = [ath.read() for ath in goals]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps




    api.add_resource(_Read, "/")
    api.add_resource(_Create, "/create")
                