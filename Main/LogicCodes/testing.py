from basicClass import *
from consumablesClass import *
from heroClass import *
from consumablesClass import *
from enemyClass import *
from equipmentClass import *
from heroRole import *


def main():
    playerHero = basicHero("Rapip", 100, 0, 0, 0, warriorRole())
    print(f"Hero name is {playerHero.getName()}")
    print(f"Hero attack power is {playerHero.getATK()}")
    print(f"Hero HP is {playerHero.getHPCurrent()}/{playerHero.getHPMax()}")
    print(f"Hero defense is {playerHero.getDEF()}")
    print(f"Hero dodge chance is {playerHero.getEvade()}")
    print(f"Hero energy is {playerHero.energyCurrent}/{playerHero.energyMax}")
    print(f"Hero role is {playerHero.heroRole.checkRole()}\n")

    print("Hero takes 10 dmg")
    playerHero.setHPCurrent(90)
    print(f"Hero HP is {playerHero.getHPCurrent()}/{playerHero.getHPMax()}\n")

    weapon1 = Weapon("Wooden Sword", 0, "Warrior", 20)
    playerHero.equipWeapon(weapon1)
    print(f"Hero attack power is {playerHero.getATK()}\n")

    armor1 = Armor("Leather Armor", 10, "Warrior", 25, 10)
    playerHero.equipArmor(armor1)
    print(f"Hero defense is {playerHero.getDEF()}")
    print(f"Hero HP is {playerHero.getHPCurrent()}/{playerHero.getHPMax()}\n")

    enemy1 = slime("Slime1", 20, 10, 0)
    enemy1.attackTarget(playerHero)
    print(f"Hero HP is {playerHero.getHPCurrent()}/{playerHero.getHPMax()}\n")


main()