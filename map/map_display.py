from map.map_array import *


def map_display():
    for r in game_map:
        for c in r:
            print(c,end = " ")
        print()
