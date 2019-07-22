from character_setup import *

class Player(character):
    """Create Player Class"""
    # initialize player at level 1 with 0 experience
    exp = 0
    lvl = 1

    def __init__(self):
        pass

    # define stats from base stats of subclass
    def stats_init(self):
        self.hp = self.stats['BASE_HP']
        self.mp = self.stats['BASE_MP']
        self.atk = self.stats['BASE_ATK']
        self.dfs = self.stats['BASE_DFS']
        self.magic_atk = self.stats['BASE_MAGIC_ATK']
        self.spd = self.stats['BASE_SPD']
        self.luck = self.stats['BASE_LUCK']

    # loop through base stats dict and add level up modifiers
    def level_up(self):
        print()
        print("*--- {} LEVELED UP! ---*".format(self.name))
        for stat, value in self.stats.items():
            print("{}: {} + {} -->".format(stat, value, self.modifiers[stat]), end="")
            self.stats[stat] = value + self.modifiers[stat]
            print(self.stats[stat])
        self.lvl += 1
        print("*----------------------------------*")
        print()
        self.stats_init()

    # check level requirements and call level up on self if met
    def check_level_up(self):
        self.levels = [100, 250, 500, 1200]
        for value in self.levels:
            if self.exp >= value:
                self.level_up()
                self.levels.remove(value)
                break

    # take in enemies defeated from battle and add exp to total player controlled character
    def calculate_experience(self, enemies):
        exp_gain = 0
        for enemy in enemies:
            self.exp = self.exp + enemy.exp
            exp_gain = exp_gain + enemy.exp
        print("{} gained {} exp!".format(self.name, exp_gain))
        print("{}'s total exp: {}".format(self.name, self.exp))

    def check_inventory(self):
        if len(self.inventory) > 0:
            for idx, item in enumerate(self.inventory):
                print("{}. {}".format(idx, item.name))

            valid_item = False
            while not valid_item:
                item = input("Pick an item: ")
                try:
                    item = int(item)
                    valid_item = 0 <= item <= idx
                except ValueError:
                    pass
                if not valid_item:
                    print("Invalid Target")
            else:
                self.inventory[item].use_potion(self)
        else:
            raise Exception("You have no items")

def character_create():
    name = input("Hello brave adventurer, what is your name? : ")
    print()
    print("Pick your character")
    print()
    print("1. Barbarian")
    print("2. Bard")
    print("3. Cleric")
    print("4. Druid")
    print("5. Fighter")
    print("6. Monk")
    print("7. Paladin")
    print("8. Ranger")
    print("9. Rouge")
    print("10. Sorcerer")
    print("11. Warlock")
    print("12. Wizard")
    print()

    chosen = False
    while not chosen:
            class_choice = input("Please choose a class: ")
            print()
            if class_choice == "1":
                return Barbarian(name)
                chosen = True
            elif class_choice == "2":
                return Bard(name)
                chosen = True
            elif class_choice == "3":
                return Cleric(name)
                chosen = True
            elif class_choice == "4":
                return Druid(name)
                chosen = True
            elif class_choice == "5":
                return Fighter(name)
                chosen = True
            elif class_choice == "6":
                return Monk(name)
                chosen = True
            elif class_choice == "7":
                return Paladin(name)
                chosen = True
            elif class_choice == "8":
                return Ranger(name)
                chosen = True
            elif class_choice == "9":
                return Rouge(name)
                chosen = True
            elif class_choice == "10":
                return Sorcerer(name)
                chosen = True
            elif class_choice == "11":
                return Warlock(name)
                chosen = True
            elif class_choice == "12":
                return Wizard(name)
                chosen = True
            else:
                print("Invalid input.")
                continue

# create different class types
class Barbarian(Player):
    """Defines Barbarian Class"""

    def __init__(self, name):
        self.name = name
        self.class_type = "Barbarian"
        self.weapon = "mace"
        self.inventory = []
        self.stats = {'BASE_HP': 100, 'BASE_MP': 100, 'BASE_ATK': 25, 'BASE_DFS': 15, 'BASE_MAGIC_ATK': 25, 'BASE_SPD': 100,
                      'BASE_LUCK': 25}
        self.modifiers = {'BASE_HP': 25, 'BASE_MP': 25, 'BASE_ATK': 25, 'BASE_DFS': 5, 'BASE_MAGIC_ATK': 5, 'BASE_SPD': 25,
                          'BASE_LUCK': 1}
        self.stats_init()
        self.x = 0
        self.y = 0

class Bard(Player):
    """Defines Bard Class"""

    def __init__(self, name):
        self.name = name
        self.class_type = "Bard"
        self.weapon = "dagger"
        self.inventory = []
        self.stats = {'BASE_HP': 12, 'BASE_MP': 2, 'BASE_ATK': 10, 'BASE_DFS': 5, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 4,
                      'BASE_LUCK': 6}
        self.modifiers = {'BASE_HP': 4, 'BASE_MP': 1, 'BASE_ATK': 2, 'BASE_DFS': 3, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 1,
                          'BASE_LUCK': 1}
        self.stats_init()
        self.x = 0
        self.y = 0

class Cleric(Player):
    """Defines Cleric Class"""

    def __init__(self, name):
        self.name = name
        self.class_type = "Cleric"
        self.weapon = "dagger"
        self.inventory = []
        self.stats = {'BASE_HP': 12, 'BASE_MP': 2, 'BASE_ATK': 10, 'BASE_DFS': 5, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 4,
                      'BASE_LUCK': 6}
        self.modifiers = {'BASE_HP': 4, 'BASE_MP': 1, 'BASE_ATK': 2, 'BASE_DFS': 3, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 1,
                          'BASE_LUCK': 1}
        self.stats_init()
        self.x = 0
        self.y = 0

class Druid(Player):
    """Defines Druid Class"""

    def __init__(self, name):
        self.name = name
        self.class_type = "Druid"
        self.weapon = "sickle"
        self.inventory = []
        self.stats = {'BASE_HP': 12, 'BASE_MP': 2, 'BASE_ATK': 10, 'BASE_DFS': 5, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 4,
                      'BASE_LUCK': 6}
        self.modifiers = {'BASE_HP': 4, 'BASE_MP': 1, 'BASE_ATK': 2, 'BASE_DFS': 3, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 1,
                          'BASE_LUCK': 1}
        self.stats_init()
        self.x = 0
        self.y = 0

class Fighter(Player):
    """Defines Fighter Class"""

    def __init__(self, name):
        self.name = name
        self.class_type = "Fighter"
        self.weapon = "sword"
        self.inventory = []
        self.stats = {'BASE_HP': 12, 'BASE_MP': 2, 'BASE_ATK': 10, 'BASE_DFS': 5, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 4,
                      'BASE_LUCK': 6}
        self.modifiers = {'BASE_HP': 4, 'BASE_MP': 1, 'BASE_ATK': 2, 'BASE_DFS': 3, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 1,
                          'BASE_LUCK': 1}
        self.stats_init()
        self.x = 0
        self.y = 0

class Monk(Player):
    """Defines Monk Class"""

    def __init__(self, name):
        self.name = name
        self.class_type = "Monk"
        self.weapon = "staff"
        self.inventory = []
        self.stats = {'BASE_HP': 12, 'BASE_MP': 2, 'BASE_ATK': 10, 'BASE_DFS': 5, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 4,
                      'BASE_LUCK': 6}
        self.modifiers = {'BASE_HP': 4, 'BASE_MP': 1, 'BASE_ATK': 2, 'BASE_DFS': 3, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 1,
                          'BASE_LUCK': 1}
        self.stats_init()
        self.x = 0
        self.y = 0

class Paladin(Player):
    """Defines Paladin Class"""

    def __init__(self, name):
        self.name = name
        self.class_type = "Paladin"
        self.weapon = "sword"
        self.inventory = []
        self.stats = {'BASE_HP': 12, 'BASE_MP': 2, 'BASE_ATK': 10, 'BASE_DFS': 5, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 4,
                      'BASE_LUCK': 6}
        self.modifiers = {'BASE_HP': 4, 'BASE_MP': 1, 'BASE_ATK': 2, 'BASE_DFS': 3, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 1,
                          'BASE_LUCK': 1}
        self.stats_init()
        self.x = 0
        self.y = 0

class Ranger(Player):
    """Defines Ranger Class"""

    def __init__(self, name):
        self.name = name
        self.class_type = "Ranger"
        self.weapon = "sword"
        self.inventory = []
        self.stats = {'BASE_HP': 12, 'BASE_MP': 2, 'BASE_ATK': 10, 'BASE_DFS': 5, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 4,
                      'BASE_LUCK': 6}
        self.modifiers = {'BASE_HP': 4, 'BASE_MP': 1, 'BASE_ATK': 2, 'BASE_DFS': 3, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 1,
                          'BASE_LUCK': 1}
        self.stats_init()
        self.x = 0
        self.y = 0

class Rouge(Player):
    """Defines Rouge Class"""
    def __init__(self, name):
        self.name = name
        self.class_type = "Rouge"
        self.weapon = "dagger"
        self.inventory = []
        self.stats = {'BASE_HP': 12, 'BASE_MP': 2, 'BASE_ATK': 10, 'BASE_DFS': 5, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 4,
                      'BASE_LUCK': 6}
        self.modifiers = {'BASE_HP': 4, 'BASE_MP': 1, 'BASE_ATK': 2, 'BASE_DFS': 3, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 1,
                          'BASE_LUCK': 1}
        self.stats_init()
        self.x = 0
        self.y = 0

class Sorcerer(Player):
    """Defines Sorcerer Class"""

    def __init__(self, name):
        self.name = name
        self.class_type = "Sorcerer"
        self.weapon = "wand"
        self.inventory = []
        self.stats = {'BASE_HP': 12, 'BASE_MP': 2, 'BASE_ATK': 10, 'BASE_DFS': 5, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 4,
                      'BASE_LUCK': 6}
        self.modifiers = {'BASE_HP': 4, 'BASE_MP': 1, 'BASE_ATK': 2, 'BASE_DFS': 3, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 1,
                          'BASE_LUCK': 1}
        self.stats_init()
        self.x = 0
        self.y = 0

class Warlock(Player):
    """Defines Warlock Class"""

    def __init__(self, name):
        self.name = name
        self.class_type = "Warlock"
        self.weapon = "wand"
        self.inventory = []
        self.stats = {'BASE_HP': 12, 'BASE_MP': 2, 'BASE_ATK': 10, 'BASE_DFS': 5, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 4,
                      'BASE_LUCK': 6}
        self.modifiers = {'BASE_HP': 4, 'BASE_MP': 1, 'BASE_ATK': 2, 'BASE_DFS': 3, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 1,
                          'BASE_LUCK': 1}
        self.stats_init()
        self.x = 0
        self.y = 0

class Wizard(Player):
    """Defines Wizard Class"""

    def __init__(self, name):
        self.name = name
        self.class_type = "Wizard"
        self.weapon = "wand"
        self.inventory = []
        self.stats = {'BASE_HP': 12, 'BASE_MP': 2, 'BASE_ATK': 10, 'BASE_DFS': 5, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 4,
                      'BASE_LUCK': 6}
        self.modifiers = {'BASE_HP': 4, 'BASE_MP': 1, 'BASE_ATK': 2, 'BASE_DFS': 3, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 1,
                          'BASE_LUCK': 1}
        self.stats_init()
        self.x = 0
        self.y = 0
