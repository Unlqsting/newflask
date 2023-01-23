import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class Athlete(db.Model):
    __tablename__= "Elite"
   
    id = db.Column(db.Integer, primary_key=True)
    _Weight = db.Column(db.Integer, nullable=False)
    _Bench = db.Column(db.Integer, nullable=False)
    _Squat = db.Column(db.Integer, nullable=False)
    _Press = db.Column(db.Integer, nullable=False)
    _Pushup = db.Column(db.Integer, nullable=False)
   
    def __init__(self, Weight, Bench, Squat, Press, Pushup):
        self._Weight = Weight
        self._Bench = Weight + (50)
        self._Squat = Weight *(2)
        self._Press = Weight /(2)
        self._Pushup = Bench /(5)

    def __repr__(self):
        return "<Athlete(Weight='%s', Bench='%s', Squat='%s', Press='%s', Pushup='%s')>" % (
            self._Weight,
            self._Bench,
            self._Squat,
            self._Press,
            self._Pushup
        )
    
    # Getters:
    @property
    def Weight(self):
        return self._Weight
    
    @property
    def Bench(self):
        return self._Bench

    @property
    def Squat(self):
        return self._Squat   

    @property
    def Press(self):
        return self._Press 
    
    @property
    def Pushup(self):
        return self._Pushup 
   
    # Setters    
    @Weight.setter
    def Weight(self,weight):
        self._Weight = weight

    @Bench.setter
    def Bench(self, bench):
        self._Bench = bench

    @Squat.setter
    def Squat(self, squat):
        self._Squat = squat

    @Press.setter
    def Press(self, press):
        self._Press = press

    @Pushup.setter
    def Pushup(self, pushup):
        self.Pushup = pushup

    @property
    def dictionary(self):
        dict = {
            "Weight" : self.Weight,
            "Bench" : self.Bench,
            "Squat" : self.Squat,
            "Press" : self.Press,
            "Pushup" : self.Pushup,
        }
        return dict

    def __str__(self):
        return json.dumps(self.dictionary)
    
    def __repr__(self):
        return f'Athlete(Weight={self._Weight}, Bench={self._Bench}, Squat={self._Squat}, Press={self._Press}, Pushup={self._Pushup})'

    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            print("commit")
            return self
        except IntegrityError:
            print("issue")
            db.session.remove()
            return None

    def read(self):
        return {
            "Weight" : self.Weight,
            "Bench" : self.Bench,
            "Squat" : self.Squat,
            "Press" : self.Press,
            "Pushup" : self.Pushup,
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, Weight="", Bench="", Squat="", Press="", Pushup=""):
        """only updates values with length"""
        if len(Weight) > 0:
            self.name = Weight
        if len(Bench) > 0:
            self.uid = Bench
        if len(Squat) > 0:
            self.set_password(Squat)
        if len(Press) > 0:
            self.set_password(Press)
        if len(Squat) > 0:
            self.set_password(Squat)
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


def initAthletes():
    db.create_all()
    """Tester data for table"""
    Liav = Athlete(130, 180, 260, 65, 36)
    Noor = Athlete(190, 240, 380, 95, 48)
    Mort = Athlete(240, 290, 480, 120, 58)
    


    Athletes = [Liav, Noor, Mort]

    for athlete in Athletes:
        try:
            print("h")
            athlete.create()
        except IntegrityError:
            db.session.remove()
            print(f"Records, exist, duplicate data, or error: {athlete.id}")
