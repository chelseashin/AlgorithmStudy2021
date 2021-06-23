# 걸린시간 2시간 20분

from collections import deque



def is_color_blindess(cur_color, color):
    if color == 'R' or color == 'G':
        if cur_color == 'R'or cur_color == 'G':
            return True
    return False


def init_values():
    N = int(input().rstrip())
    maze = [list(input().rstrip()) for _ in range(N)]
    return N, maze


def solution(N, maze):
    visited = [[0]*N for _ in range(N)]
    rg_count, count = 0, 0
    def bfs(is_visited, start, color):
        queue = deque()
        queue.appendleft(start)
        while queue:
            row, col = queue.popleft()
            for i, j in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                nr = row + i
                nc = col + j
                if 0 <= nr < N and 0 <= nc < N:
                    if visited[nr][nc] < is_visited:
                        if maze[nr][nc] != color:
                            if is_visited == 1 and is_color_blindess(maze[nr][nc], color):
                                visited[nr][nc] = is_visited
                                queue.appendleft((nr, nc))

                        else:
                            visited[nr][nc] = is_visited
                            queue.appendleft((nr, nc))

    for i in range(N):
        for j in range(N):
            # 적록 색맹 bfs
            if maze[i][j] == "R" or maze[i][j] == 'G':
                if visited[i][j] < 1:
                    bfs(1, (i, j), maze[i][j])
                    rg_count += 1
                # 적록 색맹이 아닌 bfs
                if visited[i][j] < 2:
                    bfs(2, (i, j), maze[i][j])
                    count += 1
            else:
                if visited[i][j] < 2:
                    bfs(2, (i, j), maze[i][j])
                    rg_count += 1
                    count += 1
    
    return count, rg_count
    

def main():
    N, maze = init_values()
    rg_count, count = solution(N, maze)
    print(rg_count, count)


if __name__ == "__main__":
    main()