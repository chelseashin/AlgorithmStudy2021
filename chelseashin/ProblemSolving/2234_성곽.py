# 14:00 start
# 14:55 방 갯수와 가장 넓은 방 넓이까지 구함.
# "하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기"를 구해보자..
# 15:40 한 번에 pass
# 1h 40m 소요

from sys import stdin
input = stdin.readline
from collections import deque

# 남 동 북 서
dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)
rev = (2, 3, 0, 1)  # 방향 전환 - 북 서 남 동

def makeBinInfo():
    binInfo = dict()
    for num in range(16):
        binNum = bin(num)[2:]       # 10진수 => 이진수(문자열) 변환
        binInfo[num] = list(map(int, "0"*(4-len(binNum))+binNum))
    return binInfo

# bfs로 visited에 방 번호 표시
def checkRooms(sr, sc, cnt):
    area = 1
    visited[sr][sc] = cnt
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        num = A[r][c]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 격자 밖 or 이미 방문
            if not (0 <= nr < R and 0 <= nc < C) or visited[nr][nc]:
                continue
            # 현 위치에서 나갈 수 있는 방향이고, 이동할 위치에서 현 위치에서 들어오는 곳이 뚫려있다면
            if not binInfo[num][d] and not binInfo[A[nr][nc]][rev[d]]:
                area += 1
                visited[nr][nc] = cnt
                Q.append((nr, nc))
    return area

# bfs로 경계선 방들 검사
def checkBoundary(sr, sc):
    boundarySet = set()     # 경계선 번호 검사 중복으로 하지 않기 위함
    num = visited[sr][sc]   # 현재 방 번호
    boundaryArea = 0        # 갱신용 넓이
    check[sr][sc] = num     # 방문 표시
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if check[nr][nc] == num:    # 이미 방문했으면 
                continue
            if visited[nr][nc] == num:  # 나와 같은 방이면 그냥 방문 표시
                check[nr][nc] = num
                Q.append((nr, nc))
            else:   # 나와 다른 방이면 검사
                boundaryNum = visited[nr][nc]       # 경계에 있는 방 번호
                if boundaryNum not in boundarySet:  # 첫 검사인 경우
                    boundarySet.add(boundaryNum)
                    # 경계에 있는 방 크기를 갱신할 수 있다면 
                    if boundaryArea < roomInfo[boundaryNum]:
                        boundaryArea = roomInfo[boundaryNum]
    return roomInfo[num] + boundaryArea     # 원래 방 크기와 합친 크기

# main
C, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
binInfo = makeBinInfo()     # 0~16 숫자 이진수 표현 정보 딕셔너리
# print("binInfo", binInfo)

roomCnt, maxArea = 1, 0     # 방의 갯수, 가장 큰 방 구하기
roomInfo = dict()           # 방별 넓이 정보(경계 방들 크기와 합쳐 확인하기 위함)
visited = [[0] * C for _ in range(R)]
for sr in range(R):
    for sc in range(C):
        if not visited[sr][sc]:
            # 연결된 방 방문 표시, 방의 넓이 리턴
            area = checkRooms(sr, sc, roomCnt)
            maxArea = max(maxArea, area)
            roomInfo[roomCnt] = area
            roomCnt += 1
# print("========== 현재 방 상태 ============= roomInfo >>", roomInfo)
# for row in visited:
#     print(row)
# print()

realMaxArea = 0     # 벽 뚫어 합쳤을 때의 최대 크기
check = [[0] * C for _ in range(R)]
for sr in range(R):
    for sc in range(C):
        if not check[sr][sc]:   # 첫 확인
            area = checkBoundary(sr, sc)   # bfs로 경계선 방과 합한 방 비교
            realMaxArea = max(realMaxArea, area)    # 최댓값 갱신

print(roomCnt-1)    # roomCnt 1부터 시작했기 때문에 -1 해줌
print(maxArea)            
print(realMaxArea)