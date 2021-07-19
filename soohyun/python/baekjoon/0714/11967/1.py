from collections import defaultdict, deque
# 불켜진 모든곳에 다 간다면

def is_change(start, N, turn_on, previous_visit):
    queue = deque([start])
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True
    change_flag = False
    while queue:
        loc = queue.popleft()
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr, nc = loc[0]+dr, loc[1]+dc
            if 0 <= nr < N and 0 <= nc < N:
                print(loc[0]+1,loc[1]+1,"move", nr+1, nc+1, "turnon:", turn_on[nr][nc], "visited:", visited[nr][nc])
                if turn_on[nr][nc]:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        if not previous_visit[nr][nc]:
                            previous_visit[nr][nc] = True
                            change_flag = True
                        queue.append((nr, nc))
    return change_flag


def count_turn_on(hutgan, N):
    start = (0, 0)
    light_queue =deque([start])
    turn_on = [[False] * N for _ in range(N)]
    previous_visited = [[False] * N for _ in range(N)]
    count = 0
    while light_queue:
        loc = light_queue.popleft()
        print("light_pop", loc[0]+1, loc[1]+1)
        for room in hutgan[loc]:
            if not turn_on[room[0]][room[1]]:
                print("turn on", loc[0]+1, loc[1]+1,":",room[0]+1, room[1]+1)
                turn_on[room[0]][room[1]] = True
                count += 1

        queue = deque([loc])
        visited = [[False] * N for _ in range(N)]
        visited[loc[0]][loc[1]] = True
        change_flag = False
        while queue:
            loc = queue.popleft()
            for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                nr, nc = loc[0]+dr, loc[1]+dc
                if 0 <= nr < N and 0 <= nc < N:
                    print(loc[0]+1,loc[1]+1,"move", nr+1, nc+1, "turnon:", turn_on[nr][nc], "visited:", visited[nr][nc])
                    if turn_on[nr][nc]:
                        if not visited[nr][nc]:
                            visited[nr][nc] = True
                            if not previous_visited[nr][nc]:
                                previous_visited[nr][nc] = True
                                change_flag = True
                                print("light append:", nr+1, nc+1)
                                light_queue.append((nr, nc))
                            queue.append((nr, nc))
                            print("append:",nr+1, nc+1)
        if not change_flag:
            break
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