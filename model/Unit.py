from math import hypot


class Unit:
    def __init__(self, x=0, y=0, hp=0, invis=False, typeId=0, idn=-1):
        self.idn = idn
        self.x = x
        self.y = y
        self.hp = hp
        self.invis = invis
        self.typeId = typeId

    def get_distance_to(self, x, y):
        return hypot(x - self.x, y - self.y)

    def get_distance_to_unit(self, unit):
        return self.get_distance_to(unit.x, unit.y)

    def get_squared_distance_to(self, x, y):
        x_range = x - self.x
        y_range = y - self.y
        return x_range * x_range + y_range * y_range

    def get_squared_distance_to_unit(self, unit):
        return self.get_squared_distance_to(unit.x, unit.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getHp(self):
        return self.hp

    def changeInvis(self):
        self.invis = not self.invis

    def getTypeId(self):
        return self.typeId