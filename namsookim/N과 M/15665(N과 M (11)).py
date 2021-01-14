# https://www.acmicpc.net/problem/15665
"""
1. 중복처리는 isUsed 집합으로 처리
2. check[False]를 안썻다 왜???
   같은 값을 중복해서 출력할 수 있기 때문에
"""
N, M = map(int,input().split())
array  = list(map(int,input().split()))
result = [0]*M
check = [False]*N
isUsed = set([])
array.sort()
def solve(k,num):
    if k==M:
        temp = ''
        for i in range(M):
            temp += str(result[i])

        if temp not in isUsed:
            isUsed.add(temp)
            for i in range(M):
                print(result[i],end=' ')
            print()
        return

    for i in range(N):
        result[k] = array[i]
        solve(k+1,array[i])

solve(0,0)