from character_setup import *


class enemy(character):
    def __init__(self):
        pass


"""Beast Enemies"""


class wolf(enemy):
    """Create wolf enemy"""

    def __init__(self):
        self.name = "wolf"
        self.hp = 22
        self.mp = 0
        self.atk = 4
        self.dfs = 2
        self.spd = 4
        self.luck = 10
        self.exp = 5


class bear(enemy):
    """Create bear enemy"""

    def __init__(self):
        self.name = "bear"
        self.hp = 260
        self.mp = 0
        self.atk = 30
        self.dfs = 4
        self.spd = 30
        self.luck = 10
        self.exp = 50


class troll(enemy):
    """Create troll enemy"""

    def __init__(self):
        self.name = "troll"
        self.hp = 280
        self.mp = 0
        self.atk = 35
        self.dfs = 4
        self.spd = 340
        self.luck = 10
        self.exp = 50


"""bandit Enemies"""


class bandit(enemy):
    """Create bandit enemy"""

    def __init__(self):
        self.name = "bandit"
        self.hp = 35
        self.mp = 0
        self.atk = 35
        self.dfs = 4
        self.spd = 70
        self.luck = 20
        self.exp = 10


class bandit_outlaw(enemy):
    """Create bandit_outlaw enemy"""

    def __init__(self):
        self.name = "bandit Outlaw"
        self.hp = 109
        self.mp = 25
        self.atk = 43
        self.dfs = 8
        self.spd = 86
        self.luck = 25
        self.exp = 15


class bandit_thug(enemy):
    """Create bandit_thug enemy"""

    def __init__(self):
        self.name = "bandit Thug"
        self.hp = 238
        self.mp = 25
        self.atk = 53
        self.dfs = 8
        self.spd = 107
        self.luck = 25
        self.exp = 25


class bandit_highwayman(enemy):
    """Create bandit_highwayman enemy"""

    def __init__(self):
        self.name = "bandit Highwayman"
        self.hp = 318
        self.mp = 25
        self.atk = 76
        self.dfs = 8
        self.spd = 152
        self.luck = 25
        self.exp = 45


class bandit_plunderer(enemy):
    """Create bandit_plunderer enemy"""

    def __init__(self):
        self.name = "bandit Plunderer"
        self.hp = 398
        self.mp = 25
        self.atk = 86
        self.dfs = 8
        self.spd = 172
        self.luck = 25
        self.exp = 60


class bandit_marauder(enemy):
    """Create bandit_marauder enemy"""

    def __init__(self):
        self.name = "bandit Marauder"
        self.hp = 489
        self.mp = 25
        self.atk = 123
        self.dfs = 8
        self.spd = 246
        self.luck = 25
        self.exp = 75
