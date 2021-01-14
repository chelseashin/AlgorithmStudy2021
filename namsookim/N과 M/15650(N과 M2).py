# https://www.acmicpc.net/problem/15650

"""
1. 고른 수열은 항상 오름차순이여야 된다는 조건이 있다. 그렇기 때문에 어떤 값을 정했을 때 그 값 기준으로 내림차순으로 해당하는 값들을 모두 방문처리해준다.
   이를 통해, 오름차순만 array에 저장될 수 있다.
2. 하지만 N 값이 커질수록 너무 비효율적인 코드. 굳이 내림차순 2번씩이나??
3. 더 나은풀이 참고 ㄱ
"""

N,M = map(int,input().split())
array = [0] * M
check = [False] * (N+1)
def solve(k,num):
    if k == M:
        for x in array:
            print(x,end= ' ')
        print()
        return
    for i in range(num,N+1):
        if check[i] == False:
            array[k] = i
            for j in range(i,-1,-1):
                check[j] = True
            solve(k+1,num+1)
            for j in range(i, -1, -1):
                check[j] = False
solve(0,1)