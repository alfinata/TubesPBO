from LogicCodes.equipmentClass import *

# Weapon Values
lowWarriorWeapon = Weapon("Wooden Axe", 0, "Warrior", 12)
medWarriorWeapon = Weapon("Stone Sword", 10, "Warrior", 18)
higWarriorWeapon = Weapon("Steel Spear", 20, "Warrior", 24)
endWarriorWeapon = Weapon("Emerald Claymore", 30, "Warrior", 30)

lowMageWeapon = Weapon("Wooden Staff", 0, "Mage", 8)
medMageWeapon = Weapon("Stone Wand", 10, "Mage", 12)
higMageWeapon = Weapon("Hardwood Grimoire", 20, "Mage", 16)
endMageWeapon = Weapon("Ruby Magic Book", 30, "Mage", 20)

lowAssassinWeapon = Weapon("Rusty Knife", 0, "Assassin", 10)
medAssassinWeapon = Weapon("Sharp Shortsword", 10, "Assassin", 15)
higAssassinWeapon = Weapon("Iron Machete", 20, "Assassin", 20)
endAssassinWeapon = Weapon("Mithril Sabre", 30, "Assassin", 25)

# Armor Values

lowWarriorArmor = Armor("Leather Armor", 0, "Warrior", 0, 0)
medWarriorArmor = Armor("Stone Armor", 10, "Warrior", 36, 10)
higWarriorArmor = Armor("Iron Armor", 20, "Warrior", 72, 15)
endWarriorArmor = Armor("Guardian Armor", 30, "Warrior", 108, 20)

lowMageArmor = Armor("Apprentice Robe", 0, "Mage", 0, 0)
medMageArmor = Armor("Magician Clothes", 10, "Mage", 24, 10)
higMageArmor = Armor("Chakra Cape", 20, "Mage", 48, 15)
endMageArmor = Armor("Wizard Robe", 30, "Mage", 72, 20)

lowAssassinArmor = Armor("Rogue Shirt", 0, "Assassin", 0, 0)
medAssassinArmor = Armor("Leather Light Armor", 10, "Assassin", 30, 10)
higAssassinArmor = Armor("Ninja Uniform", 20, "Assassin", 60, 15)
endAssassinArmor = Armor("Swift Assassin Robe", 30, "Assassin", 90, 20)

# Weapon Pools
warriorWeaponPool = [lowWarriorWeapon, medWarriorWeapon, higWarriorWeapon, endWarriorWeapon]
mageWeaponPool = [lowMageWeapon, medMageWeapon, higMageWeapon, endMageWeapon]
assassinWeaponPool = [lowAssassinWeapon, medAssassinWeapon, higAssassinWeapon, endAssassinWeapon]

# Armor Pools
warriorArmorPool = [lowWarriorArmor, medWarriorArmor, higWarriorArmor, endWarriorArmor]
mageArmorPool = [lowMageArmor, medMageArmor, higMageArmor, endMageArmor]
assassinArmorPool = [lowAssassinArmor, medAssassinArmor, higAssassinArmor, endAssassinArmor]