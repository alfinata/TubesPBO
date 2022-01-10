# Class Hero Role - Alfinata
class heroRole:
    def __init__(self, name, mana1, mana2):
        self.name = name
        self.manaCost1 = mana1
        self.manaCost2 = mana2

    def checkRole(self):
        return self.name

    def showAbilities(self):
        pass

    def doAbility1(self):
        pass

    def doAbility2(self):
        pass

# Class Role Mage - Alfinata
class mageRole(heroRole):
    def __init__(self):
        super().__init__("Mage", 20, 10)

    def showAbilities(self):
        print("1. Flame Burst - Deal 40 raw damage (20 energy)")
        print("2. Weaken - Reduce enemy defense (10 energy)")

    def doAbility1(self, hero, target):
        hero.useEnergy(self.manaCost1)
        dmgTaken = target.takeDamage(40)
        print(f"Flame Burst Shot! {target.getName()} suffers {dmgTaken} damage.")

    def doAbility2(self, hero, target):
        hero.useEnergy(self.manaCost2)
        if target.getDEF() >= 0:
            changeDEF = (target.getDEF() + 20)*-1
            target.setDEF(changeDEF)
        print(f"Enemy weakened! {target.getName()} defense has been lowered to {target.getDEF()}")

# Class Assassin Role - Din
class assassinRole(heroRole):
    def __init__(self):
        super().__init__("Assassin")

    def doDoubleSlash(self):
        print("DoubleSlash activated")

    def doPhantom(self):
        print("Phantom activated")

    def doLifesteal(self):
        print("Lifesteal activated")
    
    def triggerCunning(self):
        print("Cunning triggered")

        
# Class Warrior Role - Rafif
class warriorRole(heroRole):
    def __init__(self):
        super().__init__("Warrior")
        
    def doWhirlwind(self):
        print("Whirlwind activated")
    
    def doGroundSlam(self):
        print("Ground Slam activated")

    def doGuardStance(self):
        print("Guard Stance activated")

    def triggerPassiveRage(self):
        print("Passive Rage triggered")