import sys
input = sys.stdin.readline

dr1 = [1, -1, 0, 0]
dc1 = [0, 0, 1, -1]
dr2 = [1, 1, -1, -1, 2, 2, -2, -2]
dc2 = [2, -2, 2, -2, 1, -1, 1, -1]

def bfs(horse_chance, width, height, maze):
    queue = list()
    visited = c = [[[0]*(horse_chance+1) for _ in range(width)] for _ in range(height)]
    queue.append([0, 0, 0])
    visited[0][0][0] = 1
    while queue:
        row, col, cur_hc = queue.pop(0)
        if col == width-1 and row == height-1:
            print(visited[row][col][cur_hc]-1)
            return
        if cur_hc < horse_chance:
            for i in range(8):
                nr = row + dr2[i]
                nc = col + dc2[i]
                if 0 <= nr < height and 0 <= nc < width:
                    if maze[nr][nc] == 0 and c[nr][nc][cur_hc+1] == 0:
                        visited[nr][nc][cur_hc+1] = visited[nr][nc][cur_hc] + 1
                        queue.append([nr, nc, cur_hc+1])

            for i in range(4):
                nrow = row + dr1[i]
                ncol = col + dc1[i]
                if 0 <= nrow < height and 0 <= ncol < width:
                    if maze[nrow][ncol] == 0 and visited[nrow][ncol][cur_hc] == 0:
                        c[nrow][ncol][cur_hc] = c[nrow][ncol][cur_hc] + 1
                        queue.append([nrow, ncol, cur_hc])
        elif cur_hc == horse_chance:
            for i in range(4):
                nrow = row + dr1[i]
                ncol = col + dc1[i]
                if 0 <= nrow < height and 0 <= ncol < width:
                    if maze[nrow][ncol] == 0 and visited[nrow][ncol][cur_hc] == 0:
                        c[nrow][ncol][cur_hc] = c[nrow][ncol][cur_hc] + 1
                        queue.append([nrow, ncol, cur_hc])


def main():
    horse_chance = int(input())
    col, row = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(col)]
    bfs(horse_chance, col, row, maze)

if __name__ == "__main__":
    main()