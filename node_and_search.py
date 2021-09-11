'''
Define nodes of search tree and vanilla bfs search algorithm

Author: Tony Lindgren

Completed by: Maryam Askari & Mahtab BMohammadi
'''

from queue import *
import os
import psutil
from time import process_time


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

    def bfs(self, statistics=False):
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
                    pid = os.getpid()
                    process = psutil.Process(pid)
                    memoryUse = process.memory_info()[0] / 2. ** 30
                    print('memory use:', memoryUse)
                    print("Elapsed time (s):", process_time())
                    print("Solution found at depth:", curr_node.depth)
                    print("Number of nodes explored:", node_counter)
                    print("Cost of solution:", curr_node.cost)
                    print("Estimated effective branching factor:", )  # TODO: We need to calculate and add effective branching
                return curr_node

            successor = curr_node.successor()
            while not successor.empty():
                node_counter += 1   # Each time we expand one node, the counter will be increased by adding one
                v = successor.get()
                if v.state.state not in checked_states:  # Check if the state has already been visited
                    frontier.put(v)

                # Add the node to the visited states for next checking
                checked_states.append(v.state.state)

    def dfs(self, node, visited, has_found):

        visited.append(node.state.state)
        print(node.action, ": ", node.state.state)

        if node.goal_state():
            has_found = True
        successor = node.successor()
        while not successor.empty():
            v = successor.get()
            if v.state.state not in visited:
                if v.goal_state():
                    has_found = True
                    successor = Queue()
                    result = v
                    print(v.action, "*: ", v.state.state)
                    return result
                else:
                    result = self.dfs(v, visited, has_found)
                    return result


    def dfs_it(self):

        checked_states = [self.start.state.state]  # A set for already visited states
                                                   # Mark the first state (Root Node) as Visited

        frontier = Queue()
        '''
        Start with the Root Node which is
        first state all miss and canns are in the right side 
        and the boat is 'r'
        '''
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
    def dls(self, curr_node, limit):
        if curr_node.goal_state():
            return True
        if limit <= 0:
            return False

        successor = curr_node.successor()
        if not successor.empty():
            for v in iter(successor.get, None):  # Go down only one branch to the leaf
                if self.dls(v, limit-1):
                    return True
            return False

    def ids(self, limit):
        for i in range(limit):
            if self.dls(self.start, limit):
                return True
            return False
    '''

    def dls(self, limit):
        checked_states = set()  # A set for already visited states
        checked_states.add(self.start)  # Mark the first state (Root Node) as Visited

        frontier = Queue()
        '''
        Start with the Root Node which is
        first state all miss and canns are in the right side 
        and the boat is 'r'
        '''
        frontier.put(self.start)
        stop = False

        while not stop:
            if frontier.empty():
                return None
            curr_node = frontier.get()
            if curr_node in checked_states:
                continue
            if curr_node.goal_state():
                # stop = True
                return curr_node
            checked_states.add(successor)
            successor = curr_node.successor()
            while not successor.empty():
                if successor not in checked_states:  # Check if the state has already been visited
                    # Add the node to the visited states for next checking
                    frontier.put(successor.get())
