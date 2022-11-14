import sys
import math
from collections import deque
from queue import Queue
p1lst = []
p2lst = []
def whatNum(num : str):
    if num[0] == 'J':
        return 11
    elif num[0] =='Q':
        return 12
    elif num[0] == 'K':
        return 13
    elif num[0] == 'A':
        return 14
    elif num[0] == '1' and num[1] == '0':
        return 10
    else:
        return int(num[0])
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
round = 0
p1cards = []
p2cards = []
n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    p1cards.append(whatNum(cardp_1))

m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    p2cards.append(whatNum(cardp_2))

while (len(p1cards) > 0 and len(p2cards) > 0):
    p1 = p1cards.pop(0)
    n -= 1
    p2 = p2cards.pop(0)
    m -= 1
    if p1 > p2:
        for card in p1lst:
            p1cards.append(card)
        p1cards.append(p1)
        for cards in p2lst:
            p1cards.append(cards)
        p1cards.append(p2)
        p1lst.clear()
        p2lst.clear()
        n += 2
        round += 1
    elif p1 < p2:
        for card in p1lst:
            p2cards.append(card)
        p2cards.append(p1)
        for cards in p2lst:
            p2cards.append(cards)
        p2cards.append(p2)
        p1lst.clear()
        p2lst.clear()
        m += 2
        round += 1
    elif p1 == p2 :
        #print(len(p1cards), len(p2cards))
            if len(p1cards) < 3 or len(p2cards) <3 :
                p2cards.clear()
                p1cards.clear()
                break
            p1lst.append(p1)
            p1lst.append(p1cards.pop(0))
            p1lst.append(p1cards.pop(0))
            p1lst.append(p1cards.pop(0))
            p2lst.append(p2)
            p2lst.append(p2cards.pop(0))
            p2lst.append(p2cards.pop(0))
            p2lst.append(p2cards.pop(0))
if (len(p1cards) == len(p2cards)):
    print("PAT")
elif p1cards:
    print(1,round)
elif p2cards:
    print(2,round)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

#print("PAT")
