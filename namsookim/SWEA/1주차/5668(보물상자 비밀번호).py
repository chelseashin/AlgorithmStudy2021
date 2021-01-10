# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

# 01:03 시작
# 02:13 끝
# 1시간 10분 소요

"""
문제
1. 각 변에 16진수가 상자가 있음
2. 이를 각 변에 있는 숫자만큼 회전시켜서 나온 결과를 중복을 제거하여 내림차순으로 정렬한 뒤, K번째로 큰수를 찾는 문제.

시행착오
1. 각 변에 있는 숫자만큼 회전시켜야 하는데 4로 회전시켰음(사각형의 회전으로 실수)
2. int(x,16) => x의 문자열 값을 16진수로 변환, hex(), oct(), bin() => 값을 16진수, 8진수, 2진수로 변환

풀이
1. deque의 rotate를 사용해서 N//4 만큼 회전시킴
2. 나온 값을 집합에 포함시킨 뒤 리스트로 변환 후 내림차순 정렬.
3. k번째 값을 출력

"""
import sys
from collections import deque


def solve():
    global array
    number_set = set([])

    array = deque(array)
    for _ in range(N//4): # 이부분 4로 해서 틀렸음. 4가지 방향으로 돌리는 것이 아니라 한 변에는 1개의 값이 있을 수도 있고 3개의 값이 있을수도 있다. 이를 고려해야함.
        array.rotate(1)

        start = 0
        temp = N // 4
        end = N // 4
        #print(array)
        for _ in range(4):
            s = list(array)[start:end]
            #print(s)
            start = end
            end = end + temp
            if len(s) != 0:
                val = ''.join(map(str,s))
                number_set.add(int(val,16))

            #print(s)

    number_list=list(number_set)
    number_list.sort(reverse= True)


    return number_list[K-1]

sys.stdin = open("5668.txt")
input = sys.stdin.readline

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N,K = map(int,input().split())
    array = list(input().rstrip())
    print("#{0} {1}".format(test_case,solve()))

