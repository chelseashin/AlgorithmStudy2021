# 18m
# 많이 풀어본 문제라 금방 품
# 특별한 알고리즘 X, 리스트 슬라이싱을 이용해 회전, 값에 16진수 처리를 하면서 중복없이 리스트에 담아줌

import sys
sys.stdin = open("5658_input.txt")

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    A = list(input())
    turn = N//4
    result = 0
    L = []
    for _ in range(turn):
        for i in range(0, N, turn):
            temp = int(''.join(A[i:i+turn]), 16)
            if temp not in L:
                L.append(temp)
        A = [A[-1]] + A[:-1]
    print("#{} {}".format(tc+1, sorted(L, reverse=True)[K-1]))