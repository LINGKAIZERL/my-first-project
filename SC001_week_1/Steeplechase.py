"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    pass
 for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
def jump():
    up()
    cross()
    down()
def up():
    turn_left() #facing north
    while not right_is_clear():
        move()
def cross():
    turn_right()
    move()
    turn_right()
def down():
    while front_is_clear():
        move()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
move()
pick_beeper()














####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
