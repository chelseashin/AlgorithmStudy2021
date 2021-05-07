from sys import stdin
input = stdin.readline
# from itertools import permutations

n = int(input())
k = int(input())
cards = [input().strip() for _ in range(n)]
S = set()

# 방법 1
# for perm in permutations(cards, k):
    # S.add(''.join(perm))

# 방법 2
def perm(depth, temp):
    global check
    if depth == k:
        S.add(''.join(temp))
        return
    for i in range(n):
        if check[i]:
            continue
        check[i] = 1
        perm(depth+1, temp+cards[i])
        check[i] = 0

check = [0]*n
perm(0, "")
print(len(S))