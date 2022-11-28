from typing import Iterable

def print_sorted(x):
    """
    description: this function use recursion to perform deep sort in different levels for list, dict, set and tuple
    :param: x - any list / set / tuple / dict
    :returns sorted data structure in all levels
    >>> print_sorted({'a': 5,'g':(3,2,1), 'c': [1, 3, 5, 4], 'd': 6, 'b': {'z': 1,'y': 'idgg' ,'f':[2,1,4,3],'gf':{'d':54,'c':23}, 'h': 5,'j':{'b':12,'a':13}}})
    {'a': 5, 'b': {'f': [1, 2, 3, 4], 'gf': {'c': 23, 'd': 54}, 'h': 5, 'j': {'a': 13, 'b': 12}, 'y': 'idgg', 'z': 1}, 'c': [1, 3, 4, 5], 'd': 6, 'g': [1, 2, 3]}
    >>> print_sorted((3,1,2))
    [1, 2, 3]
    >>> print_sorted({"ds" : "math", "yud" : "biology", "aaa" : "bbb","aa" : {'c' : 3, 'a' : 1, 'b' : 2}})
    {'aa': {'a': 1, 'b': 2, 'c': 3}, 'aaa': 'bbb', 'ds': 'math', 'yud': 'biology'}
    >>> print_sorted(("its","election","day","today"))
    ['day', 'election', 'its', 'today']
    >>> print_sorted({'c' : (1,8,99,10,54), 'bb': (11,-2,3,1,6,2,67,24,766543,234,67,32,2,5), 'abc': (3,5,4312,456,52325,-32323,-1234,-434,123,45)})
    {'abc': [-32323, -1234, -434, 3, 5, 45, 123, 456, 4312, 52325], 'bb': [-2, 1, 2, 2, 3, 5, 6, 11, 24, 32, 67, 67, 234, 766543], 'c': [1, 8, 10, 54, 99]}
    >>> print_sorted({'f': ('g','f','c','cd','asc'), 'a': (3.1233,3.1231,0.543,1.00), 'b' :(True,False,False,False), 'c' : ["im","so","lonely"], 'cf': (4,13,546,12,0,-1,3,44)})
    {'a': [0.543, 1.0, 3.1231, 3.1233], 'b': [False, False, False, True], 'c': ['im', 'lonely', 'so'], 'cf': [-1, 0, 3, 4, 12, 13, 44, 546], 'f': ['asc', 'c', 'cd', 'f', 'g']}
    """
    print(deep_sort(x))




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





if __name__ == '__main__':
    import doctest

    doctest.testmod()






