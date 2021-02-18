# 17:00 start
# 시간 의미 X
# DP는 아무리 봐도 진짜 이해가 안 된다..ㅎ 공부하자
# LIS(Longest Increasing Subsequence) : 최장 증가 부분수열

import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]
# print(A)

# 풀이 1
dp = [0] * N
dp[0] = 1
for i in range(1, N):
    temp = []
    for j in range(i):
        if A[i] > A[j]:
            temp.append(dp[j])
    if not temp:
        dp[i] = 1
    else:
        dp[i] = max(temp) + 1
print(dp)
print(N - max(dp))


# 풀이 2
# lis = [A[0]]
# temp = 0
# for n in range(1, N):
#     for idx, val in enumerate(lis):
#         if A[n] > val and A[n] not in lis:
#             temp = A[n]
#         elif A[n] < val and A[n] not in lis:
#             lis[idx] = A[n]
#             temp = 0
#
#     if temp:
#         lis.append(temp)
#     temp = 0
# print(N-len(lis))