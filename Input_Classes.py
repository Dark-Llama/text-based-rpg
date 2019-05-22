from Map_Display import *
from Map_Array import *
from Enemy_Classes import *
from Combat_Functions import *
import sys

def player_input(player):
    inputtext = input("What do you want to do?")

    """Navigation Inputs"""
    if inputtext == "Map":
        Map_Display()

    if inputtext == "North":
        player.y = player.y + 1
        print("You have moved North one square.")

    if inputtext == "South":
        player.y = player.y - 1
        print("You have moved South one square")

    if inputtext == "East":
        player.x = player.x + 1
        print("You have moved East one square")

    if inputtext == "West":
        player.x = player.x -1
        print("You have moved West one square")

    if inputtext == "Where am I?":
        print((map[player.x][player.y]))

    if inputtext == "Pos":
        print(player.x)
        print(player.y)

    """Misc Inputs"""
    if inputtext == "Level":
        print("Experience")
        print(player.exp)
        print("Level")
        print(player.lvl)

    if inputtext == "Stats":
        print("Magica")
        print(player.mp)
        print("Health")
        print(player.hp)
        print("Player Speed")
        print(player.spd)


    """Spawn Enemies"""
    if inputtext == "Spawn Wolf":
        wolf0 = Wolf()
        print("Enemies Appear!")
        battle([player, wolf0], [player], [wolf0])
        if player.hp > 0:
            print("You defeated the wolf")
        else:
            print("You died")
            sys.exit()

    if inputtext == "Spawn Bandit":
        bandit0 = Bandit()

        print("An Enemy Appears!")
        battle([player, bandit0], [player], [bandit0])
        if player.hp > 0:
            print("You defeated the bandit")
        else:
            print("You Died")
            sys.exit()

    player_input(player)
