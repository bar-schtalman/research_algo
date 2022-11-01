from typing import Any


def breadth_first_search(start, end, neighbor_function) -> list:
    visited = []
    nei_lst = []
    nei_lst.append(start)
    queue = []
    queue.append(start)
    visited.append(start)
    while len(queue) > 0:
        curr = queue.pop(0)
        visited.append(curr)
        # print(someone)
        newlist = []
        size = len(nei_lst)
        if (curr) == end:
            """
            for count,i in enumerate(nei_lst):
                for j in range(size):
                    tup = newlist[count]
                    if  tup[0] == i[0] and tup[1] == i[1]+1"""
            return nei_lst

        con = True
        while con:
            for ni in neighbor_function(curr):
                if not ((ni[0] < start[0] and ni[0] < end[0]) or (ni[0] > start[0] and ni[0] > end[0]) or (
                        ni[1] < start[1] and ni[1] < end[1]) or (ni[1] > start[1] and ni[1] > end[1])):
                    tupp = (ni[1], ni[0])
                    if ni not in visited:
                        curr = ni
                        visited.append(ni)
                        nei_lst.append(ni)
                        queue.append(ni)
                    con = False




def four_neighbor_function(node: Any) -> list:
    (x, y) = node
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

print(breadth_first_search(start=(0, 0), end=(1, 1), neighbor_function=four_neighbor_function))
