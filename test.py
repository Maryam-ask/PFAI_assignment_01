# =============================================================================
# Created By : Maryam Askari
# Date: 9/12/2021
# Time: 12:21 PM
# =============================================================================
"""The Module Has Been Build for..."""
# =============================================================================
# Imports
# =============================================================================

from eight_puzzle import EightPuzzle
from node_and_search import Node

initial_state = [[7, 2, 4], [5, 'e', 6], [8, 3, 1]]
goal_state = [['e', 1, 2], [3, 4, 5], [6, 7, 8]]

puzzle = EightPuzzle(initial_state,goal_state)
print("Start State: ")
#puzzle.pretty_print()
node = Node(puzzle)
print(node.h_2())
print(node.h_1())
#print(e_position)