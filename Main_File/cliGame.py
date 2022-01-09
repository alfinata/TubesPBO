from cliUI.loginCLI import gameLogin
from cliUI.combatCLI import gameCombat
from LogicCodes.enemyClass import *
from LogicCodes.equipmentPool import *

a = gameLogin()

e = slime()
a.equipWeapon(lowMageWeapon)
gameCombat(a, e)