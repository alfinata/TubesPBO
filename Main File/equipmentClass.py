from basicClass import basicItem

# Class Equipment - Rafif
class Equipment(basicItem):
    def __init__(self, name, price, classRole):
        super().__init__(name, price)
        self.classRole = classRole

    def specialEffects(self):
        pass

# Class Armor - Rafif
class Armor(Equipment):
    def __init__(self, name, price, classRole, HPBonus, DEFBonus):
        super().__init__(name, price, classRole)
        self.HPBonus = HPBonus
        self.DEFBonus = DEFBonus

# Class Weapon - Rafif
class Weapon(Equipment):
    def __init__(self, name, price, classRole, ATKBonus):
        super().__init__(name, price, classRole)
        self.ATKBonus = ATKBonus 