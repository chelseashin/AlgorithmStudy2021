# 9:50 start
# 10:40 tc 다 맞으나 시간 초과..
# 정렬을 나무 심을 때마다 해줘서 시간초과 => 봄에만 나무 있는 곳에 정렬해줌
# 10:43 pass
# 53분 소요
# 특별한 알고리즘 구현 X. 문제 정확하게 이해하는 것이 중요했음.

import sys
input = sys.stdin.readline

# 8방향
dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)

# 봄
def springandsummer():
    for r in range(N):
        for c in range(N):
            if A[r][c]:         # 나무 있는 곳이면
                A[r][c].sort()  # 나이 순으로 정렬
                dead = 0
                trees = len(A[r][c])
                for i in range(trees):
                    if A[r][c][i] <= raw[r][c]:     # 나이만큼 양분 있으면
                        raw[r][c] -= A[r][c][i]     # 양분 먹고
                        A[r][c][i] += 1             # 나이 1 증가
                    else:
                        for j in range(trees, i, -1):       # 뒤에서부터 빼면서
                            dead += A[r][c].pop() // 2      # 죽은 나무의 나이//2 만큼 양분 추가
                        break
                # 여름
                if dead:                    # 죽은 나무가 있다면
                    raw[r][c] += dead       # 나무 있던 칸에 양분으로 추가
# 가을
def autumn():
    for r in range(N):
        for c in range(N):
            if A[r][c]:
                for age in A[r][c]:
                    if not age % 5:         # 나이 5의 배수인 나무
                        for d in range(8):
                            nr = r + dr[d]
                            nc = c + dc[d]
                            if 0 <= nr < N and 0 <= nc < N:
                                A[nr][nc].append(1)     # 나이 1 나무 심기
# 겨울
def winter():
    for r in range(N):
        for c in range(N):
            raw[r][c] += food[r][c]     # 땅에 양분 추가

# main
N, M, K = map(int, input().split())
food = [list(map(int, input().split())) for _ in range(N)]      # 겨울에 추가할 양분
raw = [[5] * N for _ in range(N)]       # 현재 양분의 상태
A = [[[] for _ in range(N)] for _ in range(N)]      # 현재 땅의 상태

# 초기 나무 정보
for _ in range(M):
    x, y, z = map(int, input().split())     # 나무의 위치, 나이
    A[x-1][y-1].append(z)

# K 년동안 나무 재테크
for _ in range(K):
    springandsummer()   # 봄 & 여름
    if not A:           # 나무 없으면 종료
        print(0)
        exit()
    autumn()            # 가을
    winter()            # 겨울

result = 0              # 살아남은 나무의 수
for i in range(N):
    for j in range(N):
        result += len(A[i][j])
print(result)