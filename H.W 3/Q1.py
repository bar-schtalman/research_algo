from itertools import *


class bounded_subsets:

    def __init__(self,first,end,lst = list,bound = int):
        self.state = first
        self.end = end
        self.bound = bound


    def __iter__(self):
        return self

    def __next__(self):
        if self.state == self.end:
            raise StopIteration

        res = self.state

        self.state += self.step
        return res


