"""
    This is the game_map array.
    It is 11x11. As you move through the game you are placed in one of these squares.
    To display game_map, run map_display.py
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

game_map = [
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
