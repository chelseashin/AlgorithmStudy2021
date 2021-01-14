# https://www.acmicpc.net/problem/15654
# 12분 소요
"""
1. 백트래킹으로도 풀 수 있는 문제. 우선 사전 순으로 순서대로 출력하기 위해 sort() 내장함수로 정렬하였다.

2. 함수를 호출할 때 현재 개수가 몇 개인지를 기록하도록 인자를 추가함. 
   만약 방문하지 않았으면 방문표시 해주고 값을 저장후 k값을 1증가시킨 다음 함수를 호출
3. k값이 M값과 같으면 길이가 같은것이니 출력하고 리턴해줌. 리턴한뒤 다시 false 처리하여 미방문 처리  

"""
N,M = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
result = [0]* M
check = [False] * len(array)

def solve(k):

    if k == M:
        for x in result:
            print(x,end=' ')
        print()
        return

    for i in range(len(array)):
        if check[i] == False:
            result[k] = array[i]
            check[i] = True
            solve(k+1)
            check[i] = False

solve(0)

