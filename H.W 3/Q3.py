import sys
import math

'https://www.codingame.com/training/hard/super-computer/solution?id=27402888'
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def sortSec(val):
    return val[1]


tup_list = []
n = int(input())
for i in range(n):
    j, d = [int(j) for j in input().split()]
    tup_list.append((j, j + d - 1))
tup_list.sort(key=sortSec)
sum, end = 1, tup_list[0][1]
size = len(tup_list)
for i in range(size):
    start = tup_list[i][0]
    if (end < start):
        sum, end = sum + 1, tup_list[i][1]

    # Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(sum)

