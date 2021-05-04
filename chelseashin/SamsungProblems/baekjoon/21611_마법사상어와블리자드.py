# 11:50 start
# 13:29 폭발 끝냄
# 14:11 정답 나옴 but 67%에서 IndexError
# 14:20 pass
# 2h 30m 소요

from sys import stdin
input = stdin.readline

# 좌 하 우 상(구슬 이동 시 사용)
dr = (0, 1, 0, -1)
dc = (-1, 0, 1, 0)
rev = (3, 1, 0, 2)  # 구슬 파괴 시 사용

# 구슬 파괴
def destroyMarbles(d, s):
    sr, sc = N//2, N//2
    for dis in range(1, s+1):
        nr = sr + dr[d] * dis
        nc = sc + dc[d] * dis
        A[nr][nc] = 0

# 구슬 변화
def changeMarbles(marbles):
    if not marbles: return []   # 구슬 없으면 빈 리스트 리턴
    newMarbles = []
    check = [0] * len(marbles)
    for i in range(len(marbles)):
        if check[i]: continue
        check[i] = 1            # 첫 방문이면 방문 표시
        temp = [marbles[i]]
        for nx in range(i+1, len(marbles)):
            if marbles[i] == marbles[nx]:
                check[nx] = 1
                temp.append(marbles[nx])
            else: break
        newMarbles.extend([len(temp), temp[0]])     # 연속된 구슬 갯수, 구슬 번호
    return newMarbles           # 변화한 구슬 리스트 리턴

# 구슬 폭발
def explodeMarbles(marbles):
    global result
    if not marbles: return []
    while True:
        bomb = False
        newMarbles = []
        check = [0] * len(marbles)
        for i in range(len(marbles)):
            if check[i]: continue
            check[i] = 1            # 첫 방문이면 방문 표시
            temp = [marbles[i]]
            for nx in range(i+1, len(marbles)):
                if marbles[i] == marbles[nx]:
                    check[nx] = 1
                    temp.append(marbles[nx])
                else: break
            if len(temp) < 4:
                newMarbles.extend(temp)
            else:
                bomb = True   # 폭발
                result += temp[0] * len(temp)   # (구슬 번호 × 폭발한 구슬의 개수) 더하기
        if bomb:              # 폭발한 적 있으면 갱신
            marbles = newMarbles
        else:
            return newMarbles     # 폭발할 구슬 없으면 while문 나가기

# 구슬 재배치
def drawMarbles(marbles):
    if not marbles: return  # 구슬 없으면 리턴(이 코드 없어서 IndexError 났음..)
    r, c = N//2, N//2       # 시작 위치
    d, dis = 0, 1           # 현재 방향, 이동할 거리
    A[r][c-1] = marbles[0]  # 첫 구슬 그리기
    idx = 1                 # 구슬 인덱스 +1 하며 그려주기
    while True:
        for _ in range(2):
            for _ in range(dis): 
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < N and 0 <= nc < N):
                    return
                if (r, c) != (N//2, N//2):
                    A[nr][nc] = marbles[idx]    # 맵에 구슬 그리기
                    idx += 1
                    if idx == len(marbles):     # 구슬 다 그렸으면 리턴
                        return
                r, c = nr, nc
            d = (d+1) % 4      # 방향 전환
        dis += 1               # 거리 + 1

# 구슬 첫 이동
def moveMarbles():
    r, c = N//2, N//2   # 시작 위치
    d, dis = 0, 1       # 현재 방향, 이동할 거리
    marbles = []
    if A[r][c-1]:
        marbles.append(A[r][c-1])   # 첫 구슬 담기
        A[r][c-1] = 0               # 맵에서 지우기
    while True:
        for _ in range(2):
            for _ in range(dis):
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < N and 0 <= nc < N):
                    return explodeMarbles(marbles)     # 3. 구슬 폭발 => 남은 구슬 리턴
                if (r, c) != (N//2, N//2):
                    if 1 <= A[nr][nc] <= 3:
                        marbles.append(A[nr][nc])       # 구슬 담기
                        A[nr][nc] = 0                   # 맵에서 지우기
                r, c = nr, nc
            d = (d+1) % 4      # 방향 전환
        dis += 1               # 거리 + 1

# main
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

result = 0
for _ in range(M):
    d, s = map(int, input().split())
    destroyMarbles(rev[d-1], s)           # 1. 구슬 파괴
    marbles = moveMarbles()               # 2. 구슬 이동
    marbles = changeMarbles(marbles)      # 4. 구슬 변화
    drawMarbles(marbles)                   # 5. 구슬 재배치
print(result)