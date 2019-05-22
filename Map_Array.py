"""
    This is the map array.
    It is 11x11. As you move through the game you are placed in one of these squares.
    To display map, run Map_Display.py
    ---Key---
    F - Forest
    D - Desert
    P - Plains
    M - Mountains
    L - Lake
    O - Ocean
    E - Erith
    T - Tundra
    S - Swamp Plains
"""

map = [
    ["F", "F", "F", "D", "D", "D", "D", "M", "M", "M", "M"],
    ["F", "F", "F", "F", "D", "D", "D", "P", "M", "P", "M"],
    ["F", "L", "F", "E", "F", "D", "P", "P", "P", "P", "M"],
    ["F", "F", "F", "M", "D", "D", "D", "P", "L", "P", "M"],
    ["F", "F", "M", "M", "M", "D", "D", "P", "L", "P", "M"],
    ["F", "F", "M", "T", "P", "M", "M", "P", "P", "P", "M"],
    ["F", "M", "T", "T", "T", "P", "P", "M", "P", "P", "M"],
    ["M", "T", "T", "T", "T", "T", "P", "P", "P", "L", "M"],
    ["T", "T", "T", "T", "T", "T", "P", "P", "P", "M", "M"],
    ["T", "T", "T", "O", "O", "T", "O", "P", "P", "P", "M"],
    ["O", "T", "O", "O", "O", "O", "O", "O", "O", "M", "M"]
]


"""This Array is for where programmed enemies spawn. They will always spawn if you land on one of these.
    It will correspond to the map array above, if you move north and it should check for enemies in this array and if yes
    then it will spawn them in and start the combat sequence.
    ---KEY---
    N - No Enemy
    B - Bandit
    W - Wolf
    T - Troll
    B - Bear"""

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