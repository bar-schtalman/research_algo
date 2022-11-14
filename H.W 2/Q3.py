class List(list):
    def __init__(self, lst):
        super().__init__(lst)
    def __getitem__(self, index : list):
        if isinstance(index,int):
            return super().__getitem__(index)
        else:
            ans = self
            for i,item in enumerate(index):
                #ans.append(super().__getitem__(index[i]))
                ans = self[item]
            return ans










lst2 = List[[[1,2,3,33],[4,5,6,66]],
    [[7,8,9,99],[10,11,12,122]],
    [[13,14,15,155],[16,17,18,188]]]
print(lst2)
l = [1,2,3]
ll = [4,5,6]
for i in ll:
    l.append(i)
print(l)
#print(lst2[0,1,3])
