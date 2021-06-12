import sys
input = sys.stdin.readline

def is_in_range(rlen, clen, dia_row, dia_col):
    if 0 <= dia_row < rlen and 0 <= dia_col < clen:
        return True
    return False


def bfs(maze, horse_chance, r_len, c_len):
    count = 0
    queue = [(0, 0, count, horse_chance)]
    #visited = [[[0] * (horse_chance + 1) for _ in range(r_len)] for _ in range(c_len)]
    for i in range(horse_chance+1):
        visited[i] = set()
    while queue:
        row, col, cur_horse_chance = queue.pop(0)
        if (row, col) == (r_len-1, c_len-1):
            return visited[row][col][count] - 1
        for dr, dc in [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]:
            dia_row = row + dr
            dia_col = col + dc
            if horse_chance > cur_horse_chance:
                if is_in_range(r_len, c_len, dia_row, dia_col):
                    if maze[dia_row][dia_col] == 0:
                        if (dia_row, dia_col) not in visited[dia_row][dia_col][cur_horse_chance+1]: 
                            #print("dia", "(",dia_row, dia_col, ") count:", count+1)
                            queue.append((dia_row, dia_col, cur_horse_chance+1))
                            visited[dia_row][dia_col][cur_horse_chance+1] = visited[dia_row][dia_col][cur_horse_chance] + 1
                            
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            cur_row = row + dr
            cur_col = col + dc
            if is_in_range(r_len, c_len, cur_row, cur_col):
                if (cur_row, cur_col) not in visited[0] and maze[cur_row][cur_col] == 0:
                    # print("cur", "(", cur_row,  cur_col, ")count:", count+1)
                    queue.append((cur_row, cur_col, count+1, horse_chance))
                    visited[cur_row][cur_col][horse_chance] = visited[cur_row][cur_col][horse_chance] + 1
    return 0
        

def main():
    # input 받기
    horse_chance = int(input().rstrip())
    N, M = map(int, input().rstrip().split(" "))
    maze = [list(map(int, input().rstrip().split(" "))) for _ in range(N)]
    result = bfs(maze, horse_chance, N, M)
    print(-1) if result == 0 else print(result)

if __name__ == "__main__":
    main()