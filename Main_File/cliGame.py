from cliUI.loginCLI import *
from cliUI.combatCLI import *
from cliUI.mainMenuCLI import *
from LogicCodes.enemyClass import *
from LogicCodes.equipmentPool import *
from LogicCodes.heroClass import *
from LogicCodes.heroRole import *

# a = gameLogin()

a = basicHero("Test Hero", 120, 100, mageRole(), 0)
a.equipWeapon(lowMageWeapon)
gameMenu(a)

# e = slime()

# gameCombat(a, e)