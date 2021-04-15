# 21:48 start
# 22:30 1번에 pass 시간 1위 달성!
# 42분 소요
# 원래 dfs 순열로는 39916800개가 나오는데, 
# Backtracking으로 구하니 1824개로 확연히 줄음

from sys import stdin
input = stdin.readline

# 나의 풀이(176ms/123752kb)
def perm(player, score):
    global max_score
    if player == 11:
        # print(order, score)
        max_score = max(max_score, score)   # 최대 점수 갱신
        return
    for i in range(11):
        if visited[i] or not stats[player][i]:   # 가지치기. 해당 포지션에서 적합하지 않으면 넘기기 
            continue
        visited[i] = 1      # 방문 가능
        order[player] = i
        perm(player+1, score+stats[player][i])
        order[player] = -1
        visited[i] = 0

# main
T = int(input())
for _ in range(T):
    stats = [list(map(int, input().split())) for _ in range(11)]
    max_score = 0
    order = [0] * 11
    visited = [0] * 11
    perm(0, 0)
    print(max_score)

# order 배열 사용 안 한 풀이(180ms/124544kb)
# def perm(depth, score):
#     global max_score
#     if depth == 11:
#         # print(visited, score)
#         max_score = max(max_score, score)
#         return
#     for i in range(11):
#         if visited[i] > -1 or not P[depth][i]:   # 가지치기
#             continue
#         visited[i] = depth
#         perm(depth+1, score+P[depth][i])
#         visited[i] = -1

# # # main
# T = int(input())
# for _ in range(T):
#     P = [list(map(int, input().split())) for _ in range(11)]
#     max_score = 0
#     visited = [-1] * 11
#     perm(0, 0)
#     print(max_score)