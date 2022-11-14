class List(list):
    def __init__(self,lst):
        super().__init__(lst)

    def __getitem__(self, index):
        if isinstance(index,int):
            return super(List, self).__getitem__(index)
        else:
            ans = list(self)
            for item in index:
                ans = ans[item]
            return ans




mylist = List([[[1,2,3,33],[4,5,6,66]],[[7,8,9,99],[10,11,12,122]],[[13,14,15,155],[16,17,18,288]],])
print(mylist[0,1,3])
