"""
Eight puzzle problem

Author: Maryam Askari & Mahtab BabaMohammadi
"""
from copy import deepcopy


class EightPuzzle:
    def __init__(self, initial_state, goal, eight_value="e"):
        self.state = initial_state
        self.eight_value = eight_value
        self.goal = goal
        self.action = ["up", "down", "left", "right"]

    def check_goal(self):
        if self.state == self.goal:
            return True
        else:
            return False

    def get_e_position(self, index):
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] == self.eight_value:
                    return (i, j)[index]

    def move(self, move):
        dc = deepcopy(self)
        if move == "up":
            if dc.up():
                return dc
        elif move == "down":
            if dc.down():
                return dc
        elif move == "right":
            if dc.right():
                return dc
        elif move == "left":
            if dc.left():
                return dc

    def up(self):
        i = self.get_e_position(0)
        j = self.get_e_position(1)
        if 0 < i <= (len(self.state) - 1):
            self.state[i][j] = self.state[i - 1][j]
            self.state[i - 1][j] = self.eight_value
            return True

    def down(self):
        i = self.get_e_position(0)
        j = self.get_e_position(1)
        if 0 <= i < (len(self.state) - 1):
            self.state[i][j] = self.state[i + 1][j]
            self.state[i + 1][j] = self.eight_value
            return True

    def right(self):
        i = self.get_e_position(0)
        j = self.get_e_position(1)
        if 0 <= j < (len(self.state[i]) - 1):
            self.state[i][j] = self.state[i][j + 1]
            self.state[i][j + 1] = self.eight_value
            return True
        else:
            return False

    def left(self):
        i = self.get_e_position(0)
        j = self.get_e_position(1)
        if 0 < j <= (len(self.state[i]) - 1):
            self.state[i][j] = self.state[i][j - 1]
            self.state[i][j - 1] = self.eight_value
            return True
        else:
            return False


    def h_1(self):
        misplaced_tails = 0
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                value = self.state[i][j]
                for count, x in enumerate(self.goal):
                    if value in x:
                        goal_index = (count, x.index(value))
                        if not (goal_index[0] == i and goal_index[1]==j):
                            misplaced_tails +=1

        return misplaced_tails

    def h_2(self):
        '''
        A method to calculate manhattan distance through sum of the moves.
        :return: manhattan distance
        '''
        manhattan_distance = 0
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                value = self.state[i][j]
                for count, x in enumerate(self.goal):
                    if value in x:
                        goal_index = (count, x.index(value))
                        manhattan_distance += abs(goal_index[0]-i) + abs(goal_index[1]-j)

        return manhattan_distance



    def pretty_print(self):
        """
        A Method to print out the states
        """
        print("-------------------------------")
        for j in self.state:
            [print(i, end="\t\t") for i in j]
            print()
        print("-------------------------------")
