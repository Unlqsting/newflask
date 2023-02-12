import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class Athlete(db.Model):
    __tablename__= "Elite"
   
    id = db.Column(db.Integer, primary_key=True, unique = True)
    _Age = db.Column(db.Integer, nullable=False)
    _Weight = db.Column(db.Integer, nullable=False)
    _Bench = db.Column(db.Integer, nullable=False)
    _Squat = db.Column(db.Integer, nullable=False)
    _Pullup = db.Column(db.Integer, nullable=False)
    _Mile = db.Column(db.Integer, nullable=False)
   
    def __init__(self, Age, Weight, Bench, Squat, Pullup, Mile):
        self._Age = Age
        self._Weight = Weight
        self._Bench = Bench
        self._Squat = Squat
        self._Pullup = Pullup
        self._Mile = Mile

    def __repr__(self):
        return "<Athlete(Age='%s', Weight='%s', Bench='%s', Squat='%s', Pullup='%s', Mile='%s')>" % (
            self._Age,
            self._Weight,
            self._Bench,
            self._Squat,
            self._Pullup,
            self._Mile
        )
    
    # Getters:
    @property
    def Age(self):
        return self._Age
    
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
    def Pullup(self):
        return self._Pullup 
    
    @property
    def Mile(self):
        return self._Mile 
   
    # Setters    
    @Age.setter
    def Age(self, age):
        self._Age = age

    @Weight.setter
    def Weight(self,weight):
        self._Weight = weight

    @Bench.setter
    def Bench(self, bench):
        self._Bench = bench

    @Squat.setter
    def Squat(self, squat):
        self._Squat = squat

    @Pullup.setter
    def Pullup(self, pullup):
        self._Press = pullup

    @Mile.setter
    def Mile(self, mile):
        self.Mile = mile

    @property
    def dictionary(self):
        dict = {
            "Age" : self.Age,
            "Weight" : self.Weight,
            "Bench" : self.Bench,
            "Squat" : self.Squat,
            "Pullup" : self.Pullup,
            "Mile" : self.Mile,
        }
        return dict

    def __str__(self):
        return json.dumps(self.dictionary)
    
    def __repr__(self):
        return f'Athlete(Age={self._Age}, Weight={self._Weight}, Bench={self._Bench}, Squat={self._Squat}, Pullup={self._Pullup}, Mile={self._Mile})'

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
            "Age" : self.Age,
            "Weight" : self.Weight,
            "Bench" : self.Bench,
            "Squat" : self.Squat,
            "Pullup" : self.Pullup,
            "Mile" : self.Mile
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, Age="", Weight="", Bench="", Squat="", Pullup="", Mile=""):
        """only updates values with length"""
        if len(Age) > 0:
            self.Age = Age
        if len(Weight) > 0:
            self.Weight = Weight
        if len(Bench) > 0:
            self.Bench = Bench
        if len(Squat) > 0:
            self.Squat(Squat)
        if len(Pullup) > 0:
            self.Pullup(Pullup)
        if len(Mile) > 0:
            self.Mile(Mile)
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


def initAthletes():
    with app.app_context():
        db.init_app(app)
        db.create_all()
        """Tester data for table"""
        Liav = Athlete(16, 130, 180, 260, 12, 6.42)
        Noor = Athlete(17, 190, 240, 380, 15, 7.35)


        Athletes = [Liav, Noor]

        for athlete in Athletes:
            try:
                print("h")
                athlete.create()
            except IntegrityError:
                db.session.remove()
                print(f"Records, exist, duplicate data, or error: {athlete.id}")
