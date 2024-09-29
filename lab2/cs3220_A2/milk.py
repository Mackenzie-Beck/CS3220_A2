from thingClass import Thing

class Milk(Thing):
    def __init__(self, weight=0,location=None):
        self.alive = False
        self.name = 'milk'
        self.calories = 150
        self.weight = weight
        self.location = location