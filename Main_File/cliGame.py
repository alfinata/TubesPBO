from cliUI.loginCLI import *
from cliUI.combatCLI import *
from cliUI.mainMenuCLI import *
from LogicCodes.enemyClass import *
from LogicCodes.equipmentPool import *
from LogicCodes.heroClass import *
from LogicCodes.heroRole import *

# a = gameLogin()

a = basicHero("WarriorTestHero", 400, 100, warriorRole(), 0)
a.equipWeapon(lowWarriorWeapon)
a.equipArmor(lowWarriorArmor)

# a = basicHero("MageTestHero", 100, 120, mageRole(), 0)
# a.equipWeapon(lowMageWeapon)
# a.equipArmor(lowMageArmor)

# a = basicHero("AssassinTestHero", 100, 100, assassinRole(), 10)
# a.equipWeapon(lowAssassinWeapon)
# a.equipArmor(lowAssassinArmor)

gameMenu(a)

# e = slime()

# gameCombat(a, e)