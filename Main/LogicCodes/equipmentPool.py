from LogicCodes.equipmentClass import *

# Weapon Values
lowWarriorWeapon = Weapon("Wooden Axe", 0, "Warrior", 18)
medWarriorWeapon = Weapon("Stone Sword", 30, "Warrior", 30)
higWarriorWeapon = Weapon("Steel Spear", 60, "Warrior", 42)
endWarriorWeapon = Weapon("Emerald Claymore", 90, "Warrior", 56)

lowMageWeapon = Weapon("Wooden Staff", 0, "Mage", 12)
medMageWeapon = Weapon("Stone Wand", 30, "Mage", 20)
higMageWeapon = Weapon("Hardwood Grimoire", 60, "Mage", 28)
endMageWeapon = Weapon("Ruby Magic Book", 90, "Mage", 36)

lowAssassinWeapon = Weapon("Rusty Knife", 0, "Assassin", 15)
medAssassinWeapon = Weapon("Sharp Shortsword", 30, "Assassin", 25)
higAssassinWeapon = Weapon("Iron Machete", 60, "Assassin", 35)
endAssassinWeapon = Weapon("Mithril Sabre", 90, "Assassin", 45)

# Armor Values
lowWarriorArmor = Armor("Leather Armor", 0, "Warrior", 0, 0)
medWarriorArmor = Armor("Stone Armor", 40, "Warrior", 42, 10)
higWarriorArmor = Armor("Iron Armor", 80, "Warrior", 84, 15)
endWarriorArmor = Armor("Guardian Armor", 120, "Warrior", 126, 20)

lowMageArmor = Armor("Apprentice Robe", 0, "Mage", 0, 0)
medMageArmor = Armor("Magician Clothes", 40, "Mage", 28, 10)
higMageArmor = Armor("Chakra Cape", 80, "Mage", 56, 15)
endMageArmor = Armor("Wizard Robe", 120, "Mage", 84, 20)

lowAssassinArmor = Armor("Rogue Shirt", 0, "Assassin", 0, 0)
medAssassinArmor = Armor("Leather Light Armor", 40, "Assassin", 35, 10)
higAssassinArmor = Armor("Ninja Uniform", 80, "Assassin", 70, 15)
endAssassinArmor = Armor("Swift Assassin Robe", 120, "Assassin", 105, 20)

# Weapon Pools
warriorWeaponPool = [lowWarriorWeapon, medWarriorWeapon, higWarriorWeapon, endWarriorWeapon]
mageWeaponPool = [lowMageWeapon, medMageWeapon, higMageWeapon, endMageWeapon]
assassinWeaponPool = [lowAssassinWeapon, medAssassinWeapon, higAssassinWeapon, endAssassinWeapon]

# Armor Pools
warriorArmorPool = [lowWarriorArmor, medWarriorArmor, higWarriorArmor, endWarriorArmor]
mageArmorPool = [lowMageArmor, medMageArmor, higMageArmor, endMageArmor]
assassinArmorPool = [lowAssassinArmor, medAssassinArmor, higAssassinArmor, endAssassinArmor]