from LogicCodes.basicClass import basicUnit

# Class Slime - Alfinata
class slime(basicUnit):
    def __init__(self):
        super().__init__("Slime", 30, 12, 0, 8, 0, 5)

# Class Goblin - Din
class goblin(basicUnit):
    def __init__(self):
        super().__init__("Goblin", 50, 20, 5, 16, 0, 5)


# # Class Skeleton - Din
# class skeleton(basicUnit):
#     def __init__(self, name, HPMax, ATK, DEF):
#         super().__init__(name, HPMax, ATK, DEF)
    
#     def dodge(self):
#         print("Dodge")

# # Class Vampire - Din
# class vampire(basicUnit):
#     def __init__(self, name, HPMax, ATK, DEF):
#         super().__init__(name, HPMax, ATK, DEF)
    
#     def lifesteal(self):
#         print("LiveSteal")

# # Class Demon - Din
# class demon(basicUnit):
#     def __init__(self, name, HPMax, ATK, DEF):
#         super().__init__(name, HPMax, ATK, DEF)
    
#     def burn(self):
#         print("Burn")

# # Class BigSlime - Din
# class bigslime(slime):
#     def __init__(self, name, HPMax, ATK, DEF):
#         super().__init__(name, HPMax, ATK, DEF)
    
#     def quake(self):
#         print("quake")

# # Class Orc - Din
# class orc(goblin):
#     def __init__(self, name, HPMax, ATK, DEF):
#         super().__init__(name, HPMax, ATK, DEF)

#     def block(self):
#         print("block")

# # Class Skeleton Knight - Din
# class skeletonknight(skeleton):
#     def __init__(self, name, HPMax, ATK, DEF):
#         super().__init__(name, HPMax, ATK, DEF)

#     def reflect(self):
#         print("reflect")

# # Class Vampire Price - Din
# class vampireprince(vampire):
#     def __init__(self, name, HPMax, ATK, DEF):
#         super().__init__(name, HPMax, ATK, DEF)
    
#     def summon(self):
#         print("summon")

# # Class Demon King
# class demonking(demon):
#     def __init__(self, name, HPMax, ATK, DEF):
#         super().__init__(name, HPMax, ATK, DEF)

#     def revive(self):
#         print("revive")