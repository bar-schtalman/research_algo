import itertools
import time


def bounded_subsets(set:list,num):
    """
    this generator calculate all combinatain for subset from size 0 to size num
    >>> for s in bounded_subsets([1,2,3], 4): print(s, end = '')
    [][1][2][3][1, 2][1, 3]
    >>> for s in bounded_subsets([1,2,3,4,5,6],7): print(s, end = '')
    [][1][2][3][4][5][6][1, 2][1, 3][1, 4][1, 5][1, 6][2, 3][2, 4][2, 5][1, 2, 3][1, 2, 4]
    >>> for s in bounded_subsets([],2): print(s, end = '')
    []
    >>> for s in bounded_subsets(range(1,5),9): print(s, end = '')
    [][1][2][3][4][1, 2][1, 3][1, 4][2, 3][2, 4][3, 4][1, 2, 3][1, 2, 4][1, 3, 4][2, 3, 4]
    >>> for s in zip(range(5), bounded_subsets(range(100), 1000000000000)): print(s,end = '')
    (0, [])(1, [0])(2, [1])(3, [2])(4, [3])
    >>> for s in bounded_subsets(range(50,150), 103): print(s, end = '')
    [][50][51][52][53][54][55][56][57][58][59][60][61][62][63][64][65][66][67][68][69][70][71][72][73][74][75][76][77][78][79][80][81][82][83][84][85][86][87][88][89][90][91][92][93][94][95][96][97][98][99][100][101][102][103][50, 51][50, 52][50, 53]
    """
    if not isinstance(set,range):
        set.sort()
    yield []
    size = len(set)
    for i in range(1,size):
        for combo in (itertools.combinations(set, i)):
            combo_sum = sum(combo)
            if combo_sum > num:
                break
            else:
                yield list(combo)


if __name__ == "__main__":
    import doctest

    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))