from thingClass import Thing

class Food(Thing):
    def __init__(self, location=None):
        Thing.__init__(self)
        self.weight = 0 #not done
        self.calories = 0 #not done