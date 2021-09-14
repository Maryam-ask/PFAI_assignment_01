'''
Define problem and start execution of search problems

Author: Tony Lindgren

Completed by: Maryam Askari & Mahtab BMohammadi

'''

from missionaries_and_cannibals import MissionariesAndCannibals
from node_and_search import SearchAlgorithm

init_state = [[0, 0], 'r', [3, 3]]
goal_state = [[3, 3], 'l', [0, 0]]


def main():
    mc = MissionariesAndCannibals(init_state, goal_state)
    sa = SearchAlgorithm(mc)
    # print(sa)
    # print(mc)
    # solution = sa.bfs(True)
    # solution.pretty_print_solution1(False)
    #solution.pretty_print_solution(True)

    # solution = sa.dfs(sa.start, [], False, True)
    # solution.pretty_print_solution(True)

    solution = sa.ids(True)
    solution.pretty_print_solution(True)
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