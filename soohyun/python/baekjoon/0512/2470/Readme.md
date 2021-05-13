## 문제의 핵심
- 투포인터 
# 알고리즘
- 작은수, 큰수 정렬먼저 할것
- 결과가 0보다 작다면 시작 인덱스를 하나씩 더해준다.
- 결과가 0보다 크다면 끝 인덱스를 하나씩 빼주어 왼쪽으로 간다.
- 나오는 결과들마다 하나씩 더해줘서 결과를 출력해준다.
# 사용 자료구조
- 정보를 담는 리스트
# 주요 Code Snippet
```python
 while start < end:
        result = liquids[end] + liquids[start]
        if min_result > abs(result):
            min_result = abs(result)
            idx_list = (liquids[start], liquids[end])
        if result < 0:
            start += 1
        elif result > 0:
            end -= 1
        else:
            idx_list = (liquids[start], liquids[end])
            break
```

# 추정 시간복잡도
- 시간복잡도: O(n)
    - 최악의 경우 n-1 까지 갈 수 있으므로
- 공간복잡도: O(2n)
    - tree: 최악의 경우 하나도 겹치지 않는경우: O(n)
    - tree_name: 하나도 겹치지 않는경우 O(n)
# 빠르게 푼사람 코드
- visited를 썼는데, 나도 왜저렇게 푼진 모르겠다.
- 좀더 봐야할것같다.
# 복기
- 풀이방법만 알면 금방 맞출 수 있는 문제.
- 학부때 많이 풀어본 종류임에도 불구하고 왜 풀이법을 보고 풀었는지 모르겠다.
- 정렬은 절대 하면 안된다고 생각했는데, nlogn은기본적으로 깔고 가는구나 싶다.
- quick sort를 투포인터로 푼 기억이 난다.


