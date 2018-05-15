from pysc2.lib.features import PlayerRelative
from pysc2.lib import units

class Group:
    def __init__(self, ownership=PlayerRelative.SELF, unitType=0):  # 0 - undefind type
        self.idn = -1
        self.ownership = ownership
        self.unitType = unitType
        self.reset()
        # Need to check if True
        self.takenSlots = []
        self.build_progresses = []

    def addUnit(self, unit):
        self.unitList.append(unit)
        self.massPoint_m = [self.massPoint_m[0] + unit.getX(), self.massPoint_m[1] + unit.getY()]

        self.minPoint_s = [min(self.minPoint_s[0], unit.getX()), min(self.minPoint_s[1], unit.getY())]
        self.maxPoint_s = [max(self.maxPoint_s[0], unit.getX()), max(self.maxPoint_s[1], unit.getY())]

        self.hp += unit.getHp()

    def reset(self):
        self.unitList = []
        self.minPoint_s = [84, 84]
        self.maxPoint_s = [0, 0]
        self.massPoint_m = [0, 0]
        self.hp = 0

    def renew(self, units):
        self.reset()
        for unit in units:
            self.addUnit(unit)

    def getX(self):
        return self.massPoint_m[0] // len(self.unitList)

    def getY(self):
        return self.massPoint_m[1] // len(self.unitList)