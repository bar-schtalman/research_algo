from typing import Iterable


def deep_sort(x):
    if not isinstance(x, list) and not isinstance(x, set) and not isinstance(x, tuple) and not isinstance(x, dict):
        return x

    # Sort own
    if isinstance(x, dict):
        outdict = dict(sorted(x.items()))
    else:
        outdict = sorted(x)

    # Sort children
    for element in enumerate(outdict):
        if isinstance(x, dict):
            key = element[1]
        else:
            key = element[0]
        outdict[key] = deep_sort(outdict[key])

    return outdict


def print_sorted(x):
    print(deep_sort(x))





x = {'a': 5,'g':(3,2,1), 'c': [1, 3, 5, 4], 'd': 6, 'b': {'z': 1,'y': 'idgg' ,'f':[2,1,4,3],'gf':{'d':54,'c':23}, 'h': 5,'j':{'b':12,'a':13}}}
##{'a': 5, 'b': {'f': [1, 2, 3, 4], 'h': 5, 'j': {'a': 13, 'b': 12}, 'y': 'dggi', 'z': 1}, 'c': [1, 3, 4, 5], 'd': 6}
print_sorted(x)









#print_sorted(y)
#recursive_sort(x)


