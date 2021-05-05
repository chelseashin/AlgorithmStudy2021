# 시작시간: 12시 12분
# 문제를 해석한시간: 12시 38분
# ~ 12시 50분
# 시작: 
# 코딩시간:
# 디버깅시간:
import sys
input = sys.stdin.readline
grid  = list()
DR = [0, -1, -1, -1, 0, 1, 1, 1]
DC = [-1, -1, 0, 1, 1, 1, 0, -1]

def move_cloud(d, s, clouds, N):
    global grid
    new_clouds = dict()
    for x, y in list(clouds.keys()):
        first = (x + N + DR[d-1] * s) % N
        second = (y + N + DC[d-1] * s) % N
        new_clouds[(first, second)] = True
        grid[first][second] += 1
    return new_clouds


def copy_water(clouds, N):
    global grid
    for x, y in list(clouds.keys()):
        water_count = 0
        for dr, dc in zip([-1, -1, 1, 1], [-1, 1, -1, 1]):
            nx = x + dr
            ny = y + dc
            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] > 0:
                    water_count += 1
        grid[x][y] += water_count
    return clouds


def make_new_cloud(clouds, N):
    global grid
    new_clouds = dict()
    for i in range(N):
        for j in range(N):
            if grid[i][j] >= 2 and not clouds.get((i, j), False):
                new_clouds[(i, j)] = True
                grid[i][j] -= 2
    return new_clouds


def get_answer(N):
    global grid
    answer = 0
    for i in range(N):
        for j in range(N):
            answer += grid[i][j]
    return answer


def main():
    global grid
    grid = list()
    move = list()
    N, M = map(int, input().rstrip().split(" "))
    clouds = {(N-1, 0):True, (N-1, 1):True, (N-2, 0):True, (N-2, 1):True}

    for _ in range(N):
        grid.append(list(map(int, input().rstrip().split(" "))))
    for _ in range(M):
        d, s = tuple(map(int, input().rstrip().split(" ")))
        clouds = move_cloud(d, s, clouds, N)
        clouds = copy_water(clouds, N)
        clouds = make_new_cloud(clouds, N)
    answer = get_answer(N)
    print(answer)

if __name__ == "__main__":
    main()