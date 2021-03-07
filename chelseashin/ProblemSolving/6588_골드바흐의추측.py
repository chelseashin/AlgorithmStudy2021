# 13:30 start
# 14:03 pass
# 에라토스테네스 체 이용해서 미리 소수 테이블을 만들어 놓는다.
# 가장 작은 소수인 2부터 두 수가 모두 소수인 가장 빠른 경우 정답 리턴


import sys
input = sys.stdin.readline

a = [0, 0] + [1]*(1000001-1)
for i in range(2, 1001):
    for j in range(2*i, 1000001+1, i):
        a[j] = 0

def solve(n):
    for num in range(2, n):
        if a[num] and a[n-num]:
            print(n, "=", num, "+", n-num)
            return
    print("Goldbach's conjecture is wrong.")
    return

while True:
    n = int(input())
    if not n:
        break
    solve(n)