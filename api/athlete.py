from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from .. import db
from ..model.athletes import Athlete

from model.athletes import Athlete

athlete_api = Blueprint('athlete_api', __name__,
                   url_prefix='/api/athlete')

api = Api(athlete_api)

athlete_bp = Blueprint("athlete", __name__)
athlete_api = api(athlete_bp)

class AthleteAPI(Resource):
    def get(self, Weight, Bench, Squat, Press, Pushup):
        todo = db.session.query(Athlete).get(Weight)
        if Athlete:
            return Athlete.to_dict()
        return {"message": "athlete not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Bench", required=True, type=str)
        args = parser.parse_args()

        Athlete = Athlete(args["Bench"])
        try:
            db.session.add(Athlete)
            db.session.commit()
            return Athlete.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Weight", required=True, type=int)
        args = parser.parse_args()

        try:
            todo = db.session.query(Athlete).get(args["Weight"])
            if Athlete:
                self._Bench = True
                db.session.commit()
            else:
                return {"message": "todo not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Weight", required=True, type=int)
        args = parser.parse_args()

        try:
            Athlete = db.session.query(Athlete).get(args["Weight"])
            if Athlete:
                db.session.delete(Athlete)
                db.session.commit()
                return Athlete.to_dict()
            else:
                return {"message": "athlete not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500


class athleteListAPI(Resource):
    def get(self):
        Athletes = db.session.query(Athlete).all()
        return [Athlete.to_dict() for Athlete in Athletes]


athlete_api.add_resource(AthleteAPI, "/athlete")
athlete_api.add_resource(athleteListAPI, "/athleteList")



