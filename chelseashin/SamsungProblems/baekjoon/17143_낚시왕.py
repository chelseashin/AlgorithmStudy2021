# 19:20 start
# 20:00 문제 이해 및 설계 완료, 상어 이동 시작
# 20:45 pass
# 1h 26m 소요
# 특별한 알고리즘 X, Simulation. 문제에서 요구한 대로 구현
# 코딩 전 어떤 자료구조 이용할지 미리 설계한 것이 시간 단축에 도움
# 상어의 [위치, 속도, 방향, 크기] 정보 dictionary 로 관리

import sys
input = sys.stdin.readline

# 상 하 우 좌
dr = (-1, 1, 0, 0)
dc = (0, 0, 1, -1)
rev = (1, 0, 3, 2)

# 상어 이동
def shark_move():
    new = [[0] * C for _ in range(R)]
    for idx in range(1, M+1):                       # 1번부터 M 번까지 상어 탐색
        if idx not in shark_info.keys():            # 이미 없는 상어는 넘기기
            continue
        r, c, speed, d, size = shark_info[idx]      # 현재 상어의 정보
        for _ in range(speed):
            r += dr[d]
            c += dc[d]
            if not (0 <= r < R and 0 <= c < C):     # 격자 밖으로 나가면
                d = rev[d]                          # 방향 바꾸고
                r += dr[d] * 2                      # 2번만큼 더 이동
                c += dc[d] * 2

        if not new[r][c]:     # 해당 위치에 아무도 없다면
            new[r][c] = idx   # 맵에 등록
            shark_info[idx] = [r, c, speed, d, size]   # 바뀐 정보 갱신
            continue

        # 이미 다른 상어가 있다면 크기 비교
        temp = new[r][c]                    # 원래 있던 상어의 번호
        if shark_info[temp][4] < size:      # 현재 상어가 더 크다면
            del shark_info[temp]            # 원래 있던 상어 정보 삭제
            new[r][c] = idx                 # 맵에 현재 상어 등록
            shark_info[idx] = [r, c, speed, d, size]    # 바뀐 정보 갱신
        else:                               # 원래 있던 상어가 더 크다면
            del shark_info[idx]             # 현재 상어 정보 삭제
    return new

# main
R, C, M = map(int, input().split())
if M == 0:      # 상어 0마리이면 0 출력 후 종료
    print(0)
    exit()

A = [[0] * C for _ in range(R)]
shark_info = dict()
for num in range(1, M+1):
    r, c, s, d, z = map(int, input().split())
    A[r-1][c-1] = num
    shark_info[num] = [r-1, c-1, s, d-1, z]   # 상어 정보 : [위치 좌표, 속력, 방향, 크기]

result = 0
for c in range(C):
    for r in range(R):
        if A[r][c]:     # 상어 있으면 잡기
            shark_num = A[r][c]             # 잡은 상어 번호
            result += shark_info[shark_num][4]
            del shark_info[shark_num]       # 상어 정보 삭제
            A[r][c] = 0                     # 맵에서 상어 지우기
            break                           # 잡았으니 해당 열은 더이상 볼 필요 X
    A = shark_move()    # 상어 이동

print(result)      # 잡은 상어 크기의 합 출력