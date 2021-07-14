# 문제의 핵심
- Bigraph를 구현할 수 있는가

# Bigraph 개념
- 한간선에 연결된것이 서로 다른 색을 가져야함
- B - R
  |   |
  R - B

# 구현 방법
- 큐를 이용
- 색을 하나 결정하면 다음 인접한것은 반대로 설정

# Code Snippet
```python
def is_bigraph(graph, num_of_node):

    checked = [False for _ in range(num_of_node+1)]
    for i in range(1, num_of_node+1):
        if checked[i]:
            continue
        root, is_red = i, True
        queue = deque([(root, is_red)])
        visited = defaultdict(set)
        visited[is_red].add(root)
        checked[root] = True
        while queue:
            parent, is_red = queue.popleft()
            for child in graph[parent]:
                if is_visited(visited, child, is_red):
                    if child in visited[is_red]:
                        return False
                else:
                    visited[not is_red].add(child)
                    checked[child] = True
                    queue.append((child, not is_red))
    return True
```