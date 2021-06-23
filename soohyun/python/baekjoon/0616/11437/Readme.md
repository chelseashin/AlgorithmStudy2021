# 문제의 핵심
- 트리
- 최소 공통조상 찾는법

# 알고리즘
- 양방향 그래프 제작
- 트리와, 노드의 깊이를 저장한 배열 제작
- 같은 부모를 찾을때가지 아래를 반복
    - 깊이가 같고 두노드의 부모가같다면 부모를 부모를 반환
    - 깊이가 같고 부모가같지 않다면 그래프를 통해 부모를 찾아감
    - 깊이가 다르다면 깊이를 서로 맞춰줌
# 자료구조
 - 깊이 리스트: 인덱스는 자식, 값은 자식깊이를 나타내는 그래프
 - 그래프: 인덱스는 자식, 값은 부모를 나타내는 리스트

 # Code Snippet
 ```python
 def solution(graph, depth):
    def LCA(start, end):
        while True:
            if depth[start] == depth[end]:
                if start == end:
                    return start
                else:
                    start, end = graph[start], graph[end]
            elif depth[start] > depth[end]:
                start = graph[start]
            else:
                end = graph[end]

    for start, end in input_value(CMD.QUERY):
        yield LCA(start, end)
 ```
 ```python

def make_pgraph(graph):
    pgraph = [0] * (len(graph.keys())+1)
    depth_info = [0] * (len(graph.keys())+1)
    queue = deque()
    queue.appendleft((1, 0))
    while queue:
        parent, depth = queue.popleft()
        childs = graph[parent]
        for child in childs:
            if child != 1 and pgraph[child] == 0:
                pgraph[child] = parent
                depth_info[child] = depth + 1
                queue.append((child, depth+1))
    return pgraph, depth_info
```
# 시간복잡도
O(2*NlogN): 트리높이만큼 순회하는 횟수
# 비슷한 풀이

# 복기할것
- 트리의 특징
    - 부모는 1개,
    - 사이클이없음