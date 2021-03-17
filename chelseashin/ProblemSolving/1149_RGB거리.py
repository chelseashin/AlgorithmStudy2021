# 19:00 DP로 다시 풀기
# 19:30 finish
# 미리 dp 테이블  손으로 그려보고 그대로 코드로 옮김

from sys import stdin
input = stdin.readline

# main
N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(3):
        dp[i][j] = dp[i][j] + min(dp[i-1][:j] + dp[i-1][j+1:])

print(min(dp[N-1]))

# 10
# 711 572 325
# 209 187 673
# 512 930 898
# 759 85 260
# 136 226 532
# 201 3 959
# 132 607 359
# 601 775 848
# 462 776 920
# 74 807 671
# 정답 : 3058