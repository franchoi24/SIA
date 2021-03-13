from game.Sokoban import Sokoban
from game import Constants
from NotInformed.Bfs import Bfs
from NotInformed.Dfs import Dfs
from NotInformed.Iddfs import Iddfs
from Informed.Greedy import Greedy
from collections import deque
import time
import json


def main():
    
    # objective = [(2,5),(6,5)]
    # dimensions = (9,9)
    # boxes = [(5,5), (3,5)]
    # walls = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
    #         (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
    #         (8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),
    #         (1,8),(2,8),(3,8), (4,8),(5,8),(6,8),(7,8)]
    # player = (4, 5)
    # sokoban = Sokoban(walls, objective, dimensions, player, boxes)

    objective = [(0,0), (2,2)]
    dimensions = (5,5)
    boxes = [(0,1), (1, 2)]
    walls = [(3,3), (4,4),(3,2), (3,1)]
    player = (4, 3)
    sokoban = Sokoban(walls, objective, dimensions, player, boxes)

    with open('config.json') as config:
        data = json.load(config)

    algorithm = data['algorithm']
    level_map = data['level_map']
    heuristic = data['heuristic']
    iddfs_max_depth = data["iddfs_max_depth"]
    print("Algorithm is:", algorithm)
    print()


    if algorithm == "bfs":
        start = time.time()
        aux = Bfs(sokoban)
        res = aux.start()
        print(time.time() - start)

    elif algorithm == "dfs":
        start = time.time()
        aux = Dfs(sokoban)
        res = aux.start()
        print(time.time() - start)

    elif algorithm == "iddfs":
        print("Max depth for IDDFS is:", iddfs_max_depth)
        start = time.time()
        aux = Iddfs(sokoban, iddfs_max_depth)
        res = aux.start()
        print(time.time() - start)
    elif algorithm == "greedy":
        start = time.time()
        aux = Greedy(sokoban, heuristic)
        res = aux.start()
        print(time.time() - start)
    else:
        print("Invalid algorithm.")
        exit()

    if res.result:
        for n in res.solutionNodePath:
            n.sokoban.printBoard(mode='vis')




if __name__ == "__main__":
    main()


