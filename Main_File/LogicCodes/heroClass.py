from LogicCodes.basicClass import *
from LogicCodes.consumablesClass import *

# Class Basic Hero - Alfinata
class basicHero(basicUnit):
    def __init__(self, name, HP, energy, role, evasion):
        super().__init__(name, HP, 0, 0, 10, evasion, 5)
        self.energyMax = energy
        self.energyCurrent = self.energyMax
        self.heroRole = role
        self.inventory = Inventory()
        
    def equipWeapon(self, weapon):
        self.weapon = weapon
        self.setATK(weapon.ATKBonus)

    def equipArmor(self, armor):
        self.changeMaxHP(100+armor.HPBonus)
        self.setDEF(armor.DEFBonus)

    def useEnergy(self, value):
        self.energyCurrent = self.energyCurrent - value

    def showInfo(self):
        print(f"{self.heroRole.checkRole()} {self.getName()}")
        print(f"HP: {self.getHPCurrent()}/{self.getHPMax()}")
        print(f"Energy: {self.energyCurrent}/{self.energyMax}")
        print(f"Attack Power: {self.getATK()}")
        print(f"Defense Power: {self.getDEF()}")
        print(f"Critical Chance: {self.critChance}")
        print(f"Evasion: {self.getEvade()}")

    def showHeroInfo(self):
        print(f"{self.heroRole.checkRole()} {self.getName()}")
        print(f"HP: {self.getHPCurrent()}/{self.getHPMax()}")
        print(f"Energy: {self.energyCurrent}/{self.energyMax}")
        print(f"Attack Power: {self.getATK()}")
        print(f"Defense Power: {self.getDEF()}")
        print(f"Critical Chance: {self.critChance}")
        print(f"Evasion: {self.getEvade()}")
        print(f"Money: {self.money}")
        
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