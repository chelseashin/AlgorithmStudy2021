# 문제의 핵심
- 그래프 탐색
- 깊이 우선 탐색
# 사용 자료구조
- graph: dict 리스트
# 알고리즘
- 그래프를 입력받음
- 그래프를 지움
    - 지울노드의 자식들을 받음
    - 노드를 지움
    - 자식들을 하나씩 순회하면서 leaf node 일때까지 지운다.
- 남은 그래프를 센다.
    - 자식으로 남아있는 지울노드는 제외하고, 그래프내의 모든
      그래프를 지운다.
# Code Snippet
1. remove graph
```python
def remove_graph(graph, remove_node):
    def recursive(remove_node):
        if graph.get(remove_node, None) is None:
            return
        else:
            children = graph[remove_node]
            graph.pop(remove_node)
            for child in children:
                recursive(child)
    recursive(remove_node)
```
# 복기할것
- Key Error: 모든 노드(키)를 만들어주고 시작해야한다.
- Value Error: get 할때 None 에대한표시를 안해주면 None일때도 그냥 넘어간다.
- 틀렸습니다 1: 모든 노드가 연결되지 않은 리프노드 일때도 모두 셀수있어야한다. 
- 틀렸습니다 2: 자식노드로 표현된 removed_node는 지우지 않으므로 셀때 제외시켜야한다.
