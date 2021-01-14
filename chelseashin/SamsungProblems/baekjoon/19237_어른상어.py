import sys
sys.stdin = open("19237_input.txt")
input = sys.stdin.readline

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def solve():
    global shark_cnt
    time = 0
    while True:
        if time > 1000:
            return -1
        # 번호가 낮은 것부터 먼저 상어 새 위치에 등록하기 위해서 정렬
        numbers = sorted(list(shark_info.keys()))
        for num in numbers:
            sr, sc, sd = shark_info[num]
            if not A[sr][sc]:               # 빈 공간이거나
                A[sr][sc] = [num, K]
            elif A[sr][sc][0] == num:       # 자기 냄새가 있던 칸이면
                A[sr][sc] = [num, K]        # 새 위치로 상어 이동, 냄새 뿌리기
            else:   # 이동할 공간 없다면 정보 삭제 == 쫓겨난 것
                del shark_info[num]
                shark_cnt -= 1
        # 상어 이동 - shark_info 에 정보만 업데이트
        numbers = sorted(list(shark_info.keys()))
        for num in numbers:
            sr, sc, sd = shark_info[num]     # 상어의 위치, 방향
            # 우선순위 1 : 이동할 수 있는 빈 칸 있는지 여부
            flag_blank = False
            # 상어별 바라보는 방향의 우선순위 nd
            for nd in priority_dir[num-1][sd-1]:
                nr = sr + dr[nd-1]
                nc = sc + dc[nd-1]
                if not (0 <= nr < N and 0 <= nc < N):   # 격자 밖
                    continue
                if not A[nr][nc]:       # 빈 칸 찾으면
                    flag_blank = True
                    shark_info[num] = [nr, nc, nd]   # 상어 [이동 위치, 방향] 정보 업데이트
                    break
            # 우선순위 2 : 빈 공간 발견하지 못하면 나와 같은 냄새 있는 곳으로
            flag_same = False
            if not flag_blank:
                for nd in priority_dir[num-1][sd-1]:
                    nr = sr + dr[nd-1]
                    nc = sc + dc[nd-1]
                    if not (0 <= nr < N and 0 <= nc < N):
                        continue
                    if A[nr][nc][0] == num:     # 자신과 같은 냄새 찾으면
                        flag_same = True
                        shark_info[num] = [nr, nc, nd]  # 상어 이동
                        break
            else:
                continue
            if not flag_same:           # 같은 냄새도 없으면 정보 삭제
                del shark_info[num]
                shark_cnt -= 1          # 격자 내 갈 곳이 없음 == 쫓겨난 것

        # 상어가 지나간 자리 냄새 1 감소
        # 미리 1 감소시키고 새로 이동할 때 K 만큼의 냄새 생성하는 개념
        for i in range(N):
            for j in range(N):
                if A[i][j]:
                    A[i][j][1] -= 1
                    if A[i][j][1] == 0:     # 냄새 소멸
                        A[i][j] = 0         # 빈 공간으로
        if shark_cnt == 1:      # 1번 상어만 남으면 종료
            return time
        time += 1
        # print(time, "초 후 현재 맵 상황", shark_info)
        # for a in A:
        #     print(a)

# main
N, M, K = map(int, input().split())     # 맵 크기, 상어 수, 냄새 없어지는 시간
A = [list(map(int, input().split())) for _ in range(N)]
current_dir = list(map(int, input().split()))
shark_info = {}  # 현재 맵에 있는 상어 정보 dict로 관리
shark_cnt = 0
for i in range(N):
    for j in range(N):
        if A[i][j]:
            # 상어의 위치(r, c)와 방향정보(d) 저장
            shark_info[A[i][j]] = [i, j, current_dir[A[i][j]-1]]
            A[i][j] = 0
            shark_cnt += 1
# 상어 이동 우선순위 정보 저장
priority_dir = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]
print(solve())