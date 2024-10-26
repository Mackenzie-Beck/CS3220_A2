class manhattanDistance():
    @staticmethod
    def calc(coord1, coord2):
        return abs(coord2 - coord1)

    @staticmethod
    def calc(coord1, coord2):
        return abs(coord2[0] - coord1[0]) + abs(coord2[1] - coord1[1])