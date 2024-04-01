"""
File: Steeplechase.py
Name: 張意鈞
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()

def jump():
    """
   pre-condition:Karel is on the left side of the wall,facing East
   post-condition:Karel is on the right side of the wall
    """
    up()
    cross()
    down()
def down():
    """
     pre - condition:Karel is at the upper right, facing South
     post - condition:Karel is facing South

    """
    while front_is_clear():
        move()
def cross():
    """
    pre - condition:Karel is facing North
    post - condition:Karel is at the upper right,facing South

"""
    turn_right()
    move()
    turn_right()
def up():
    """
   pre-condition:Karel is on the left side of the wall,facing East
   post-condition:Karel is facing North
    """
    turn_left()
    #Facing North
    while not right_is_clear():
        move()
    """
    while not  front_is_clear():
        turn_left()
        move()
        turn_right()
        """

def turn_right():
    turn_left()
    turn_left()
    turn_left()





# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
