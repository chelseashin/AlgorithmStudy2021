from collections import deque

def dfs(virus, act_num, result, current):
    visited = [False]* len(virus)
    if act_num == len(current):
        result.add(tuple(current))
        return
    else:
        for i in range(0, len(virus)):
            if not visited[i]:
                if len(current) <= 0:
                    visited[i] = True
                    current.append(i)
                    dfs(virus, act_num, result, current)
                    current.pop()
                    visited[i] = False

                elif current[len(current)-1] < i:
                    visited[i] = True
                    current.append(i)
                    dfs(virus, act_num, result, current)
                    current.pop()
                    visited[i] = False

def activate_virus(width, act_num, labs, virus, virus_map):
    result = set()
    dfs(virus, act_num, result, [])
    answer_max = -1
    while result:
        virus_loc = result.pop()
        visited = [[0]*width for _ in range(width)]
        for loc in virus_loc:
            cur_virus = virus[loc]
            queue = deque([(cur_virus, 0)])
            visited[cur_virus[0]][cur_virus[1]] = 0
            while queue:
                cur_loc, count = queue.pop()
                for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                    nr, nc = cur_loc[0] + dr, cur_loc[1] + dc
                    if 0 <= nr < width and 0 <= nc < width:
                        if labs[nr][nc] == 1:
                            visited[nr][nc] = '-'
                        if labs[nr][nc] != 1:
                            if visited[nr][nc] == 0 or visited[nr][nc] > count+1:
                                visited[nr][nc] = count+1
                                queue.appendleft(((nr, nc),count+1))
            visited[cur_virus[0]][cur_virus[1]] = 0

        total_max = 0
        is_complete = True
        for i in range(width):
            for j in range(width):
                if labs[i][j] != 1 and not virus_map[i][j] and visited[i][j] == 0:
                    is_complete = False
                    break
                if labs[i][j]!=1 and visited[i][j]!='-' and visited[i][j] > total_max:
                    if not virus_map[i][j]:
                        total_max = visited[i][j]

        if is_complete and (answer_max == -1 or answer_max > total_max):
            answer_max = total_max
        #print("answer", answer_max)
        #print_visited(visited)
        #previous_max = max_num

    return answer_max

def print_visited(visited):
    print("")
    for row in visited:
        print(*row)
    print("")
    

            



def main():
    width, activate_num = map(int, input().rstrip().split(" "))
    virus_map = [[False]*width for _ in range(width)]
    labs = list()
    virus = list()
    zero_count = 0
    for i in range(width):
        row = list(map(int, input().rstrip().split(" ")))
        for j in range(width):
            if row[j] == 0:
                zero_count += 1
            elif row[j] == 2:
                row[j] = 0
                virus_map[i][j] = True
                virus.append((i, j))
        labs.append(row)
    
    print(0) if zero_count <= 0 else print(activate_virus(width, activate_num, labs, virus, virus_map))

if __name__ == "__main__":
    main()