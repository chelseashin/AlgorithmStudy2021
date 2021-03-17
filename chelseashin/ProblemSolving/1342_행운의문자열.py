# 19:40 start
# 19:55 finish
# 문자열을 순열로 처리해서 완탐.. 가지치기 없이 너무 오래 걸림


from sys import stdin
input = stdin.readline

def dfs(depth, temp):

    if depth == N:
        candidates.add(temp)
        return
    for i in range(N):
        if check[i]:
            continue
        if temp and S[i] == temp[-1]:
            continue
        check[i] = 1
        dfs(depth+1, temp + S[i])
        check[i] = 0


S = input().strip()
N = len(S)
candidates = set()
check = [0] * N
dfs(0, "")
print(len(candidates))