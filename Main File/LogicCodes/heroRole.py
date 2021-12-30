# Class Hero Role - Alfinata
class heroRole:
    def __init__(self, name):
        self.name = name

    def checkRole(self):
        return self.name

# Class Role Mage - Alfinata
class mageRole(heroRole):
    def __init__(self):
        super().__init__("Mage")

    def doFlameBurst(self):
        print("Flame burst activated")

    def doLightningStrike(self):
        print("Lightning Strike activated")

    def doWeaken(self):
        print("Weaken activated")

    def triggerArcaneMastery(self):
        print("Arcane Mastery triggered")

# Class Assassin Role - Din
class assassinSkillSet(heroRole):
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