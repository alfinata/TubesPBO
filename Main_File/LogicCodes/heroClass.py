from LogicCodes.basicClass import basicUnit

# Class Basic Hero - Alfinata
class basicHero(basicUnit):
    def __init__(self, name, HPMax, ATK, DEF, money, heroRole):
        super().__init__(name, HPMax, ATK, DEF)
        self.energyMax = 100
        self.energyCurrent = self.energyMax
        self.money = money
        self.heroRole = heroRole
        self.inventory = Inventory([], [], [])
        self.critChance = 0
        
    def equipWeapon(self, weapon):
        self.weapon = weapon
        self.setATK(weapon.ATKBonus)

    def equipArmor(self, armor):
        self.changeMaxHP(100+armor.HPBonus)
        self.setDEF(armor.DEFBonus)
        
# Class Inventory - Rafif
class Inventory:
    def __init__(self, weapons, armors, potions):
        self.weapons = weapons
        self.armors = armors
        self.potions = potions