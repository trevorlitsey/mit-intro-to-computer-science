class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, otherCoord):
        return bool(self.x == otherCoord.x and self.y == otherCoord.y)

    def __repr__(self):
        return 'Coordinate(' + str(self.x) + ',' + str(self.y) + ')'
