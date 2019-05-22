from Player_Classes import *
from Enemy_Classes import *
from Item_Classes import *
from Combat_Functions import *
from Map_Array import *
from Map_Display import *
from Input_Classes import *


def main():
    player = character_create()
    potion = Potion()
    player.inventory.append(potion)
    player.x = 2
    player.y = 3

    print("You are {}, the {}".format(player.name, player.class_type))
    print()

    print("You wake up to the sound of horses trotting by, your head is groggy, you raise it up from where it lies on a bale of hay.")
    print("As you look around you find yourself in a town called Erith, it is small but has everything you need including a tavern to sleep and a shop to buy new weapons and supplys at. You have nothing but the clothes on your back, a few gold coins and a {}, a new life awaits.".format(player.weapon))
    print("Welcome to the land of Swauyae")
    print()

    player_input(player)


if __name__ == '__main__':
    main()