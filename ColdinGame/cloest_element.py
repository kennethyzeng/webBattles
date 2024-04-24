import sys
import math

# CodinGame planet is being attacked by slimy insectoid aliens.
# <---
# Hint:To protect the planet, you can implement the pseudo-code provided in the statement, below the player.

class Enemy:

    __name: str
    __dist: int

    def __init__(self, name: str, distance: int = 0):
        self.__name = name
        self.__dist = distance


    def __le__(self, enemy):
        # nothing to compare with
        if not enemy:
            return True
        # TODO Handle not an enemy object
        # comparaison
        return self.__dist <= enemy.dist


    @property
    def name(self):
        return self.__name

    @property
    def dist(self):
        return self.__dist

    


# game loop
while True:
    enemy_1 = input()  # name of enemy 1
    dist_1 = int(input())  # distance to enemy 1
    enemy_2 = input()  # name of enemy 2
    dist_2 = int(input())  # distance to enemy 2

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    enemy_obj_1 = Enemy(name=enemy_1, distance=dist_1)
    enemy_obj_2 = Enemy(name=enemy_2, distance=dist_2)

    if enemy_obj_1 <= enemy_obj_2:
        print(enemy_obj_1.name)
    else:
        print(enemy_obj_2.name)

    # You have to output a correct ship name to shoot ("Buzz", enemy1, enemy2, ...)
    
