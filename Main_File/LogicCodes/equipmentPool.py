from LogicCodes.equipmentClass import *

# Weapon Values
lowWarriorWeapon = Weapon("Wooden Axe", 0, "Warrior", 18)
medWarriorWeapon = Weapon("Stone Sword", 30, "Warrior", 24)
higWarriorWeapon = Weapon("Steel Spear", 60, "Warrior", 30)
endWarriorWeapon = Weapon("Emerald Claymore", 90, "Warrior", 36)

lowMageWeapon = Weapon("Wooden Staff", 0, "Mage", 12)
medMageWeapon = Weapon("Stone Wand", 30, "Mage", 16)
higMageWeapon = Weapon("Hardwood Grimoire", 60, "Mage", 20)
endMageWeapon = Weapon("Ruby Magic Book", 90, "Mage", 24)

lowAssassinWeapon = Weapon("Rusty Knife", 0, "Assassin", 15)
medAssassinWeapon = Weapon("Sharp Shortsword", 30, "Assassin", 20)
higAssassinWeapon = Weapon("Iron Machete", 60, "Assassin", 25)
endAssassinWeapon = Weapon("Mithril Sabre", 90, "Assassin", 30)

# Armor Values
lowWarriorArmor = Armor("Leather Armor", 0, "Warrior", 0, 0)
medWarriorArmor = Armor("Stone Armor", 40, "Warrior", 36, 10)
higWarriorArmor = Armor("Iron Armor", 80, "Warrior", 72, 15)
endWarriorArmor = Armor("Guardian Armor", 120, "Warrior", 108, 20)

lowMageArmor = Armor("Apprentice Robe", 0, "Mage", 0, 0)
medMageArmor = Armor("Magician Clothes", 40, "Mage", 24, 10)
higMageArmor = Armor("Chakra Cape", 80, "Mage", 48, 15)
endMageArmor = Armor("Wizard Robe", 120, "Mage", 72, 20)

lowAssassinArmor = Armor("Rogue Shirt", 0, "Assassin", 0, 0)
medAssassinArmor = Armor("Leather Light Armor", 40, "Assassin", 30, 10)
higAssassinArmor = Armor("Ninja Uniform", 80, "Assassin", 60, 15)
endAssassinArmor = Armor("Swift Assassin Robe", 120, "Assassin", 90, 20)

# Weapon Pools
warriorWeaponPool = [lowWarriorWeapon, medWarriorWeapon, higWarriorWeapon, endWarriorWeapon]
mageWeaponPool = [lowMageWeapon, medMageWeapon, higMageWeapon, endMageWeapon]
assassinWeaponPool = [lowAssassinWeapon, medAssassinWeapon, higAssassinWeapon, endAssassinWeapon]

# Armor Pools
warriorArmorPool = [lowWarriorArmor, medWarriorArmor, higWarriorArmor, endWarriorArmor]
mageArmorPool = [lowMageArmor, medMageArmor, higMageArmor, endMageArmor]
assassinArmorPool = [lowAssassinArmor, medAssassinArmor, higAssassinArmor, endAssassinArmor]