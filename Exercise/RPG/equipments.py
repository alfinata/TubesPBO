class item:
    def __init__(self, name):
        self.name = name

class sword(item):
    type = "Sword"

    def __init__(self, name, dmg):
        super().__init__(name)
        self.damage = dmg

    def showInfo(self):
        print(f"{sword.type} name is {self.name}.")
        print(f"This sword deals {self.damage} damage.")
        print("")
        
class armor(item):
    type = "Armor"

    def __init__(self, name, hpboost):
        super().__init__(name)
        self.HPBoost = hpboost

    def showInfo(self):
        print(f"{armor.type} name is {self.name}.")
        print(f"This increases your maximum health by {self.HPBoost}.")
        print("")