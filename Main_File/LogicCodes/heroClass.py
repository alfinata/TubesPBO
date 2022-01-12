from LogicCodes.basicClass import *
from LogicCodes.consumablesClass import *

# Class Basic Hero - Alfinata
class basicHero(basicUnit):
    def __init__(self, name, HP, energy, role, evasion):
        super().__init__(name, HP, 0, 0, 100, evasion, 5)
        self.energyMax = energy
        self.energyCurrent = self.energyMax
        self.heroRole = role
        self.inventory = Inventory()
        self.defaultHP = self.getHPMax()
        
    def equipWeapon(self, weapon):
        self.weapon = weapon
        self.setATK(weapon.ATKBonus)

    def equipArmor(self, armor):
        # baseHP = 100
        # if self.heroRole.checkRole() == "Warrior":
        #     baseHP = 120
        self.armor = armor
        self.changeMaxHP(self.defaultHP + armor.HPBonus)
        self.setDEF(armor.DEFBonus)

    def useEnergy(self, value):
        self.energyCurrent = self.energyCurrent - value

    def restoreEnergy(self, value):
        self.energyCurrent = self.energyCurrent + value
        if self.energyCurrent > self.energyMax:
            self.energyCurrent = self.energyMax

    def showInfo(self):
        print(f"{self.heroRole.checkRole()} {self.getName()}")
        print(f"HP: {self.getHPCurrent()}/{self.getHPMax()}")
        print(f"Energy: {self.energyCurrent}/{self.energyMax}")
        print(f"Attack Power: {self.getATK()}")
        print(f"Defense Power: {self.getDEF()}%")
        print(f"Critical Chance: {self.critChance}%")
        print(f"Evasion: {self.getEvade()}%")

    def showHeroInfo(self):
        print(f"{self.heroRole.checkRole()} {self.getName()}")
        print(f"HP: {self.getHPCurrent()}/{self.getHPMax()}")
        print(f"Energy: {self.energyCurrent}/{self.energyMax}")
        print(f"Attack Power: {self.getATK()}")
        print(f"Defense Power: {self.getDEF()}%")
        print(f"Critical Chance: {self.critChance}%")
        print(f"Evasion: {self.getEvade()}%")
        print(f"Money: {self.money} Gold")
        
# Class Inventory - Rafif
class Inventory:
    def __init__(self):
        self.potions = [ManaPot(0), HPPot(0), ATKPot(0)]

    def addConsumable(self, potion):
        if(potion == 1):
            self.potions[0].stack += 1
        elif(potion == 2):
            self.potions[1].stack += 1
        elif(potion == 3):
            self.potions[2].stack += 1

    def useConsumable(self, potion):
        if(potion == 1):
            self.potions[0].stack -= 1
        elif(potion == 2):
            self.potions[1].stack -= 1
        elif(potion == 3):
            self.potions[2].stack -= 1