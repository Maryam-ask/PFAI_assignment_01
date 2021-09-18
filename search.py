'''
Define nodes of search tree and vanilla bfs search algorithm

Author: Tony Lindgren

Completed by: Maryam Askari & Mahtab Babamohammadi
'''

from queue import *
import os
import psutil
from time import process_time
from dataclasses import dataclass, field
from typing import Any
from queue import PriorityQueue


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)

class Node:
    '''
    This class defines nodes in search trees. It keep track of:
    state, cost, parent, action, and depth
    '''

    def __init__(self, state, cost=0, parent=None, action=None):
        self.parent = parent
        self.state = state
        self.action = action
        self.cost = cost
        self.depth = 0
        self.g = 9999999 #we need to calculate this three attributes
        self.h = 0
        self.f = 9999999
        if parent:
            self.depth = parent.depth + 1

    def goal_state(self):
        return self.state.check_goal()

    def successor(self):
        successors = Queue()
        for action in self.state.action:
            child = self.state.move(action)
            if child != None:
                childNode = Node(child, self.cost + 1, self, action)
                successors.put(childNode)
        return successors

    def pretty_print_solution(self, verbose=False):
        """
        A recursive method to print the whole solution.
        Args :
            verbose: True or False for printing only actions or printing solutions and actions
        """
        if self.parent is None:
            return
        if verbose:
            self.parent.pretty_print_solution(verbose)
            print("action:", self.action)
            self.state.pretty_print()
        elif not verbose:
            print("Action: ", self.parent.action)
            self.parent.pretty_print_solution(verbose)


class SearchAlgorithm:
    '''
    Class for search algorithms, call it with a defined problem
    '''

    def __init__(self, problem):
        self.start = Node(problem)
        self.start_process = process_time()
        self.node_counter = 0

    # A * Search Algorithm
    def a_star(self, h=1):
        frontier = PriorityQueue()
        previous_node = []

        self.start.g = 0
        self.start.h = self.start.state.h_1() if h == 1 else self.start.state.h_2()
        self.start.f = self.start.g + self.start.h
        # print(self.start.g, self.start.h, self.start.f)
        frontier.put(PrioritizedItem(self.start.f, self.start))
        # print(open_list.get())
        # print(self.start.state.state)
        visited = [self.start.state.state]

        while not frontier.empty():
            curr_node = frontier.get()
            print(curr_node.item.state.state)
            if curr_node.item.goal_state():
                return curr_node.item.state.state

            successors = curr_node.item.successor()
            while not successors.empty():
                successor = successors.get()
                new_g = curr_node.item.g + 1
                if new_g < successor.g:
                    successor.g = new_g
                    successor.h = successor.state.h_1() if h == 1 else successor.state.h_2()
                    successor.f = successor.g + successor.h
                    if successor.state.state not in visited:
                        # print(successor.state.state)
                        visited.append(successor.state.state)
                        frontier.put(PrioritizedItem(successor.f, successor))


        return False






