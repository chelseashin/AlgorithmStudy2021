# 16:25 start
# 16:45 finish
# 20m 소요
# 47%에서 시간초과 실패 >> DP로 접근하바

from sys import stdin
input = stdin.readline

def dfs(depth, temp):
    global MIN
    if temp > MIN:      # 가지치기
        return
    if depth == N:
        # for c in check:
        #     print(c)
        # print(temp)
        MIN = min(MIN, temp)
        return
    for i in range(3):
        if check[depth-1][i]:
            continue
        check[depth][i] = 1
        dfs(depth+1, temp + A[depth][i])
        check[depth][i] = 0

# main
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
check = [[0] * 3 for _ in range(N)]
MIN = float('inf')
for i in range(3):
    check[0][i] = 1
    dfs(1, A[0][i])
    check[0][i] = 0
print(MIN)