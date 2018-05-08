class Group:

    def __init__(self, ownership, unit_type):
        self.idn = -1
        self.unitList = []
        self.screenMinX = 84
        self.screenMinY = 84
        self.screenMaxX = 0
        self.screenMaxY = 0
        self.minimapMassX = 0
        self.minimapMassX = 0

        self.unit_type = unit_type
        self.ownership = ownership
        self.hp = 0
        # Need to check if True
        self.takenSlots = []
        self.build_progresses = []

    def addUnit(self, unit):
        self.unitList.append(unit)
        self.minimapMassX += unit.getX()
        self.minimapMassY += unit.getY()

        self.screenMinX = min(self.screenMinX, unit.getX())
        self.screenMinY = min(self.screenMinY, unit.getY())
        self.screenMaxX = max(self.screenMaxX, unit.getX())
        self.screenMaxY = max(self.screenMaxY, unit.getY())
        self.hp += unit.getHp()

