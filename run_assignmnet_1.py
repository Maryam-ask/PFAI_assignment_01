'''
Define problem and start execution of search problems

Author: Tony Lindgren

Completed by: Maryam Askari & Mahtab BabaMohammadi

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
    BFS:
    """
    #solution = sa.bfs()
    #solution = sa.bfs(statistics=True)


    """
    DFS:
    """
    #solution = sa.dfs(sa.start, [], has_found=False)
    #solution = sa.dfs(sa.start, [], has_found=False, statistics=True)


    """
    IDS: 
    """
    #solution = sa.ids()
    #solution = sa.ids(statistics=True)

    """
    Printing out the solution of missionaries_and_cannibals with pretty_print_solution:
    """
    #mc.pretty_print()
    #solution.pretty_print_solution(True)   # Verbose = True for printing actions and states
    #solution.pretty_print_solution1(False)    # verbose = False for only printing actions

    """
    ********************************************************************************************************************
    Eight_Puzzle problem 
    """
    initial_state = [[7, 2, 4], [5, 'e', 6], [8, 3, 1]]
    goal_state = [['e', 1, 2], [3, 4, 5], [6, 7, 8]]

    puzzle = EightPuzzle(initial_state, goal_state)
    sa = SearchAlgorithm(puzzle)

    # print(puzzle.h_2())   # manhattan distance
    # print(puzzle.h_1())   # number of tails out of place
    # print(e_position)

    """
    Greedy search with h=1 to solve the problem with number of misplaced tiles heuristic function.
    """
    #solution = sa.greedy_search()
    #solution = sa.greedy_search(statistics=True)

    """
    Greedy search with h=2 to solve the problem with manhattan distance heuristic function.
    """
    #solution = sa.greedy_search(h=2)
    #solution = sa.greedy_search(h=2, statistics=True)

    """
    A_Star search with h=1
    """
    #solution = sa.a_star_search()
    # solution = sa.a_star_search(statistics=True)

    """
    A_Star search with h=2
    """
    # solution = sa.a_star_search(h=2)
    #solution = sa.a_star_search(h=2, statistics=True)

    '''
    BFS:
    '''
    #solution = sa.bfs(statistics=True)

    '''
    DFS:
    '''
    solution = sa.dfs(sa.start, [], has_found=False, statistics=True)

    '''
    IDS:
    '''
    #solution = sa.ids(statistics=True)

    """
    Printing out the solution with pretty_print_solution:
    """
    #puzzle.pretty_print()
    #solution.pretty_print_solution(True)    # Verbose = True for printing actions and states
    #solution.pretty_print_solution()       # verbose = False for only printing actions



if __name__ == "__main__":
    main()