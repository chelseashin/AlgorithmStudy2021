# https://www.acmicpc.net/problem/15656
"""
1. 방문 체크를 안하고 돌리게 되면 처음값 부터 계속 진행한다. 즉 중복을 허용한 오름차순 형태로 진행

"""

N, M = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
result = [0] * M
check = [False]*N

def solve(k):
    if k == M:
        for res in result:
            print(res,end=' ')
        print()
        return

    for i in range(N):

        result[k] = array[i]
        solve(k+1)


solve(0)
