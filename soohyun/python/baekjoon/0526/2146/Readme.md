# 1. 문제의 핵심
- bfs
- 백트래킹
# 2. 풀이 알고리즘
1. 섬에 숫자를 붙여줌
  - make_island, 
  - find_same_island
    - bfs를 통해 하나의 섬으로 연결
2. 각섬에 다리를 연결함
   - 하나의 섬에서 모든섬까지 bfs를 실행함
      - 현재 섬은 모두 방문표시하여 큐에 넣어놓음
      - 다른섬을 만날때까지 아래를 진행함
        - 현재 모든 섬에서 한칸씩 앞으로 진행하며
          바다(0)인부분으 큐에 넣음

## 2.0 사용 자료구조
- 지도: 이차원 배열
- 섬의 정보: 딕셔너리 형태
  ```python
  {섬의 번호: 섬내 원소 개수}
  ```

## 2.2 Code Snippet
- 섬에 번호붙이는 코드(bfs)
```python
def find_same_island(i, j, kmap, N, island_num):
    queue = [(i, j)]
    island_info = {(i, j)}
    kmap[i][j] = island_num
    while len(queue) > 0: #큐가 빌때까지 반복
        row, col = queue.pop(0)
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1 ,1]):
            nr = row + dr
            nc = col + dc
            # 다음 행렬이 들어간다면 
            if nr >= 0 and nc >= 0 and nr < N and nc < N: # 범위내에 있고
                if kmap[nr][nc] == 1 and (nr, nc) not in island_info:
                    # 육지이고(1), 아직 방문하지 않았다면 
                    kmap[nr][nc] = island_num
                    # 육지를 섬번호로 바꿔줌
                    queue.append((nr, nc))
                    island_info.add((nr, nc))
                    # 섬정보에 넣음
    return list(island_info)
```
- 다리를 연결하는코드
```python
def bridge_bfs(island_info, kmap, island_num, N):
    queue = island_info
    visited = dict()
    result = 0
    for i, j in queue: # 섬의 모든 곳을 방문 표시한다.
        visited[(i,j)]=True

    while len(queue) > 0:
        size = len(queue) # 섬을 모두 큐에넣는다.
        for _ in range(size): # 모든 섬에서 
            row, col = queue.pop(0) # 섬에서 하나씩 빼면서
            for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]): 
                # bfs를 실행한다.
                nr = row + dr
                nc = col + dc
                if nr >= 0 and nc >= 0 and nr < N and nc < N:
                    if kmap[nr][nc] == 0 and not visited.get((nr, nc), False):
                        visited[(nr, nc)] = True
                        queue.append((nr, nc))
                    if kmap[nr][nc] != 0 and kmap[nr][nc] != island_num:
                        # 섬이 아닌곳을 만났으면
                        # 바로 result를 반환한다.
                        return result
        # 모든 섬으로부터 한칸씩 증가시켰으므로 result를 한칸 증가한다.
        result += 1
    return result

```
# 3. 시간 복잡도
- O(4n*n*n): 
    - O(4n*n): 기준섬내의 모든 위치에서 bfs
    - O(n*n): 일반적인 bfs 코드
# 4. 빨리푼사람 코드
- 섬주변을 -1로 마킹함
- 만약 -1을 만난다면 순회를 멈춤


# 5. 복기할것
- 가장 많이 틀린문제
- 가장 많이 시간이 걸린 문제
- 처음에는 각 섬에 하나의 원소만 가져와서 bfs 돌렸는데 시간초과남
    - 원인: 하나의 위치에서 다른 섬의 모든 위치까지 둘러봐야함
    - 아직 이해안감.....ㅠㅠ
    - 참고한 코드와 다른점: 참고한 코드는 기준섬의 모든 위치를 고려함