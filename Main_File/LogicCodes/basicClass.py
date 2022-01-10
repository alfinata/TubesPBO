import random

# Class Basic Unit - Alfinata
class basicUnit:
    def __init__(self, name, HPMax, ATK, DEF, money, evade, critChance):
        self.__name = name
        self.__HPMax = HPMax
        self.__HPCurrent = self.__HPMax
        self.__ATK = ATK
        self.__DEF = DEF
        self.__evade = evade
        self.status = []
        self.critChance = critChance
        self.money = money

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
        evadeProc = random.randrange(1, 101)
        if evadeProc > target.getEvade():
            critProc = random.randrange(1, 101)
            if critProc < self.critChance:
                dmgDealt = target.takeDamage(self.__ATK*2.5)
                print(f"{self.getName()} attacked {target.getName()} and scores a CRITICAL HIT!, dealing {dmgDealt} damage.\n")
            else:
                dmgDealt = target.takeDamage(self.__ATK)
                print(f"{self.getName()} attacked {target.getName()}, dealing {dmgDealt} damage.\n")
        else:
            print(f"Too bad! {target.getName()} completely evaded the attack!")

    def takeDamage(self, value):
        HPnow = self.getHPCurrent()
        damage = value*((100-self.getDEF())/100)
        HPthen = HPnow - damage
        if HPthen < 0:
            HPthen = 0
        self.setHPCurrent(HPthen)
        return damage

    def healHP(self, value):
        HPnow = self.getHPCurrent()
        HPthen = HPnow + value
        if HPthen > self.getHPMax():
            HPthen = self.getHPMax()
        self.setHPCurrent(HPthen)

    def showInfo(self):
        print(f"{self.getName()}")
        print(f"HP: {self.getHPCurrent()}/{self.getHPMax()}")
        print(f"Attack Power: {self.getATK()}")
        print(f"Defense Power: {self.getDEF()}")
        print(f"Critical Chance: {self.critChance}")
        print(f"Evasion: {self.getEvade()}")

# Class Basic Item - Alfinata
class basicItem:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
