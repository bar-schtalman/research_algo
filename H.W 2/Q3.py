class List(list):
    """
    this class made by inheritance from list to implement multidimensional operator for get items from multidimensional list
    by overload the "getitem" method of class "list" and therfore by creating List you can now use the new operator!
    >>> mylist[1,0]
    [7, 8, 9, 99]
    >>> mylist[0]
    [[1, 2, 3, 33], [4, 5, 6, 66]]
    >>> mylist[0,0,3]
    33
    >>> mylist[1,1,2]
    12
    >>> mylist2[1,1]
    [True, False, False, False, True]
    >>> mylist2[1,1,1]
    False
    >>> mylist2[2,1]
    [1, True, 'abc', 13454]
    >>> mylist2[2]
    [['alef', 'bet', 'gimel', 'daled'], [1, True, 'abc', 13454]]

    """
    def __init__(self,lst):
        super().__init__(lst)

    def __getitem__(self, index):
        if isinstance(index,int):
            return super().__getitem__(index)
        else:
            ans = List(self)
            for item in index:
                ans = ans[item]
            return ans


mylist = List([[[1,2,3,33],[4,5,6,66]],[[7,8,9,99],[10,11,12,122]],[[13,14,15,155],[16,17,18,288]],])
mylist2 = List([[['a','b','c','abc'],['d','e','f','def']],[[5,2,4,6],[True,False,False,False,True],[5.12,3.14]],[['alef','bet','gimel','daled'],[1,True,'abc',13454]],[[5,2,3,7,4,5],[11,22,33]]])
if __name__ == '__main__':
    import doctest

    doctest.testmod()
