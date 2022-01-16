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
        print("1. Flame Burst - Deal 45 raw damage (20 energy)")
        print("2. Weaken - Reduce enemy defense (10 energy)")

    def doAbility1(self, hero, target):
        hero.useEnergy(self.manaCost1)
        dmgTaken = int(target.takeDamage(45))
        print(f"Flame Burst Shot! {target.getName()} suffers {dmgTaken} damage.")

    def doAbility2(self, hero, target):
        hero.useEnergy(self.manaCost2)
        target.setDEF(target.getDEF() - 25)
        print(f"Enemy weakened! {target.getName()} defense has been lowered to {target.getDEF()}")

# Class Assassin Role - Din
class assassinRole(heroRole):
    def __init__(self):
        super().__init__("Assassin", 20, 10)

    def showAbilities(self):
        print(f"1. Lifesteal - Attack with lifesteal (20 energy)")
        print(f"2. Phantom - Increase critical chance (10 energy)")

    def doAbility1(self, hero, target):
        hero.useEnergy(self.manaCost1)
        dmgTaken = int(target.takeDamage(hero.getATK()))
        hero.healHP(dmgTaken)
        print(f"Lifesteal done succesfully! {target.getName()} suffers {dmgTaken} damage, ")
        print(f"and {hero.getName()} heals {dmgTaken} HP.")

    def doAbility2(self, hero, target):
        hero.useEnergy(self.manaCost2)
        hero.critChance = int(hero.critChance + ((100 - hero.critChance) * 25/100))
        print(f"{hero.getName()} succesfully used phantom.")
        print(f"His critical chance is now {hero.critChance}%")
        
# Class Warrior Role - Rafif
class warriorRole(heroRole):
    def __init__(self):
        super().__init__("Warrior", 20, 10)
        
    def showAbilities(self):
        print(f"1. Whirlwind - Deals 2x damage (20 energy)")
        print(f"2. Guard Stance - Increase defense (10 energy)")

    def doAbility1(self, hero, target):
        hero.useEnergy(self.manaCost1)
        dmgGiven = int(target.takeDamage(2 * hero.getATK()))
        print(f"Whirlwind hits {target.getName()}, dealing {dmgGiven} damage.")
        
    def doAbility2(self, hero, target):
        hero.useEnergy(self.manaCost2)
        baseDEF = hero.getDEF()
        inverse = 100 - baseDEF
        added = inverse * 15/100
        increasedDEF = baseDEF + added
        hero.setDEF(int(increasedDEF))
        print(f"Guard stance is activated! {hero.getName()} defense has been increased to {increasedDEF}")