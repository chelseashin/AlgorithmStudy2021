# 문제의 핵심
- bfs에서 적당한 조건을 추가할 수 있는지 묻는 문제

# 사용 자료구조
- 큐: 데크
- visited: 2차원 배열
- fires: 리스트내 튜플
- person: 위치들어있는 튜플

# 알고리즘
- visited와 queue를 선언함
**- 큐에 불의 위치와 사람의 위치를 차례로 넣음**
- 큐가 빌때까지 다음을 반복함
    - 큐에서 원소를 하나 뽑음
    - 뽑은 원소가 사람이고 가장자리에 도착했을때는 count를 반환함
    - 상하좌우를 모두 돌면서
        - 범위밖에있거나 벽인경우 넘어감
        - 방문하지 않은경우
            - 현재 불, 혹은 사람의 위치를 넣어주고
            - 큐에 count를 하나 더해준후 다음으로 진행
        **- 현재 장소가 불이고 다음위치가 사람일경우는 불은 사람을 넘어갈 수 있으므로**
            - 큐에 넣어주고 다음으로 진행

# Code Snippet
```python
def solution(maze, fires, person):
    height, width = len(maze), len(maze[0])
    queue = deque()
    visited = make_visited(fires, person, height, width)
    for fire in fires:
        queue.appendleft((PLACE.FIRE, fire, 0))
    queue.appendleft((PLACE.PERSON, person, 0))

    while queue:
        place, loc, count = queue.pop()
        if is_arrive(place, loc, height, width):
            return count
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr, nc = loc[0] + dr, loc[1] + dc
            if not is_inrange((nr, nc), height, width):
                continue
            if maze[nr][nc] == '#':
                continue

            if visited[nr][nc] == 0:
                visited[nr][nc] = place
                queue.appendleft((place, (nr, nc), count+1))
            if place == PLACE.FIRE and visited[nr][nc] == PLACE.PERSON:
                visited[nr][nc] = place
                queue.appendleft((place, (nr, nc), count+1))
    return -1
```
# 복잡도
- 시간복잡도 O(N*M): maze크기만큼 반복되므로
- 공간복잡도 O(N*M): visited의 크기

# 빨리 푼사람 풀이
- 특별할게 없어보임.. 잘모르겠다.

# 복기할것
- 틀렸습니다: 불을 사람보다 더 먼저 큐에 넣어야함!
