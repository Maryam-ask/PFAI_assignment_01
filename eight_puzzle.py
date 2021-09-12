"""
Eight puzzle problem

Author: Maryam Askari & Mahtab BMohammadi
"""
from copy import deepcopy


class EightPuzzle:
    def __init__(self, initial_state, goal):
        self.state = initial_state
        self.goal = goal
        self.action = ["up", "down", "left", "right"]
        self.e_position = self.state[1][1]

    def check_goal(self):
        if self.state == self.goal:
            return True
        else:
            return False

    def move(self, move):
        if move == "up":
            dc = deepcopy(self)

    def pretty_print(self):
        """
        A Method to print out the states
        """
        print('----------------------------')
        print("[", self.state[0][0], ",", self.state[0][1], ",", self.state[0][2], "]", ","
              "[", self.state[1][0], ",", self.state[1][1], ",", self.state[1][2], "]", ",",
              "[", self.state[2][0], ",", self.state[2][1], ",", self.state[2][2], "]]")
        print('----------------------------')
