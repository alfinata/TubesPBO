from mechanics import navigate
from units import basicUnit, playerHero, enemyUnit, lastBoss, woodSword
from equipments import sword, armor
import os

os.system('cls' if os.name == 'nt' else 'clear')
x = input("Insert your hero name here: ")
h1 = playerHero(x)
print("======================================")


os.system('cls' if os.name == 'nt' else 'clear')
print("======================================")
print("")
print(f"{h1.getName()}, welcome to this little RPG game.")
print("You will find various items along your journey.")
print("Use these items to grow stronger and defeat the final boss, Dio!")
print("")
input("<<Press enter to continue>>")

os.system('cls' if os.name == 'nt' else 'clear')
print("======================================")
print("")
print(f"Your journey won't be an easy one.")
print("So consider this as a starting gift.")
woodSword.showInfo()
print("You received 50 gold.")
print("You received a Wooden Sword")
h1.equipWeapon(woodSword)
print("")
input("<<Press enter to continue>>")

navigate(h1)
