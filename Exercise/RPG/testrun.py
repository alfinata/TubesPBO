from units import basicUnit, playerHero, enemyUnit, lastBoss
from equipments import sword, armor
import os


# Hero Initialization
h1 = playerHero("JoJo")

# 1st Sword
s1 = sword("Wooden Sword", 10)
s1.showInfo()

# Equip Sword
h1.equipWeapon(s1)
h1.showInfo()

# 2nd Sword
s2 = sword("Stone Sword", 15)
s2.showInfo()

# Equip Sword
h1.equipWeapon(s2)
h1.showInfo()

# 1st Armor
a1 = armor("School Uniform", 25)
a1.showInfo()

h1.equipArmor(a1)
h1.showInfo()

lastBoss.showInfo()

h1.attackTarget(lastBoss)

lastBoss.showInfo()

