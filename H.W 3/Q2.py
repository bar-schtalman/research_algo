from typing import Callable, Any


def find(algorithm: Callable, items: Any):
    """
    this design-pattern here for finding first two highest element in any data structer and compute the sum of them
    >>> find(algorithm=first,items=[12,25,1,10,34,1])
    (34, 25)
    >>> find(algorithm=first,items={"a":12, "b": 25, "c":1, "d":10, "e":34,"f":1})
    (34, 25)
    >>> find(algorithm=first_sum,items=[12,25,1,10,34,1])
    59
    >>> find(algorithm=second,items=[9,4,123,433,5432,3456,5432,566,4356,7665,645,3345,4443])
    (7665, 5432)
    >>> find(algorithm=second,items={"a":9, "b": 4, "c":123, "d":433, "e":5342,"f":3456,'g':5432,"h":566,"i":4356,"j":7665,'k':645,'l':3345,'m':4443})
    (7665, 5432)
    >>> find(algorithm=second_sum,items={"a":9, "b": 4, "c":123, "d":433, "e":5342,"f":3456,'g':5432,"h":566,"i":4356,"j":7665,'k':645,'l':3345,'m':4443})
    13097
    """
    if isinstance(items, dict):
        item_vals = list(items.values())
        valueof = items.__getitem__
    else:
        item_vals = items
        valueof = lambda item: item
    return algorithm(item_vals, valueof)


def first(item_vals: list, valueof: Callable[[Any], float] = lambda x: x):
    """
    this method compute and return first two different max number in list
    >>> first([8,7,4,15,19,2,4,5,16,19])
    (19, 16)
    >>> first([11,12,12,12,12,12])
    (12, 11)
    >>> first([442.5,443.33,443.36,444])
    (444, 443.36)
    """
    size = len(item_vals)
    sec = -1
    first = -1
    for i in range(size):
        first = max(first,item_vals[i])
    for i in range(size):
        if(item_vals[i] != first):
            sec = max(sec,item_vals[i])
    return first,sec


def first_sum(item_vals: list, valueof: Callable[[Any], float] = lambda x: x):
    """
    this method compute and return sum of first two different max number in list
    >>> first_sum([8,7,4,15,19,2,4,5,16,19])
    35
    >>> first_sum([11,12,12,12,12,12])
    23
    >>> first_sum([442.5,443.33,443.36,444])
    887.36

    """
    a,b = first(item_vals, valueof)
    return a+b


def second(item_vals: list, valueof: Callable[[Any], float] = lambda x: x):
    """
    this method compute and return first two different max number in list
    >>> second([8,7,4,15,19,2,4,5,16,19])
    (19, 16)
    >>> second([11,12,12,12,12,12])
    (12, 11)
    >>> second([442.5,443.33,443.36,444])
    (444, 443.36)
    """
    first = -1
    sec = "no second number"
    for i in range(len(item_vals)):
        if (item_vals[i] > first):
            sec = first
            first = item_vals[i]
        elif (item_vals[i] > sec and item_vals[i] != first):
            sec = item_vals[i]
    return first, sec


def second_sum(item_names: list, valueof: Callable[[Any], float] = lambda x: x):
    """
    this method compute and return sum of first two different max number in list
    >>> second_sum([8,7,4,15,19,2,4,5,16,19])
    35
    >>> second_sum([11,12,12,12,12,12])
    23
    >>> second_sum([442.5,443.33,443.36,444])
    887.36
    """
    a,b = second(item_names,valueof)
    return a+b


if __name__ == "__main__":
    import doctest

    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))




