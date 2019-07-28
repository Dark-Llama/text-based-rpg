from character_setup import *


class Enemy(Character):
    def __init__(self):
        pass


"""Beast Enemies"""


class Wolf(Enemy):
    """Create Wolf Enemy"""

    def __init__(self):
        self.name = "Wolf"
        self.hp = 22
        self.mp = 0
        self.atk = 4
        self.dfs = 2
        self.spd = 4
        self.luck = 10
        self.exp = 5


class Bear(Enemy):
    """Create Bear Enemy"""

    def __init__(self):
        self.name = "Bear"
        self.hp = 260
        self.mp = 0
        self.atk = 30
        self.dfs = 4
        self.spd = 30
        self.luck = 10
        self.exp = 50


class Troll(Enemy):
    """Create Troll Enemy"""

    def __init__(self):
        self.name = "Troll"
        self.hp = 280
        self.mp = 0
        self.atk = 35
        self.dfs = 4
        self.spd = 340
        self.luck = 10
        self.exp = 50


"""Bandit Enemies"""


class Bandit(Enemy):
    """Create Bandit Enemy"""

    def __init__(self):
        self.name = "Bandit"
        self.hp = 35
        self.mp = 0
        self.atk = 35
        self.dfs = 4
        self.spd = 70
        self.luck = 20
        self.exp = 10


class BanditOutlaw(Enemy):
    """Create BanditOutlaw Enemy"""

    def __init__(self):
        self.name = "Bandit Outlaw"
        self.hp = 109
        self.mp = 25
        self.atk = 43
        self.dfs = 8
        self.spd = 86
        self.luck = 25
        self.exp = 15


class BanditThug(Enemy):
    """Create BanditThug Enemy"""

    def __init__(self):
        self.name = "Bandit Thug"
        self.hp = 238
        self.mp = 25
        self.atk = 53
        self.dfs = 8
        self.spd = 107
        self.luck = 25
        self.exp = 25


class BanditHighwayman(Enemy):
    """Create BanditHighwayman Enemy"""

    def __init__(self):
        self.name = "Bandit Highwayman"
        self.hp = 318
        self.mp = 25
        self.atk = 76
        self.dfs = 8
        self.spd = 152
        self.luck = 25
        self.exp = 45


class BanditPlunderer(Enemy):
    """Create BanditPlunderer Enemy"""

    def __init__(self):
        self.name = "Bandit Plunderer"
        self.hp = 398
        self.mp = 25
        self.atk = 86
        self.dfs = 8
        self.spd = 172
        self.luck = 25
        self.exp = 60


class BanditMarauder(Enemy):
    """Create BanditMarauder Enemy"""

    def __init__(self):
        self.name = "Bandit Marauder"
        self.hp = 489
        self.mp = 25
        self.atk = 123
        self.dfs = 8
        self.spd = 246
        self.luck = 25
        self.exp = 75
