from equipments import sword
from equipments import armor

class basicUnit:
    def __init__(self, name):
        self.name = name
        self.maxHP = 0
        self.currHP = self.maxHP
        self.attack = 0

    def getName(self):
        return self.name
    
    def attackTarget(self, target):
        target.currHP -= self.attack
        print(f"{self.name} attacks {target.name} and dealt {self.attack} damage.")
        print("")

class playerHero(basicUnit):
    defaultHP = 100
    def __init__(self, name):
        super().__init__(name)
        self.maxHP = playerHero.defaultHP
        self.currHP = self.maxHP
        self.equippedWeapon = [1]
        self.equippedArmor = [1]
        self.money = 50
    
    def equipWeapon(self, weapon):
        self.equippedWeapon = weapon
        self.attack = self.equippedWeapon.damage
        print(f"{weapon.name} is now Equipped. Your attacks now deal {self.attack} damage.")
        print("")

    def equipArmor(self, armor):
        self.equippedArmor = armor
        self.maxHP = playerHero.defaultHP + self.equippedArmor.HPBoost
        self.currHP = self.maxHP
        print(f"{armor.name} is now Equipped. Your max HP is now {self.maxHP}")
        print("")

    def showInfo(self):
        print("Character details:")
        print(f"Name: {self.name}")
        print(f"Attack: {self.attack}")
        print(f"HP: {self.currHP}/{self.maxHP}")
        print(f"Gold: {self.money}")
        print("")

class enemyUnit(basicUnit):
    def __init__(self, name, maxHP, attack):
        super().__init__(name)
        self.maxHP = maxHP
        self.currHP = self.maxHP
        self.attack = attack

    def showInfo(self):
        print("Enemy details:")
        print(f"Name: {self.name}")
        print(f"Attack: {self.attack}")
        print(f"HP: {self.currHP}/{self.maxHP}")
        print("")

lastBoss = enemyUnit("Dio", 200, 20)

woodSword = sword("Wooden Sword", 10)