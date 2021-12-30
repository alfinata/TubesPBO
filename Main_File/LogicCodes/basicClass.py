# Class Basic Unit - Alfinata
class basicUnit:
    def __init__(self, name, HPMax, ATK, DEF):
        self.__name = name
        self.__HPMax = HPMax
        self.__HPCurrent = self.__HPMax
        self.__ATK = ATK
        self.__DEF = DEF
        self.__evade = 0
        self.status = []

    def getName(self):
        return self.__name

    def getHPCurrent(self):
        return self.__HPCurrent

    def getHPMax(self):
        return self.__HPMax

    def setHPCurrent(self, newHP):
        self.__HPCurrent = newHP

    def changeMaxHP(self, newHP):
        currHP = self.__HPCurrent/self.__HPMax
        self.__HPMax = newHP
        self.__HPCurrent = currHP*self.__HPMax
    
    def getATK(self):
        return self.__ATK

    def setATK(self, newATK):
        self.__ATK = newATK

    def getATK(self):
        return self.__ATK
    
    def setDEF(self, newDEF):
        self.__DEF = newDEF

    def getDEF(self):
        return self.__DEF
    
    def setEvade(self, newEvade):
        self.__evade = newEvade

    def getEvade(self):
        return self.__evade
    
    def attackTarget(self, target):
        target.takeDamage(self.__ATK)

    def takeDamage(self, value):
        HPnow = self.getHPCurrent()
        damage = value*((100-self.getDEF())/100)
        HPthen = HPnow - damage
        self.setHPCurrent(HPthen)

# Class Basic Item - Alfinata
class basicItem:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
