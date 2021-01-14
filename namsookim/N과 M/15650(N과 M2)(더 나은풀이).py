"""
1. 오름차순으로 나타내기 위해 이전값의 정보를 활용해야 한다. 그래서 인자값으로 이전 값 정보를 받음
2. 이전 값으로 받은 정보부터 N까지 반복문 ㄱㄱ 하면 계속 자신보다 큰 수만 선택한다.
3. 리턴할 때 방문했던곳 false 처리 필수
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

            check[i] = True
            solve(k+1,i+1)
            check[i] = False

solve(0,1)

