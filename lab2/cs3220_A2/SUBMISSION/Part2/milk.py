from food import Food

class Milk(Food):
    def __init__(self, weight=0,location=None):
        Food.__init__(self)
        self.calories = 150
        self.weight = weight
        self.location = location