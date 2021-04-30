# 2시간 40분 시도했으나 실패..
# 내일 다시 ㄱㄱ..

from sys import stdin
input = stdin.readline

# 상 좌 하 우
dr = (-1, 0, 0, 1)
dc = (0, -1, 1, 0)

# 인접한 학생 값이 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000
def satisfied():
    result = 0
    for r in range(N):
        for c in range(N):
            if not A[r][c]:
                continue
            cnt = 0
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if A[nr][nc] in likeInfo[A[r][c]]:
                    cnt += 1
            if cnt:
                result += 10 ** (cnt-1)
    return result

def drawIdx(idx):
    # print("======================", idx, "=======================")
    maxLike, maxEmpty = -1, -1
    maxR, maxC = -1, -1
    for r in range(N):
        for c in range(N):
            if A[r][c]:
                continue
            likeCnt, emptyCnt = 0, 0
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                # 1. 좋아하는 사람 인접한 칸에 있는 갯수
                if A[nr][nc] in likeInfo[idx]:
                    likeCnt += 1      
                # 2. 두 번째는 인접한 칸 중 빈 칸 갯수
                if not A[nr][nc]:
                    emptyCnt += 1
            # maxLike가 갱신됐거나
            if maxLike < likeCnt or (maxLike == likeCnt and maxEmpty < emptyCnt):
                maxR, maxC = r, c
                maxLike, maxEmpty = likeCnt, emptyCnt

# main
N = int(input())
A = [[0] * N for _ in range(N)]
likeInfo = dict()
for _ in range(N**2):
    info = list(map(int, input().split()))
    likeInfo[info[0]] = set(info[1:])
# print("likeInfo", likeInfo)
for idx in likeInfo.keys():
    drawIdx(idx)
    # for a in A:
    #     print(a)
    # print()

print(satisfied())      # 만족도 조사
