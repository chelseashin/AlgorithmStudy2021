# 에라 모르겠다.....

from math import comb

def solution(a):
    n = len(a); m = len(a[0])
    dp = [[0] * (n+1) for _ in range(m+1)]
    dp[0][n] = 1
    cols = [r.count(1) for r in zip(*a)]
    combs = {}

    for c in range(1, m+1):
        for r in range(n+1):
            for r2 in range(n+1):
                a1, b1 = n-r2, r2
                a2, b2 = cols[c-1], n-cols[c-1]
                x2 = (r + a2 - b1)
                if x2 % 2:
                    continue
                x = x2 // 2
                y = r - x
                if 0 <= x <= a2 and 0 <= y <= b2:
                    if (a1, x) not in combs:
                        combs[(a1, x)] = comb(a1, x)
                    if (b1, y) not in combs:
                        combs[(b1, y)] = comb(b1, y)

                    i = combs[(a1, x)]
                    j = combs[(b1, y)]
                    dp[c][r] += (dp[c-1][r2] * i * j)
            dp[c][r] %= 10**7 + 19

    return dp[m][n]

print(solution([[0,1,0],[1,1,1],[1,1,0],[0,1,1]]))  # 6
print(solution([[1,0,0],[1,0,0]]))      # 0
print(solution([[1,0,0,1,1],[0,0,0,0,0],[1,1,0,0,0],[0,0,0,0,1]]))  # 72