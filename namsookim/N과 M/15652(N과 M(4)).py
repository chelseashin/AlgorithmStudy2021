# https://www.acmicpc.net/problem/15652
# 10분 소요
"""
1. 비내림차순으로 진행하는 수열이다. 현재의 숫자보다 항상 같거나 커야한다.

2. 이러한 조건 때문에 마지막 숫자를 기록할 수 있게 함수의 인자로 주었고, 반복문을 돌 때 이 문자보다
   같거나 클 수 있도록 반복문을 구현했다.

"""
N,M = map(int,input().split())

array = [0] * M
def solve(k,l): # 마지막 숫자
    if k == M:
        for x in array:
            print(x,end=' ')
        print()
        return

    for i in range(l,N+1):
        array[k] = i
        k+=1
        solve(k,i)
        k-=1

solve(0,1)