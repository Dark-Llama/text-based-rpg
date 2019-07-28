"""
    This Array is for where programmed enemies spawn. They will always spawn if you land on one of these.
    It will correspond to the map_array array above, if you move north and it should check for enemies in this array and if yes
    then it will spawn them in and start the combat sequence. This does not affect random encounters.
    ---KEY---
    N - No Enemy
    B - Bandit
    W - Wolf
    T - Troll
    B - Bear
"""

enemy_array = [
    ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],
    ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],
    ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],
    ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],
    ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],
    ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],
    ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],
    ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],
    ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],
    ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],
    ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],
    ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N"]
]
