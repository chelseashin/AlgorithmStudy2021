# 1시 10분
import sys

DX = (-1, 1, 2)


def find_sister(N, limit, visited, K):
    queue = list()
    queue.append((N, 0, 0))
    visited[N] = [0, 1]
    min_count = 100000000000
    while len(queue) > 0:
        # 현재위치, 걸린시간, 현재위치로 오는 방법수 
        num, second, visit_count = queue.pop(0)
        if num == K:
            min_count = second
        if (second+1) > min_count:
            break
        for dx in DX:
            if dx == 2:
                nx = num * 2
            else:
                nx = num + dx
            if nx < 0 or nx > limit:
                continue
            # 아직 방문 안했거나, 기존 방문이 현재방문보다 크다면
            if visited[nx][1] == 0 or visited[nx][0] > (second+1):
                visited[nx][0] = second + 1
                visited[nx][1] = 1
                queue.append((nx, second + 1, 1))
            # 기존의 방문과 현재 방문의 수가 동일하다면
            elif visited[nx][0] == (second+1):
                visited[nx][1] += 1
                queue.append((nx,  second + 1, visited[nx][1]))
    return visited[K][0], visited[K][1]

 
def main():
    N, K = map(int, sys.stdin.readline().rstrip().split(" "))
    visited = []
    if N == 0:
        division = N + 1
    else:
        division = N
    visited_size = (K//division+1)*division + 1
    for _ in range(visited_size):
        visited.append([0, 0])
    return find_sister(N, visited_size-1, visited, K)


if __name__ == "__main__":
    min_value, min_count = main()
    print(min_value)
    print(min_count)