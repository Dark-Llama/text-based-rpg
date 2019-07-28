from map.map_array import *


def map_display():
    for r in map_array:
        for c in r:
            print(c,end = " ")
        print()
