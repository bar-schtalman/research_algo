from typing import Any


def breadth_first_search(start, end, neighbor_function) -> list:
    """
    description: this function performe bfs search from origin point to destination and provide possible path steps with neighbor_function constraints
    :param: start point, end point, neighbor_function
    :returns possible path steps.... //should have return optimal path
    >>> breadth_first_search(start = (0,0), end = (1,0),neighbor_function= four_neighbor_function)
    [(0, 0), (1, 0)]
    >>> breadth_first_search(start = (1,5), end = (3,-2),neighbor_function= four_neighbor_function)
    [(1, 5), (2, 5), (1, 4), (3, 5), (2, 4), (1, 3), (3, 4), (2, 3), (1, 2), (3, 3), (2, 2), (1, 1), (3, 2), (2, 1), (1, 0), (3, 1), (2, 0), (1, -1), (3, 0), (2, -1), (1, -2), (3, -1), (2, -2), (3, -2)]
    >>> breadth_first_search(start = (-1,-1), end = (0,0),neighbor_function= four_neighbor_function)
    [(-1, -1), (0, -1), (-1, 0), (0, 0)]
    >>> breadth_first_search(start = (0,0), end = (1,2),neighbor_function= two_neighbor_function)
    [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2)]
    >>> breadth_first_search(start = (15,13), end = (15,15),neighbor_function= two_neighbor_function)
    [(15, 13), (15, 14), (15, 15)]
    >>> breadth_first_search(start = (0,0), end = (0,0),neighbor_function= four_neighbor_function)
    [(0, 0)]
    >>> breadth_first_search(start = (-45,0), end = (-45,0),neighbor_function= two_neighbor_function)
    [(-45, 0)]


    """
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


def two_neighbor_function(node: Any) -> list:
    (x, y) = node
    return [(x + 1, y), (x, y + 1)]

if __name__ == '__main__':
    import doctest

    doctest.testmod()
