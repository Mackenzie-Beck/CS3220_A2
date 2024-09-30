from food import Food

class Sausage(Food):
    def __init__(self, weight=0, location=None):
        Food.__init__(self)
        self.weight = weight
        self.calories = 100
        self.location = location