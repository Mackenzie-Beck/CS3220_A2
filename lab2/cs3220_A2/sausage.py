from thingClass import Thing

class Sausage(Thing):
    def __init__(self, weight=0, location=None):
        Thing.__init__(self)
        self.weight = weight
        self.calories = 100
