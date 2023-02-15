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
                
                return jsonify(user.read())
            except Exception as e:
                return {'message':str(e)}
                