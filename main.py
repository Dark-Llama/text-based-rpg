from player_classes import *
from items import *
from input_classes import *


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
      "You have nothing but the clothes on your back, "
      "a few gold coins and a {}, a new life awaits.".format(player.weapon))
print("Welcome to the land of Swauyae")
print()


def main():
    game = True
    while game:
        z = random.randint(0, 10)
        if z == 10:
            bandit0 = Bandit()

            print("An Enemy Appears!")
            battle([player, bandit0], [player], [bandit0])
            if player.hp > 0:
                print("You defeated the Bandit")
            else:
                print("You Died")
                sys.exit()
        x = random.randint(0,6)
        if x == 6:
            wolf0 = Wolf()
            print("Enemies Appear!")
            battle([player, wolf0], [player], [wolf0])
            if player.hp > 0:
                print("You defeated the Wolf")
            else:
                print("You died")
                sys.exit()

        else:
            player_input(player)


if __name__ == '__main__':
    main()
