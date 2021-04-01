# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu
# 참고: https://github.com/chelseashin/My-Algorithm/blob/master/swea/%EB%AA%A8%EC%9D%98SW%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8/2112_%EB%B3%B4%ED%98%B8%ED%95%84%EB%A6%84.py
"""
1. dfs로 풀이하면 된다.
2. 1...K까지 개수를 선택하고 모든 경우의 수를 따져가면서 행을 선택한다.
2. 백트래킹 ㄲ

시행착오
1. 시간초과(결국 해결못했음) = 이 코드는 돌아감
2. 0,1 넣는거를 아예 새로 만들어주는 생각 못했음
"""
import sys
sys.stdin = open('2112(보호 필름).txt')

# 성능 테스트
def test(F):
    global K
    for c in range(W):
        cnt = 1
        temp = F[0][c]
        for r in range(1, D):
            if F[r][c] == temp:
                cnt += 1
            else:
                temp = F[r][c]
                cnt = 1
            if cnt >= K:
                break
        if cnt < K:
            return False
    return True

# 현재 약물 투입 횟수, 시작 행 위치, 최대 투입 횟수
def dfs(depth, pos, K):
    global MIN, flag
    if depth >= MIN or flag:    # 가지치기
        return
    if depth == K:
        if test(film):
            MIN = min(MIN, depth)
            flag = 1
        return
    for i in range(pos, D):     # 약물 투입할 행 선택
        for j in range(2):
            if selected[i]:
                continue
            selected[i] = 1
            film[i] = drug[j]   # 약품 투입
            dfs(depth+1, i+1, K)
            film[i] = raw[i]    # 복원
            selected[i] = 0

# main
T = int(input())
for tc in range(T):
    D, W, K = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(D)]
    MIN = float('inf')

    if test(raw):
        MIN = 0
    else:
        film = [r[:] for r in raw]
        drug = [[0] * W, [1] * W]
        selected = [0] * D
        flag = 0
        for i in range(1, K+1):  # 약물 투여 최대 횟수 K까지 할 수 있음
            dfs(0, 0, i)
            if flag:
                break

    print("#{} {}".format(tc + 1, MIN))