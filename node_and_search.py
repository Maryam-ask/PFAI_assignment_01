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
            verbose: True or False. If False it prints only actions or if True it prints solutions and actions
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

    def statistics_calculator(self, depth, node_counter, cost):
        """
        A method to show statistics information of search functions.
        :param depth: depth of the last node
        :param node_counter: number of explored nodes
        :param cost: cost of solution
        :return: printing out the result
        """
        pid = os.getpid()
        process = psutil.Process(pid)
        memory_use = process.memory_info()[0] / 2. ** 30
        print('memory use:', memory_use)
        print("Elapsed time (s):", process_time()-self.start_process)
        print("Solution found at depth:", depth)
        print("Number of nodes explored:", node_counter)
        print("Cost of solution:", cost)
        print("Estimated effective branching factor:", node_counter ** (1 / depth))
        print("------------------------------------")

    def bfs(self, statistics=False):  # A parameter statistics to show information about search nodes if statistics=True
        self.start_process = process_time()
        checked_states = []  # A list for adding visited states in it
        node_counter = 0    # A counter for counting whole branches
        frontier = Queue()
        '''
        Start with the Root Node which is
        first state all miss and canns are in the right side 
        and the boat is 'r': [[0, 0], 'r', [3, 3]]
        '''
        frontier.put(self.start)

        stop = False
        while not stop:

            if frontier.empty():
                return None
            curr_node = frontier.get()

            if curr_node.goal_state():
                stop = True
                if statistics:   # statistics = true
                    self.statistics_calculator(curr_node.depth, node_counter, curr_node.cost)
                return curr_node

            successor = curr_node.successor()
            while not successor.empty():
                node_counter += 1   # Each time we expand one node, the counter will be increased by adding one
                v = successor.get()
                if v.state.state not in checked_states:  # Check if the state has already been visited
                    frontier.put(v)

                # Add the node to the visited states for next checking
                checked_states.append(v.state.state)

    def dfs(self, curr_node, visited, has_found, statistics=False, node_counter=0):
        """
        Depth-first Search is a recursive function.
        :param curr_node: The root node
        :param visited: A list for checking the already visited nodes
        :param has_found: To check if the goal state has been found
        :param statistics: if True print the information about the search method
        :param node_counter: for counting the nodes
        :return: A Node which has reach the goal state
        """
        self.start_process = process_time()
        visited.append(curr_node.state.state)
        # print(node.action, ": ", node.state.state)

        if curr_node.goal_state():
            has_found = True
        successor = curr_node.successor()
        while not successor.empty():
            v = successor.get()
            if v.state.state not in visited:
                if v.goal_state():
                    has_found = True
                    # successor = Queue()
                    if statistics:  # statistics = true
                        self.statistics_calculator(curr_node.depth, node_counter, curr_node.cost)
                    result = v
                    # print(v.action, "*: ", v.state.state)
                    return result
                else:
                    node_counter += 1
                    result = self.dfs(v, visited, has_found, statistics, node_counter)
                    return result

    def dls(self, curr_node, visited, has_found, limit, statistics=False):
        """
        It is a recursive function which is same like DFS but in DLS we have limited the depth.
        :param curr_node: The root node
        :param visited: A list for checking the already visited nodes
        :param has_found: To check if the goal state has been found
        :param limit: for limiting depth
        :param statistics: if True print the information about the search method
        :return: A Node which has reach the goal state
        """
        if limit == 0:
            if curr_node.goal_state():
                has_found = True
                return curr_node
        elif limit > 0:
            visited.append(curr_node.state.state)
            # print(node.action, ": ", node.state.state)

            if curr_node.goal_state():
                has_found = True
            successor = curr_node.successor()
            while not successor.empty():
                v = successor.get()
                if v.state.state not in visited:
                    if v.goal_state():
                        has_found = True
                        # successor = Queue()
                        result = v
                        # print(v.action, "*: ", v.state.state)
                        return result
                    else:
                        self.node_counter += 1
                        result = self.dls(v, visited, has_found, limit-1, statistics)
                        return result

    def ids(self, statistics=False):
        self.start_process = process_time()
        stop = False
        limit = 0
        while not stop:
            result = self.dls(self.start, [], False, limit, statistics)
            if result:
                if statistics:  # statistics = true
                    self.statistics_calculator(result.depth, self.node_counter, result.cost)
                # print(result.state.state)
                stop = True
                # print("*****************",limit,"*******************")
                return result
            limit += 1

    '''
    def dfs_it(self):

        checked_states = [self.start.state.state]  # A set for already visited states
                                                   # Mark the first state (Root Node) as Visited

        frontier = Queue()

        frontier.put(self.start)
        stop = False

        while not stop:
            if frontier.empty():
                return None

            curr_node = frontier.get()

            if curr_node.goal_state():
                # stop = True
                return curr_node

            if curr_node.state.state in checked_states:
                continue
            print(curr_node.action, ": ", curr_node.state.state)

            checked_states.append(curr_node.state.state)

            successor = curr_node.successor()
            while not successor.empty():  # Go down only one branch to the leaf
                v = successor.get()
                if v.state.state not in checked_states:  # Check if the state has already been visited
                    frontier.put(v)
                    if successor.empty():
                        successor = v.successor()
    '''

    def greedy_search(self, h=1, statistics=False):
        """
        A* search is using heuristic function to solve the problem. f(n) = g(n) + h(n)
        :param h: if h=1 it will use h_1(sum of misplaced tails) and if h=2 it will use h_2(manhattan distance)
        :return: A Node which has reach the goal state
        """
        self.start_process = process_time()
        frontier = PriorityQueue()
        previous_node = []

        self.start.h = self.start.state.h_1() if h == 1 else self.start.state.h_2()
        # print(self.start.g, self.start.h, self.start.f)
        frontier.put(PrioritizedItem(self.start.h, self.start))
        # print(open_list.get())
        # print(self.start.state.state)
        visited = [self.start.state.state]

        while not frontier.empty():
            curr_node = frontier.get()
            self.node_counter += 1
            # print(curr_node.item.state.state)
            if curr_node.item.goal_state():
                if statistics:  # statistics = true
                    self.statistics_calculator(curr_node.item.depth, self.node_counter, curr_node.item.cost)
                return curr_node.item

            successors = curr_node.item.successor()
            while not successors.empty():
                successor = successors.get()
                if successor.state.state not in visited:
                    if successor.goal_state():
                        if statistics:  # statistics = true
                            self.statistics_calculator(successor.depth, self.node_counter, successor.cost)
                        return successor
                    visited.append(successor.state.state)
                    h = successor.state.h_1() if h == 1 else successor.state.h_2()
                    frontier.put(PrioritizedItem(h, successor))
        return False

    # A * Search Algorithm
    def a_star_search(self, h=1, statistics=False):
        """
        Greedy search is using heuristic function to find the solution.
        :param h: if h=1 it will use h_1(sum of misplaced tails) and if h=2 it will use h_2(manhattan distance)
        :return: A Node which has reach the goal state
        """
        self.start_process = process_time()
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
            self.node_counter += 1
            # print(curr_node.item.state.state)
            if curr_node.item.goal_state():
                if statistics:  # statistics = true
                    self.statistics_calculator(curr_node.item.depth, self.node_counter, curr_node.item.cost)
                return curr_node.item

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
                        if successor.goal_state():
                            if statistics:  # statistics = true
                                self.statistics_calculator(successor.depth, self.node_counter, successor.cost)
                            return successor
                        visited.append(successor.state.state)
                        frontier.put(PrioritizedItem(successor.f, successor))

        return False


