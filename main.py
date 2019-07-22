from player_classes import *
from items import *
from input_classes import *


def main():
    player = character_create()
    potion = Potion()
    player.inventory.append(potion)
    player.x = 2
    player.y = 3

    print("You are {}, the {}".format(player.name, player.class_type))
    print()

    print("You wake up to the sound of horses trotting by, your head is groggy. "
          "You raise it up from where it lies on a bale of hay.")
    print("As you look around you find yourself in a town called Erith."
          "It is small but has everything you need. "
          "You have nothing but the clothes on your back, a few gold coins and a {}, a new life awaits.".format(player.weapon))
    print("Welcome to the land of Swauyae")
    print()

    player_input(player)


if __name__ == '__main__':
    main()
