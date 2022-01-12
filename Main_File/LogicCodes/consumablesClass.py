from LogicCodes.basicClass import *

# Class Consumable - Rafif
class Consumables(basicItem):
    def __init__(self, name, price, stack):
        super().__init__(name, price)
        self.stack = stack
        self.value = 0

# Class HP Potion - Rafif
class HPPot(Consumables):
    def __init__(self, stack):
        super().__init__("HP Potion", 10, stack)
        self.value = 30
    # def restoreHP():

# Class Mana Potion - Rafif
class ManaPot(Consumables):
    def __init__(self, stack):
        super().__init__("Mana Potion", 10, stack)
        self.value = 25
    # def restoreMana():

# Class ATK Potion - Rafif
class ATKPot(Consumables):
    def __init__(self, stack):
        super().__init__("ATK Potion", 10, stack)
        self.value = 10
    # def bonusATK():
