# https://www.acmicpc.net/problem/15649

"""
1. array를 전역변수로 받아서 매번 현재까지의 문자열을 들고 다닐 필요가 없다.
2. array값은 갱신할 필요가 없는데 어차피 새로운 값으로 덮이기 때문이다.
3. 훨씬 간결하게 해결 가능하다
"""
N , M = map(int,input().split())

isUsed = [False]*(N+1)
array = [0] * M
def solve(k):
    if k == M:
        for x in array:
            print(x,end=' ')
        print()
        return

    for i in range(1,N+1):
        if isUsed[i] != True:
            array[k] = i
            isUsed[i] = True
            solve(k+1)
            isUsed[i] = False

solve(0)
