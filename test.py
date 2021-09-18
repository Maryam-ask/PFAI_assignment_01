# =============================================================================
# Created By : Maryam Askari
# Date: 9/12/2021
# Time: 12:21 PM
# Authors: Maryam Askari - Mahtab Babamohammadi
# =============================================================================
"""The Module Has Been Build for..."""
# =============================================================================
# Imports
# =============================================================================

from eight_puzzle import EightPuzzle
from search import Node, SearchAlgorithm

initial_state = [[7, 2, 4], [5, 'e', 6], [8, 3, 1]]
goal_state = [['e', 1, 2], [3, 4, 5], [6, 7, 8]]

puzzle = EightPuzzle(initial_state, goal_state)
# print("Start State: ")
# puzzle.pretty_print()
# print(puzzle.h_2())
# print(puzzle.h_1())
# print(e_position)
sa = SearchAlgorithm(puzzle)
print(sa.a_star())

