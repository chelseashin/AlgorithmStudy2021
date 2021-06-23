import sys
input = sys.stdin.readline

def is_in_range(rlen, clen, dia_row, dia_col):
    if 0 <= dia_row < rlen and 0 <= dia_col < clen:
        return True
    return False


def bfs(maze, horse_chance, r_len, c_len):
    count = 0
    queue = [(0, 0, count, horse_chance)]
    visited = {(0, 0)}
    dia_visited = {(0, 0)}

    while queue:
        row, col, count, horse_chance = queue.pop(0)
        if (row, col) == (r_len-1, c_len-1):
            return count
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            cur_row = row + dr
            cur_col = col + dc
            if is_in_range(r_len, c_len, cur_row, cur_col):
                if horse_chance > 0:
                    for diagonal in [-1, 1]:
                        if dr == 0:
                            dia_row, dia_col = cur_row+diagonal, cur_col + 1
                        elif dc == 0:
                            dia_row, dia_col = cur_row+1, cur_col + diagonal
                    
                        if is_in_range(r_len, c_len, dia_row, dia_col):
                            if maze[dia_row][dia_col] == 0:
                                if (dia_row, dia_col) not in dia_visited: 
                                    #print("dia", "(",dia_row, dia_col, ") count:", count+1)
                                    queue.append((dia_row, dia_col, count+1, horse_chance-1))
                                    dia_visited.add((dia_row, dia_col))   
                                                 
                if  maze[cur_row][cur_col] == 0:
                    if (cur_row, cur_col) not in visited:
                        # print("cur", "(", cur_row,  cur_col, ")count:", count+1)
                        queue.append((cur_row, cur_col, count+1, horse_chance))
                        visited.add((cur_row, cur_col))     
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