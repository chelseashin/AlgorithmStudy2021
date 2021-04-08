# 22:00 start
# 11% 지옥에 빠졌다..
# 24:48 pass.......
# 장장 2시간 48분 소요..

from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def checkLand(checkPoints):
    check = [[0] * C for _ in range(R)]
    # 땅에 붙어 있는 미네랄 check 배열에 표시
    for lc in range(C):
        if cave[R-1][lc] == "x" and not check[R-1][lc]:     # 미네랄이면서 첫 방문이면
            check[R-1][lc] = 1
            Q = deque([(R-1, lc)])
            while Q:
                r, c = Q.popleft()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if not (0 <= nr < R and 0 <= nc < C):       # 격자 밖이면
                        continue
                    if cave[nr][nc] == "x" and not check[nr][nc]:   # 미네랄이거나 방문한 적 없으면
                        check[nr][nc] = 1
                        Q.append((nr, nc))

    minerals = []    # 공중에 떠있는 미네랄 리스트
    fallLst = []     # 떨어질 수 있는 클러스터의 아랫부분만 저장
    cr, cc = checkPoints[0]     # 깨진 부분의 4방향 확인
    for d in range(4):
        r = cr + dr[d]
        c = cc + dc[d]
        if not (0 <= r < R and 0 <= c < C):       # 격자 밖이면
            continue
        # 미네랄인데 땅에 붙어 있지 않다면(check 배열에서 0으로 표시되어 있다면)
        if cave[r][c] == "x" and not check[r][c]:
            Q = deque([(r, c)])
            check[r][c] = 2
            minerals.append((r, c))
            cave[r][c] = "."        # 동굴에서 공중에 떠 있는 미네랄 제거
            while Q:
                r, c = Q.popleft()
                if cave[r+1][c] == ".":
                    fallLst.append((r, c))
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if not (0 <= nr < R and 0 <= nc < C):
                        continue
                    if cave[nr][nc] == "x" and not check[nr][nc]:
                        check[nr][nc] = 2           # 공중에 떠있는 미네랄 클러스터 표시
                        Q.append((nr, nc))
                        minerals.append((nr, nc))   # 미네랄 위치 리스트에 담기
                        cave[nr][nc] = "."

    if minerals:    # 공중에 떠있는 미네랄이 있다면
        # for chk in check:
        #     print(chk)
        # print()
        # print("FallLIST", fallLst)
        downCnt, flag = 1, 0      # downCnt 크기 1씩 늘려가며
        while True:
            for r, c in fallLst:
                if r+downCnt == R-1:        # 땅을 만나거나
                    flag = 1
                    break
                if cave[r+downCnt+1][c] == 'x' and check[r+downCnt+1][c]:   # 다른 미네랄 만나면
                    flag = 1
                    break
            if flag:    # 그 때가 떨어질 수 있는 최대 downCnt 값
                break
            downCnt += 1
        # print("내릴 칸 갯수 downCnt", downCnt)
        
        for mr, mc in minerals:
            cave[mr+downCnt][mc] = "x"      # 미네랄 떨어진 위치 동굴에 그리기

# main
R, C = map(int, input().split())
cave = [list(input().rstrip()) for _ in range(R)]
N = int(input())
heights = list(map(int, input().split()))

for i in range(N):
    checkPoints = []
    br = R - heights[i]
    if not i % 2:       # 왼쪽에서 깸
        for bc in range(C):
            if cave[br][bc] == "x":
                cave[br][bc] = "."
                checkPoints.append((br, bc))
                break
    else:               # 오른쪽에서 깸
        for bc in range(C-1, -1, -1):
            if cave[br][bc] == "x":
                cave[br][bc] = "."
                checkPoints.append((br, bc))
                break
    checkLand(checkPoints)
    # for row in cave:
    #     print(i, ''.join(row))
    # print()

# 형식에 맞게 출력
for row in cave:
    print(''.join(row))


