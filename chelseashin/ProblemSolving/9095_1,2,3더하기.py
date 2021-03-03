# 11:00 start
# 11:32 pass
# 처음에 combination으로 풀려다가 숫자를 자세히 보니 규칙성 발견
# 4번째 수 이후로 이전의 세 수의 합의 값을 가짐. n은 10까지 수를 가지므로 미리 리스트로 만들어놓고
# 인덱스에 해당하는 값을 찾아 간단하게 풀 수 있는 문제.

import sys
input = sys.stdin.readline

dp = [1, 2, 4]
for i in range(3, 12):
    dp.append(dp[i-3]+dp[i-2]+dp[i-1])
# print(dp)

n = int(input())
for _ in range(n):
    print(dp[int(input())-1])