# 1. 문제의 핵심
1. backtracking
2. 걸린시간 약 1시간 + a
3. 부모노드의 모든 자식을 넣어주고 하나씩 빼면서 재귀를 돌린다.

# 2. 알고리즘
## 2.0 재귀 형태
0. 인자: 그래프, 부모노드로부터의 같은 레벨의 자식들
1. 연산: 그래프의 자식을 모두 넣어준다.
2. 재귀가 반환되는경우: 자식리스트가 아무도 없는경우
3. 그밖의 경우: 일반 dfs와 동일
    
## 2.1 알고리즘
```python
# 인자

# 연산
for 노드 in 현재레벨의 노드들:
    if: 노드의 자식이 없다면 무시
    else: child_list에 넣는다.
#초기값
if: 리프노드인경우
    return 현재 노드개수를 반환
else: 중간 노드인경우
    child를 하나씩 빼면서
    그 결과를 반환
    결과가 min값보다 작으면 갱신
    min값보다 작은값과 현재 노드의 개수를 반환

```
## 2.2 code snippet
```python
 for node in nodes:
        if not graph.get(node, False) or len(graph[node]) <= 0:
            continue
        child_list.extend(graph[node])
```
```python
    if len(child_list) <= 0:
        return len(nodes)
```

```python
        for _ in range(len(child_list)):
            node = child_list.pop(0)
            result = dfs(graph, child_list)
            child_list.append(node)
            if result < min_result:
                min_result = result
        return min_result + len(nodes)
```


# 3. 시간 복잡도 및 공간 복잡도
1. 시간복잡도: O(n^2)
   - O(n): 모든 블록 순회
   - O(n/2): 좌우로 한번더 순회(nxn에서 절반만 순회)
2. 공간복잡도: O(n^2)
   - nxn피라미드를 저장

# 4. 복기할것
1. 초기값 정의: return되어야하는지 생각할것
2. 초기값으로부터 어떻게 반환되어야할지 정의