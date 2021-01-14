# https://www.acmicpc.net/problem/15655

"""
1. 오름차순으로 표현해야함. 정렬 후 현재 몇 번째 인덱스를 조회하는 함수인지 인자를 통해 기록하면 오름차순 출력 가능

2. k의 값은 현재 몇개의 값이 포함되었는지, num의 값은 바로 전 인덱스는 몇번째 인덱스인지 기록

3. 멋지게 해결 가능
"""
N, M = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
result = [0] * M
check = [False]*N

def solve(k,num):
    if k == M:
        for res in result:
            print(res,end=' ')
        print()
        return

    for i in range(N):
        if num>i:
            continue
        if check[i] != True:
            result[k] = array[i]
            check[i] = True
            solve(k+1,i)
            check[i] = False

solve(0,0)
