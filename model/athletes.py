from athletes import Column, Integer, String, Boolean
from .. import db
import json

class Athlete(db.Model):
    _tablename_= "Athletes"
   
    id = Column(Integer, primary_key=True)
    _text = Column(String(255), nullable=False)
    _completed = Column(Boolean, nullable=False)
   
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