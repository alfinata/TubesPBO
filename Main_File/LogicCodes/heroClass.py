from LogicCodes.basicClass import *
from LogicCodes.consumablesClass import *

# Class Basic Hero - Alfinata
class basicHero(basicUnit):
    def __init__(self, name, HPMax, ATK, DEF, money, heroRole):
        super().__init__(name, HPMax, ATK, DEF)
        self.energyMax = 100
        self.energyCurrent = self.energyMax
        self.money = money
        self.heroRole = heroRole
        self.inventory = Inventory()
        self.critChance = 0
        
    def equipWeapon(self, weapon):
        self.weapon = weapon
        self.setATK(weapon.ATKBonus)

    def equipArmor(self, armor):
        self.changeMaxHP(100+armor.HPBonus)
        self.setDEF(armor.DEFBonus)
        
# Class Inventory - Rafif
class Inventory:
    def __init__(self):
        self.weapons = []
        self.armors = []
        self.potions = [ManaPot(0), HPPot(0), ATKPot(0)]

    def addWeapon(self, weapon):
        self.weapons.append(weapon)

    def removeWeapon(self, weapon):
        self.weapons.remove(weapon)

    def addArmor(self, armor):
        self.armors.append(armor)

    def removeArmor(self, armor):
        self.armors.remove(armor)

    def addConsumable(self, potion):
        if(potion == 1):
            self.potions[0] += 1
        elif(potion == 2):
            self.potions[1] += 1
        elif(potion == 3):
            self.potions[2] += 1

    def useConsumable(self, potion):
        if(potion == 1):
            self.potions[0] -= 1
        elif(potion == 2):
            self.potions[1] -= 1
        elif(potion == 3):
            self.potions[2] -= 1