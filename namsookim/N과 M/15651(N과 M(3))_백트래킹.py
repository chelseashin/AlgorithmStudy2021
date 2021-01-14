# https://www.acmicpc.net/problem/15649

"""
1. 중복순열로도 풀리고 백트래킹으로도 풀리는 문제  . N,M 의 개수가 적어서 풀림
2. 아이디어는 순서대로 골라본 뒤에 총 문자열의 개수가 M과 동일할 때, 출력하고 리턴한다.
    그 후 함수를 빠져나왔으니 현재 문자열 개수를 줄여준다.

"""
import sys
input = sys.stdin.readline
N , M = map(int,input().split())
array = [i for i in range(1,N+1)]

def solve(k,s):
    if k == M:
        for x in s:
            print(x,end=' ')
        print()
        return
        #return

    for i in range(1,N+1):

        k = k+1
        solve(k,s+str(array[i-1]))
        k = k-1

solve(0,'')
