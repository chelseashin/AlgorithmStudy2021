# 문제
-  https://www.acmicpc.net/problem/1238
# 걸린시간
- 1시간 30분
# 문제의 핵심
- 최단거리 알고리즘 사용
    - 다익스트라
    - 벨만포드(사용법 익힐것)
# 알고리즘 
1. 다익스트라 알고리즘 (***중요***)
    - 알고리즘의 핵심: ***특정 정점*** 에서 모든 정점까지의 최단거리
    - 알고리즘:
        1. 모든 정점간의 거리를 무한대로 초기화
        2. 특정정점의 거리는 0으로 초기화
        3. 특정정점을 시작정점으로두고 아래를 반복

            3.1. 시작정점과 연결된 노드들을순회

            3.2. 순회하면서 
            
            시작노드거리 + 연결된 거리 < 현재 저장된 노드거리이면 
            현재 노드거리를 갱신

            3.3. 계신된 거리가 가장 ***작은*** 것을 시작정점으로 두고 3을 다시 반복
2. 코드 알고리즘
    1. 목적지 정점을 제외한 모든정점에서의 최단거리를 구함 (목적지로 출발)
    2. 목적지 정점에서의 최단거리를 구함 (목적지에서 출발지로 돌아감)
    3. 목적지로 출발하는 정점[목적지] + 출발지 돌아가는 정점[현출발지] 의 최대값을 구함

# Code Snippet
```python
# dijkstra 알고리즘
min_dist = [math.inf] * nodes_num
    min_dist[start_node] = 0
    queue = [(0, start_node)]
    while queue:
        weight, popped_node = heapq.heappop(queue)
        for node in graph[popped_node]:
            if weight + node.con_weight < min_dist[node.con_node]:
                min_dist[node.con_node] = weight + node.con_weight
                heapq.heappush(queue, (min_dist[node.con_node], node.con_node))

    return min_dist
```
# 복잡도
- 시간 복잡도: O(node*edge)

- 공간 복잡도: O(node)

# 실수한 부분
- 가장 작은 부분을 찾기위해 heappush를 넣는도중 weight 계산 실수 
    - 갱신된 결과를 넣어야하는데
    - 현노드가 연결된 노드만 넣어버림
- idx 계산 실수
    - 입력은 1부터, 계산은 0부터 계산해야함

