"""This is just a storage file for code until it gets reimplemented in game.
    Code pulled from original main() function. replaced by input_classes.py"""

print("As you travel through the forest you encounter a fork in the road.\nWhich way do you go?")
print("1. Left\n2. Right")
print()
direction = input("Pick a path: ")
print()
if direction == "1":
    back = False
    while not back:
        wolf0 = Wolf()
        wolf1 = Wolf()

        print("Enemies Appear!")
        battle([player, wolf0, wolf1], [player], [wolf0, wolf1])
        if player.hp > 0:
            print("Behind the beast was a dead end. Do you want to turn back?")
            print("1. Yes\n2. No")
            print()
            go_back = input("Go back? : ")
            if go_back == "1":
                print(
                    "As you head back you see another adventurer walking away from the other path with boundless treasure, too bad you didn't go that way.")
                back = True
            elif go_back == "2":
                continue
        else:
            break
elif direction == "2":
    back = False
    while not back:
        bandit0 = Bandit()

        print("An enemy Appears!")
        battle([player, bandit0], [player], [bandit0])
        if player.hp > 0:
            print("Behind the slime is a path leading into the woods, do you continue or turn back?")
            print("1. Head back\n2. Continue")
            print()
            go_back = input("Go back? : ")
            if go_back == "1":
                print("As you head back you fall into a trap and die")
                back = True
            elif go_back == "2":
                continue
        else:
            break

print("Game over.")