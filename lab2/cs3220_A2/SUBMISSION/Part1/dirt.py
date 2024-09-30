from thingClass import Thing

class Dirt(Thing):
    def __init__(self, location=None):
        Thing.__init__(self)
        self.location = location
        self.name = 'dirt'
        self.alive = False


        