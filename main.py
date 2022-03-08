'''
This program runs a text based adventure game!
Author: Jermaine
'''

inventory = {}
inventory_container = []
weapon_container = []
loot_drops = {1 : "String", 2 : "Stick", 3 : "Stone", 4 : "Coal", 5 : "Dirt", 6 : "Flint", 7 : "Iron", 8 : "Brick", 9 : "Wood", 10 : "Health Potion"}
magics = {1 : "Fire", 2 : "Ice", 3 : "Re-equip", 4 : "Celestial Spirit", 5 : "Transformation", 6 : "Air", 7 : "Steel", 8 : "Water"}

from random import randint
from time import sleep
import sys

def slowprint_title(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep(1./100)

def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep(1./25)


def bootup_Aether():
  slowprint_title("───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
  slowprint_title("────────────────██████───────██████████████─██████████████─██████████████─██████──██████─██████████████─████████████████───")
  slowprint_title("────────────────██░░████─────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───")
  slowprint_title("────────────────████░░████───██░░██████░░██─██░░██████████─██████░░██████─██░░██──██░░██─██░░██████████─██░░████████░░██───")
  slowprint_title("──────────────────████░░████─██░░██──██░░██─██░░██─────────────██░░██─────██░░██──██░░██─██░░██─────────██░░██────██░░██───")
  slowprint_title("─██████████████─────████░░██─██░░██████░░██─██░░██████████─────██░░██─────██░░██████░░██─██░░██████████─██░░████████░░██───")
  slowprint_title("─██░░░░░░░░░░██───────██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─────██░░██─────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───")
  slowprint_title("─██████████████─────████░░██─██░░██████░░██─██░░██████████─────██░░██─────██░░██████░░██─██░░██████████─██░░██████░░████───")
  slowprint_title("──────────────────████░░████─██░░██──██░░██─██░░██─────────────██░░██─────██░░██──██░░██─██░░██─────────██░░██──██░░██─────")
  slowprint_title("────────────────████░░████───██░░██──██░░██─██░░██████████─────██░░██─────██░░██──██░░██─██░░██████████─██░░██──██░░██████─")
  slowprint_title("────────────────██░░████─────██░░██──██░░██─██░░░░░░░░░░██─────██░░██─────██░░██──██░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─")
  slowprint_title("────────────────██████───────██████──██████─██████████████─────██████─────██████──██████─██████████████─██████──██████████─")
  slowprint_title("───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
  sleep(2)
  slowprint("Welcome to the world of magic.")
  sleep(1)
  slowprint("This world contains strange creatures and monsters so be cautious! \nThere is also magic, guilds, dark guilds, missions/quests! \nYou'll meet tons of people along the way and either join forces to create allies and alliances or cause war and destruction!")
  sleep(1)
  player = input("What is your name?")
  starter_magic_select = input("Please choose your main magic power! You can learn more magic in the future and even increase and evolve your magic power!\n1) Fire Magic\n2) Ice Magic\n3) Re-equip Magic\n4) Celestial Spirit Magic\n5) Transformation Magic\n6) Air Magic\n7) Steel Magic\n8) Water\n")
  try:
    primary_magic = int(starter_magic_select)
    slowprint(("\n\nYou have learned %s magic!") % magics[primary_magic])
  except ValueError:
    print("Invalid Selection, please try again.")
    sleep(1)
    bootup_Aether()
  aspire_beginning(player, primary_magic)

def aspire_beginning(player, primary_magic):
  location = "Aspire"
  slowprint("You are currently in the town of Aspire.")
  sleep(1)
  slowprint("\nYou wake up at the tavern, you decided to stay in and grab your belongings. Then head out the door.")
  sleep(2)
  print("\n+1 Wooden Sword \n+500 Coins")
  inventory["Wooden Sword"] = 1
  weapon_container.append("Wooden Sword")
  inventory["Coins"] = 500
  inventory_container.append("Coins")
  sleep(1)
  slowprint("\nYou see a small shop.")
  zen_shop_enter = input("\nDo you enter the shop? 1 for yes, 2 for no.");
  zen_shop_enter = int(zen_shop_enter)
  if zen_shop_enter == 1:
    zen_shop(location, 0)
  slowprint("You continue walking and end up reaching the forest and you enter.")
  slowprint("You walk along the path and you find a cave!")
  forest_cave = input("Do you enter the cave or keep walking along the path? \n1) Enter the cave. \n2) Continue walking through the forest \n3) Check your inventory.")
  forest_cave = int(forest_cave)
  if forest_cave == 1:
    slowprint("You stumble into a spider!")
    battle("Jm", 25, "Spider", 10)
    slowprint("You continue on your adventure through the cave and find a small locked chest!")
    if "Small Key" not in inventory:
      slowprint("Unfortunately you do not have a small key!")
    else:
      small_chest = input("Would you like to open the chest? \n1) Yes! \n2) No!")
      if small_chest == 1:
        slowprint("You found a Stone Sword! \n\n +1 Stone Sword")
        inventory["Stone Sword"] = 1
    slowprint("You continue walking down the cave and end up on the other side.")
    sleep(1)
    slowprint("You've reached the trail towards the mountain village, Tentra! \n\nWhat would you like to do?")
    tentra_path = input("1. Travel up the path!\n2. Turn back.\n3. Look around the area.")
  elif forest_cave == 2:
    slowprint("You stumble into a Treeling!")
    battle("Jm", 25, "Treeling", 14)

def aspire_main():
  slowprint("You've arrived at the small town, Aspire!")

def tentra_main():
  slowprint("You've arrived at the mountian village, Tentra!")

def paein_island_main():
  slowprint("You've arrived at the tropical island, Paein Island!")

def boust_main():
  slowprint("You've arrived at the sea side city, Boust!")

def era_main():
  slowprint("You've arrived the central kingdom, Era!")

def chronos_main(player, player_health):
  location = "Chronos"
  slowprint("You've arrived at the modern metropolis, Chronos!")
  battle(player, player_health, "Arkend", 20000)

def zen_shop(location, times):
  slowprint("\nWelcome to the Zen! This is what we're selling:")
  sleep(1)
  if location == "Aspire":
    print("1. Health Potion - 50 Coins\n2. Wooden Bow - 400 Coins\n3. Arrows - 10 Coins each")
    shop1_buy = input("\nWould you like to buy anything? Please enter a corresponding number.")
    shop1_buy = int(shop1_buy)
    if shop1_buy == 1:
      multi_buy(50, "Health Potion", location, times)
    elif shop1_buy == 2:
      multi_buy(400, "Bow", location, times)
    elif shop1_buy == 3:
      multi_buy(100, "Arrow", location, times)
  
  
def multi_buy(cost, item, location, times):
  if inventory["Coins"] - cost >= cost:
    multi_buy_select = input("\nHow many would you like to buy?")
    multi_buy_select = int(multi_buy_select)
    if multi_buy_select > 1 and multi_buy_select * cost <= inventory["Coins"]:
      if times > 0:
        if item in inventory:
          inventory[item] = inventory[item] + multi_buy_select
          times = times + 1
          print("+" + str(multi_buy_select) + " " + item + "\n-" + str(cost) + "Coins")
          revisit(location)
        else:
          inventory[item] = multi_buy_select
          print("+" + str(multi_buy_select) + " " + item + "\n-" + str(cost) + "Coins")
          times = times + 1
      else:
        inventory[item] = multi_buy_select
        inventory[1] = inventory[1] - (multi_buy_select * cost)
        print("+" + str(multi_buy_select) + " " + item + "\n-" + str(cost) + "Coins")
        revisit(location)
    elif multi_buy_select == 1:
      if item not in inventory:
        inventory[item] = 1
        inventory["Coins"] = inventory["Coins"] - cost
        print("+" + str(multi_buy_select) + " " + item + "\n-" + str(cost) + "Coins")
        revisit(location)
      else:
        inventory[item] = inventory[item] + 1
        inventory["Coins"] = inventory["Coins"] - cost
        print("+" + str(multi_buy_select) + " " + item + "\n-" + str(cost) + "Coins")
        revisit(location)
    else:
      slowprint("\nYou cannot afford that many!")
      revisit(location)
      return
    print(inventory)
  elif inventory["Coins"] >= cost:
      if item not in inventory:
        inventory[item] = 1
        inventory["Coins"] = inventory["Coins"] - cost
        print("\n+1 " + item + "\n-" + str(cost) + "Coins")
        revisit(location)
      else:
        inventory[item] = inventory[item] + 1
        inventory["Coins"] = inventory["Coins"] - cost
        print("\n+1 " + item + "\n-" + str(cost) + "Coins")
        revisit(location)
  else:
    print("\nYou cannot afford this item!")
    revisit(location)
    return 
    
    
def revisit(location):
  revisit_select = input("\nWould you like to look around the shop a bit more? Enter 1 for yes, 2 for no.")
  revisit_select = int(revisit_select)
  if revisit_select == 1:
    zen_shop(location, 1)
  elif revisit_select == 2:
    return
  else:
    slowprint("Invalid Selection. Please try again.")
    revisit(location)
    
    
def battle(player, player_health, monster, monster_health):
  weapon_choice = input("Which weapon would you like to use?")
  weapon_choice = weapon_choice.upper()
  while monster_health > 0:
    print(player + "'s Hp:" + str(player_health) + " " + monster + "'s Hp:" + str(monster_health))
    battle_choice = input("\nWhat will you do?\n1. Attack\n2. Check Backpack.\n3. Use Magic")
    battle_choice = int(battle_choice)
    if battle_choice == 1:
      print(inventory_container)
      if weapon_choice == "WOODEN SWORD":
        wooden_sword_dmg = randint(1, 6)
        monster_health = monster_health - wooden_sword_dmg
        slowprint(("You attack with your wooden sword and you deal %s damage!") % wooden_sword_dmg)
        monster_damage = randint(1, 4)
        player_health = player_health - monster_damage
      if weapon_choice == "BOW":
        if "Arrows" not in inventory:
          slowprint("You have no arrows to use your bow with!")
          battle(player, player_health, monster, monster_health)
        bow_dmg = randint(3, 7)
        monster_health = monster_health - bow_dmg
        inventory["Arrows"] = inventory["Arrows"] - 1
        slowprint(("You attack with your Bow and Arrow and you deal %s damage!") % bow_dmg)
      if weapon_choice == "EXCALIBUR":
        monster_damage = 1
        excalibur_dmg = 1000000
        monster_health = monster_health - excalibur_dmg
        slowprint(("You attack with the Legendary Excalibur and you deal %s damage!") % excalibur_dmg)
    if battle_choice == 2:
      print(inventory)
      battle_item = input("What would you like to use?")
      battle_item = battle_item.upper()
      if battle_item not in inventory:
        print("scream")
      if battle_item == "HEALTH POTION":
        player_health = player_health + 10
        inventory["Health Potion"] = inventory["Health Potion"] - 1
  if monster == "Arkend":
    slowprint("You defeated Arkend and saved the world from total destruction!")
  else:
    slowprint("You defeated the " + monster)
    battle_end(monster_health)
  
  
def battle_end(monster_health):
  if monster_health < 25:
    loot = randint(1, 51)
    if loot % 2 == 0:
      looting(2, loot)
    elif loot % 3 == 0:
      looting(3, loot)
    elif loot % 5 == 0:
      looting(5, loot)
    elif loot % 7 == 0:
      looting(7, loot)
    elif loot == 1:
      looting(1, loot)
    else:
      looting(10, loot)
  leveling(monster_health)

def looting(prime_group, loot):
  double_loot = randint(1,10)
  print(loot, double_loot)
  double_loot_item = loot_drops[double_loot]
  inventory["Coins"] = inventory["Coins"] + loot
  if double_loot > prime_group * 2:
    print("\n+" + str(loot) + " Coins" + "\n+1 " + loot_drops[double_loot])
    if double_loot_item in inventory:
      inventory[double_loot_item] = inventory[double_loot_item] + 1
    else:
      inventory[double_loot_item] = 1
      print(inventory)
          
def leveling(monster_health, player_level, player_exp):
  if player_level == 20:
    slowprint("Final level reached! Congratulations!")
    print(str(player_level), str(player_exp))
    leveling(monster_health, player_level, player_exp)
  elif player_level < 21:
    if player_exp >= 10000:
      player_level = player_level + 1
    elif player_exp >= 50:
      player_level = player_level + 1
    elif monster_health < 26:
      loot_exp = 1000000
      player_exp = player_exp + loot_exp
  print(str(player_level), str(player_exp))

'''
2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50
3, 9, 15, 21, 27, 33, 39, 45
5, 15, 25, 35, 45,
7, 49
1, 11, 13, 17, 19, 23 , 29, 31, 37, 41, 43, 47
'''

#bootup_wildy()
inventory["Coins"] = 1000000
inventory["Wooden Sword"] = 1
inventory["Excalibur"] = 1
bootup_Aether()
'''
player = "Jm"
player_health = 100000
player_exp = 1
player_level = 10
chronos_main()
'''
