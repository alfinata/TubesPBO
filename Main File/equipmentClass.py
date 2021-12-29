from basicClass import basicItem

# Class Equipment - Rafif
class Equipment(basicItem):
    def __init__(self, name, price, classRole):
        super().___init__(name, price)
        self.classRole = classRole

# Class Armor - Rafif
class Armor(Equipment):
    def __init__(self, name, price, HPBonus, DEFBonus):
        super().__init__(name, price)
        self.HPBonus = HPBonus
        self.DEFBonus = DEFBonus

# Class Weapon - Rafif
class Weapon(Equipment):
    def __init__(self, name, price, ATKBonus):
        super().__init__(name, price)
        self.ATKBonus = ATKBonus