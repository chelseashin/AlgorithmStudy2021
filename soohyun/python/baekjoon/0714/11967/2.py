from collections import defaultdict, deque
def count_turn_on(hutgan, N):
    queue = deque([(0, 0)])
    turn_on = [[False] * N for _ in range(N)]
    can_visit = [[False] * N for _ in range(N)] 
    visited = [[False] * N for _ in range(N)]    
    turn_on[0][0] = True
    while queue:
        loc = queue.popleft()
        for light in hutgan[loc]:
            if not turn_on[light[0]][light[1]]:
                turn_on[light[0]][light[1]] = True
                
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1 ,1]):
            nr, nc = loc[0] + dr, loc[1] + dc
            if 0 <= nr < N and 0 <= nc < N:
                can_visit[nr][nc] = True

        for i in range(0, N):
            for j in range(0, N):
                if can_visit[i][j] and turn_on[i][j] and not visited[i][j]:
                    visited[i][j] = True
                    queue.append((i, j))
    count = 0
    #for row in turn_on:
    #    print(*row)
         
    for i in range(N):
        for j in range(N):
            if turn_on[i][j]:
                count += 1
    return count

        

def main():
    N, M = map(int, input().rstrip().split(" "))
    hutgan = defaultdict(list)
    for _ in range(M):
        start_r, start_c, end_r, end_c = \
            map(int, input().rstrip().split(" "))
        hutgan[(start_r-1, start_c-1)].append((end_r-1, end_c-1))
    print(count_turn_on(hutgan, N))

if __name__ == "__main__":
    main()