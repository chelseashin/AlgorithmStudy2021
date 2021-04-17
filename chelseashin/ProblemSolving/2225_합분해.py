# https://www.acmicpc.net/problem/2225
# 참고 링크 : https://suri78.tistory.com/105

from sys import stdin
input = stdin.readline

N, K = map(int, input().split())

dp = [[1] * (N+1) for _ in range(K)]

for r in range(1, K):
    for c in range(1, N+1):
        dp[r][c] = dp[r-1][c] + dp[r][c-1]

# for row in dp:
    # print(row)

print(dp[K-1][N] % 1000000000)