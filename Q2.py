import types
from typing import Any

def breadth_first_search(start, end, neighbor_function)->list:
    nei_lst = []
    visited = []
    queue = []
    queue.append(start)
    visited.append(start)
    while len(queue) > 0:
        someone = queue.pop(0)
        print(someone)
        if (someone) == end:
            return nei_lst
        for ni in neighbor_function(someone):
            if ni not in visited:
                if someone
                    nei_lst.append(ni)
                    queue.append(ni)
                    visited.append(ni)




def four_neighbor_function(node:Any)->list:
    (x,y) = node
    return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

print(breadth_first_search(start=(0,0), end=(2,2), neighbor_function= four_neighbor_function))