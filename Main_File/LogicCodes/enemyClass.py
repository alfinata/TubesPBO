from LogicCodes.basicClass import basicUnit

# Class Slime - Alfinata
class slime(basicUnit):
    def __init__(self, name, HPMax, ATK, DEF):
        super().__init__(name, HPMax, ATK, DEF)

# Class Goblin - Din
class goblin(basicUnit):
    def __init__(self, name, HPMax, ATK, DEF):
        super().__init__(name, HPMax, ATK, DEF)


# Class Skeleton - Din
class skeleton(basicUnit):
    def __init__(self, name, HPMax, ATK, DEF):
        super().__init__(name, HPMax, ATK, DEF)
    
    def dodge(self):
        print("Dodge")

# Class Vampire - Din
class vampire(basicUnit):
    def __init__(self, name, HPMax, ATK, DEF):
        super().__init__(name, HPMax, ATK, DEF)
    
    def lifesteal(self):
        print("LiveSteal")

# Class Demon - Din
class demon(basicUnit):
    def __init__(self, name, HPMax, ATK, DEF):
        super().__init__(name, HPMax, ATK, DEF)
    
    def burn(self):
        print("Burn")

# Class BigSlime - Din
class bigslime(slime):
    def __init__(self, name, HPMax, ATK, DEF):
        super().__init__(name, HPMax, ATK, DEF)
    
    def quake(self):
        print("quake")

# Class Orc - Din
class orc(goblin):
    def __init__(self, name, HPMax, ATK, DEF):
        super().__init__(name, HPMax, ATK, DEF)

    def block(self):
        print("block")

# Class Skeleton Knight - Din
class skeletonknight(skeleton):
    def __init__(self, name, HPMax, ATK, DEF):
        super().__init__(name, HPMax, ATK, DEF)

    def reflect(self):
        print("reflect")

# Class Vampire Price - Din
class vampireprince(vampire):
    def __init__(self, name, HPMax, ATK, DEF):
        super().__init__(name, HPMax, ATK, DEF)
    
    def summon(self):
        print("summon")

# Class Demon King
class demonking(demon):
    def __init__(self, name, HPMax, ATK, DEF):
        super().__init__(name, HPMax, ATK, DEF)

    def revive(self):
        print("revive")