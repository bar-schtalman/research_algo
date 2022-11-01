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
        # print(someone)
        if (curr) == end:
            return nei_lst


        for ni in neighbor_function(curr):
            if not ((ni[0] < start[0] and ni[0] < end[0]) or  (ni[0] > start[0] and ni[0] > end[0]) or  (
                    ni[1] < start[1] and ni[1] < end[1]) or  (ni[1] > start[1] and ni[1] > end[1])):
                if ni not in visited:
                    visited.append(curr)
                    visited.append(ni)
                    nei_lst.append(ni)
                    queue.append(ni)




def four_neighbor_function(node: Any) -> list:
    (x, y) = node
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

print(breadth_first_search(start=(0, 0), end=(3, 3), neighbor_function=four_neighbor_function))
