'''
Define problem and start execution of search problems

Author: Tony Lindgren

Completed by: Maryam Askari & Mahtab BMohammadi

'''

from missionaries_and_cannibals import MissionariesAndCannibals
from node_and_search import SearchAlgorithm
from eight_puzzle import EightPuzzle


def main():
    """
    The first codes are used to solve the missionaries and cannibals problem
    and the other part is to solve the eight_puzzle problem.
    """
    init_state = [[0, 0], 'r', [3, 3]]
    goal_state = [[3, 3], 'l', [0, 0]]
    mc = MissionariesAndCannibals(init_state, goal_state)
    sa = SearchAlgorithm(mc)
    """
    To print the solution through BFS search:
    """
    #mc.pretty_print()
    # solution = sa.bfs()
    # solution = sa.bfs(True)  # BFS using Statistics = True
    #solution.pretty_print_solution1(False)    # verbose = False for only printing actions
    # solution.pretty_print_solution(True)   # Verbose = True for printing actions and states

    """
    To print the solution through DFS search
    """
    # mc.pretty_print()
    # solution = sa.dfs(sa.start, [], False)
    # solution = sa.dfs(sa.start, [], False, True)   # Statistics = True
    # solution.pretty_print_solution(True)   # Verbose = True
    #solution.pretty_print_solution()       # verbose = False

    """
    To print the solution through IDS search 
    """
    # solution = sa.ids(True)
    # solution.pretty_print_solution(True)

    # Eight_puzzle
    initial_state = [[7, 2, 4], [5, 'e', 6], [8, 3, 1]]
    goal_state = [['e', 1, 2], [3, 4, 5], [6, 7, 8]]

    puzzle = EightPuzzle(initial_state, goal_state)
    # print("Start State: ")
    # puzzle.pretty_print()
    # print(puzzle.h_2())
    # print(puzzle.h_1())
    # print(e_position)
    sa = SearchAlgorithm(puzzle)
    # solution = sa.greedy_search(statistics=True)
    # solution.pretty_print_solution(True)
    # solution = sa.a_star_search(statistics=True)
    # solution.pretty_print_solution(True)
    #print(dfs_rec.action, "**: ", dfs_rec.state.state)
    #print(dfs_rec)
    # if solution:
    #    print("Answer found")

    #solution.pretty_print_solution()
    # print(solution)
    '''
    print('BFS')
    print('Start state: ')
    mc.pretty_print()
    goal_node = sa.bfs()
    print('goal state: ')
    goal_node.state.pretty_print()
    '''

if __name__ == "__main__":
    main()