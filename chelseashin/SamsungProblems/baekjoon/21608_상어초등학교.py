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
            cnt = 0
            idx = A[r][c]
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if A[nr][nc] in likeInfo[idx]:
                    cnt += 1
            print(idx, "번 학생", cnt)
            result += 10 ** (cnt-1)
    return result

# main
N = int(input())
A = [[0] * N for _ in range(N)]
likeInfo = dict()
for _ in range(N**2):
    info = list(map(int, input().split()))
    print(info)
    likeInfo[info[0]] = set(info[1:])

print(likeInfo)
print(satisfied())      # 만족도 조사