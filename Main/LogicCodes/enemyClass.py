from imghdr import what
import random
from LogicCodes.basicClass import basicUnit

class basicEnemy(basicUnit):
    def __init__(self, name, HP, ATK, DEF, money, evade, critChance):
        super().__init__(name, HP, ATK, DEF, money, evade, critChance)
        self.abilityCounter = 0
    
    def doSomething(self, target):
        pass

# Class Dummy - Alfinata
class dummyTarget(basicEnemy):
    def __init__(self):
        super().__init__("Dummy Target", 999, 0, 0, 0, 0, 0)

# Class Slime - Din
class slime(basicEnemy):
    def __init__(self):
        super().__init__("Slime", 30, 6, 0, 5, 0, 5)
    
    def doSomething(self, target):
        self.attackTarget(target)

# Class Goblin - Din
class goblin(basicEnemy):
    def __init__(self):
        super().__init__("Goblin", 40, 12, 10, 8, 0, 5)
    
    def doSomething(self, target):
        if (self.getHPCurrent()/self.getHPMax()) <= 0.5:
            if self.abilityCounter == 0:
                self.setDEF(self.getDEF() + 20)
                self.abilityCounter = 1
                print(f"Goblin senses danger! He increases his defense power to {self.getDEF()}")
            else: 
                self.attackTarget(target)
        else:
            self.attackTarget(target)

# Class Skeleton - Din
class skeleton(basicEnemy):
    def __init__(self):
        super().__init__("Skeleton", 65, 18, 0, 10, 0, 5)
    
    def doSomething(self, target):
        if (self.getHPCurrent()/self.getHPMax()) <= 1:
            if self.abilityCounter == 0:
                self.setEvade(25)
                self.abilityCounter = 1
                print(f"Skeleton uses Evade! His evasion chance is increased to {self.getEvade()}")
            else: 
                self.attackTarget(target)
        else:
            self.attackTarget(target)

# Class Vampire - Din
class vampire(basicEnemy):
    def __init__(self):
        super().__init__("Vampire", 100, 24, 20, 15, 10, 10)
    
    def doSomething(self, target):
        whatToDoProc = random.randrange(1, 101)
        if whatToDoProc > 40:
            self.attackTarget(target)
        else:
            dmgDealt = target.takeDamage(24)
            self.healHP(self.getHPMax()/10)
            print(f"Vampire uses Bloodsuck! He dealt {dmgDealt} damage and healed himself to {self.getHPCurrent()}/{self.getHPMax()}")

# Class Demon - Din
class demon(basicEnemy):
    def __init__(self):
        super().__init__("Demon", 125, 27, 25, 20, 0, 10)
    
    def doSomething(self, target):
        if self.abilityCounter == 0:
            whatToDoProc = random.randrange(1, 101)
            if whatToDoProc > 50:
                self.attackTarget(target)
            else:
                target.setATK(int(target.getATK() * 0.9))
                self.abilityCounter = 1
                print(f"Demon uses Scare! Hero's attack power has been reduced to {target.getATK()}")
        else:
            self.attackTarget(target)

# Class Demon King
class demonKing(basicEnemy):
    def __init__(self):
        super().__init__("Demon King", 250, 35, 30, 50, 20, 10)
    
    def doSomething(self, target):
        if self.abilityCounter == 0:
            target.setHPCurrent(int(target.getHPCurrent()*0.5))
            print(f"Demon King uses Doom! {target.getName()} loses half of its HP, with only {target.getHPCurrent()}/{target.getHPMax()} HP remaining.")
            self.abilityCounter = 1
        else:
            whatToDoProc = random.randrange(1, 4)
            if whatToDoProc == 1:
                self.attackTarget(target)
            elif whatToDoProc == 2:
                target.setATK(int(target.getATK() * 0.9, 0))
                print(f"Demon King uses Scare! Hero's attack power has been reduced to {target.getATK()}")
            else:
                dmgDealt = target.takeDamage(35)
                self.healHP(int(self.getHPMax() * 0.15, 0))
                print(f"Demon King uses Bloodsuck! He dealt {dmgDealt} damage and healed himself to {self.getHPCurrent()}/{self.getHPMax()}")