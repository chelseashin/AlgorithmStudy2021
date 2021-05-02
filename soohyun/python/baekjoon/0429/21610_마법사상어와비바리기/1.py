# 시작시간: 12시 12분
# 문제를 해석한시간: 12시 38분
# ~ 12시 50분
# 시작: 
# 코딩시간:
# 디버깅시간:
import sys
input = sys.stdin.readline
DR = [0, -1, -1, -1, 0, 1, 1, 1]
DC = [-1, -1, 0, 1, 1, 1, 0, -1]
def magic(grid, move, N):
    clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
    for d, s in move:
        # 구름 이동
        #print("before", clouds, d, s)
        for cloud in clouds:
            cloud[0] = (cloud[0] + N + DR[d-1] * s) % N
            cloud[1] = (cloud[1] + N + DC[d-1] * s) % N
            grid[cloud[0]][cloud[1]] += 1
        # 물의양 증가
        #print("after", clouds, d, s)
        
        #print("==water==")
        #print_grid(grid)
        # 물복사 버그
        for cloud in clouds:
            x = cloud[0]
            y = cloud[1]
            water_count = 0
            for dr, dc in zip([-1, -1, 1, 1], [-1, 1, -1, 1]):
                nx = x + dr
                ny = y + dc
                if 0 <= nx < N and 0 <= ny < N:
                    if grid[nx][ny] > 0:
                        water_count += 1
            grid[x][y] += water_count
        #print_grid(grid)
        # 2이상인 모든 칸에 구름, 기존 구름 제외
        new_clouds = list()
        for i in range(N):
            for j in range(N):
                if grid[i][j] >= 2 and not in [i, j]:
                    new_clouds.append([i, j])
                    grid[i][j] -= 2
        del clouds
        clouds = new_clouds
        #print(clouds)
        #print_grid(grid)

    answer = 0
    for i in range(N):
        for j in range(N):
            answer += grid[i][j]
    return answer
        

def print_grid(grid):
    print("==start==")
    for i in range(len(grid)):
        print(*grid[i])
    print("==end==")


def main():
    grid = list()
    move = list()
    N, M = map(int, input().rstrip().split(" "))
    for _ in range(N):
        grid.append(list(map(int, input().rstrip().split(" "))))
    for _ in range(M):
        move.append(tuple(map(int, input().rstrip().split(" "))))
    print(magic(grid, move, N))

if __name__ == "__main__":
    main()