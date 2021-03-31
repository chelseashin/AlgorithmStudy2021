# 16:00 start
# 16:12 finish
# 12m 소요

import sys
input = sys.stdin.readline

def comb(depth, pos):
    if depth == 6:
        print(*order)
        return
    for i in range(pos, k):
        order.append(lottos[i])
        comb(depth+1, i+1)
        order.pop()

while True:
    lottos = list(map(int, input().split()))
    k = lottos.pop(0)
    if not lottos:
        break
    order = []
    comb(0, 0)
    print()