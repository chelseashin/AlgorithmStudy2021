# https://www.acmicpc.net/problem/15663

"""
1. 중복되는 수열을 여러번 출력하면 안된다는 조건이 있다. 지금까지 어떤 수열을 출력했는지 기록하고,
   지금까지 사용한 기록이 없으면 출력한 뒤에 지금까지 사용한 기록에 현재 출력한 것을 저장한다.

2. 이를 위해 집합 자료형을 사용. set([]) 로 선언하였고 .add 연산자로 집합 자료형에 값을 추가할 수 있다.

"""
N,M = map(int,input().split())
array = list(map(int,input().split()))
array.sort()

result = [0] * M
check = [False] * N
pos_result = set([])     # set()과 동일

def solve(k):
    #global pos_value
    if k == M:
        temp = []
        for i in range(M):
            temp.append(result[i])
        temp = tuple(temp)

        if temp not in pos_result:
            pos_result.add(temp)
            for te in temp:
                print(te,end= ' ')
            print()

        return

    for i in range(len(array)):
        if check[i] != True:
            check[i] = True
            result[k] = array[i]
            solve(k+1)
            check[i] = False

solve(0)