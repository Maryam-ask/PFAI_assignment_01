# =============================================================================
# Created By : Maryam Askari
# Date: 9/12/2021
# Time: 12:21 PM
# =============================================================================
"""The Module Has Been Build for..."""
# =============================================================================
# Imports
# =============================================================================
import queue
from eight_puzzle import EightPuzzle
from node_and_search import Node

initial_state = [[7, 2, 4], [5, 'e', 6], [8, 3, 1]]
goal_state = [['e', 1, 2], [3, 4, 5], [6, 7, 8]]

puzzle = EightPuzzle(initial_state,goal_state)
node = Node(puzzle)

for i in range(5):
    q = queue.PriorityQueue()
    q.get(initial_state)
    node = q.get()
    successor = node.successor()
    while not successor.empty():
        v = successor.get()
        print(v.state.state)
        print(v.state.h_1())
        print(v.state.h_2())
        q.put(v.state.state)




print("Start State: ")
#puzzle.pretty_print()
"""print(puzzle.h_2())
print(puzzle.h_1())"""
#print(e_position)