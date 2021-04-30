# 다른 사람 풀이 - 시간: 188ms로 시간 1위 달성^_^
# 는 사실 다른 분 풀이 참고,, 링크는 https://hillier.tistory.com/76
# 확실히 heap 사용하는 것보다 빠르다. 
# O(N^2)으로 바로 학생 놓을 위치 찾기

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
            # 핵심!
            # maxLike를 갱신할 수 있거나 (maxLike와 likeCnt가 같고 maxEmpty를 갱신할 수 있다면)
            if maxLike < likeCnt or (maxLike == likeCnt and maxEmpty < emptyCnt):
                maxR, maxC = r, c                       # 위치 갱신
                maxLike, maxEmpty = likeCnt, emptyCnt   # maxLike, maxEmpty 갱신

    A[maxR][maxC] = idx     # 자리 배치

# main
N = int(input())
A = [[0] * N for _ in range(N)]
likeInfo = dict()          # 학생 번호별 좋아하는 학생 정보 {학생 번호 : 좋아하는 학생 Set}
for _ in range(N**2):
    info = list(map(int, input().split()))
    likeInfo[info[0]] = set(info[1:])

for idx in likeInfo.keys():
    drawIdx(idx)

print(satisfied())      # 만족도 조사