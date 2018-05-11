import math
from utils import extramath, vector
from enum import Enum

class vectortype(Enum):
    XY = 'XY'
    RTHETA = 'RTHETA'


class Vector(object):
    
    def __init__(self, coords, mode):
        if mode == vectortype.RTHETA:
            self.r = coords[0]
            self.theta = coords[1]
            self.x = self.r * math.cos(math.radians(self.theta))
            self.y = self.r * math.sin(math.radians(self.theta))
        else:
            self.x = coords[0]
            self.y = coords[1]
            self.r = extramath.dist([0,0], [self.x, self.y])
            self.theta = math.degrees(math.atan2(self.y, self.x))
        self.xy = [self.x, self.y]
        self.rtheta = [self.r, self.theta]

    def listxy(self):
        return self.x, self.y

    def listrtheta(self):
        return self.r, self.theta

    def __repr__(self):
        return 'Vector(' + str(self.x) + ', ' + str(self.y) + ')'

    def __str__(self):
        return 'Vector(' + str(self.x) + ', ' + str(self.y) + ')'

    def __mul__(self, other):
        return vector.Vector((self.x * other, self.y * other), vectortype.XY)

    def __truediv__(self, other):
        return vector.Vector((self.x / other, self.y / other), vectortype.XY)

    def __add__(self, other):
        return vector.Vector((self.x + other.x, self.y + other.y), vectortype.XY)

    def __sub__(self, other):
        return vector.Vector((self.x - other.x, self.y - other.y), vectortype.XY)

    def __abs__(self):
        return vector.Vector((abs(self.x), abs(self.y)), vectortype.XY)

    def deadband_xy(self, deadband):
        return vector.Vector((extramath.deadband(self.x, deadband), extramath.deadband(self.y, deadband)), vectortype.XY)