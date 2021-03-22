# 참고 : https://pacific-ocean.tistory.com/152
# https://claude-u.tistory.com/204
# dp[i]의 최댓값을 구하는 것은 세 가지 방법에 의해 결정된다.
# 1) OXOO: 연속 두 개
# 2) OXO: 하나 띄고 한 개
# 3) X: i 번째를 마시지 않는 경우

from sys import stdin
input = stdin.readline

n = int(input())
a = [0] + [int(input()) for _ in range(n)]
dp = [0, a[1]]
if n > 1:
    dp.append(a[1] + a[2])
for i in range(3, n+1):
    dp.append(max(dp[i-1], dp[i-3]+a[i-1]+a[i], dp[i-2]+a[i]))
# print(n, a, dp)
print(dp[n])

# 위와 같은 방법
# wine = [0] + [int(input()) for _ in range(n)]
# dp = [0] * (n+1)
# dp[1] = wine[1]
# if n > 1:
#     dp[2] = wine[1] + wine[2]
# for i in range(3, n+1):
#     dp[i] = max(dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i], dp[i-1])
#
# print(dp[n])