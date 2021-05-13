## 문제의 핵심
- 투포인터 
- 회전
# 알고리즘
- start, end 두개를 선언한다.
- 만약 k개가 차지 않았다면 end를 늘려가면서 맵내 원소를 증가
- 만약 k개가 찼다면 start를 하나씩 늘려가면서 맵내 원소개수를 증가
# 사용 자료구조
- 회전초밥 정보를 저장할 리스트
- 회전초밥내 최대 개수를 세기위한 dict

# 주요 Code Snippet
- EOF 까지 입력받기
```python
 while start < N:
        sushi_set[sushi[end%N]] = sushi_set.get(sushi[end%N], 0) + 1
        if end - start == k - 1:
            if max_length <= len(sushi_set):
                max_length = len(sushi_set) if c in sushi_set else len(sushi_set) + 1
            sushi_set[sushi[start]] -= 1
            if sushi_set[sushi[start]] <= 0:
                sushi_set.pop(sushi[start])
            start += 1
        end += 1
```

# 추정 시간복잡도
- 시간복잡도: O(n+k)
    - start가 0부터 n까지 움직임
    - k는 k만큼 거리차가 나야하므로
- 공간복잡도: O(2n)
    - tree: 최악의 경우 하나도 겹치지 않는경우: O(n)
    - tree_name: 하나도 겹치지 않는경우 O(n)
# 빠르게 푼사람 코드
- visited를 썼는데, 나도 왜저렇게 푼진 모르겠다.
- 좀더 봐야할것같다.
# 복기
- start, end의 끝처리(index out of bound)를 잘해줘야하는 문제이다. start가 언제시작하고 end가 언제끝나는지 계속 생각해봐야할것같다.
- 회전초밥이 언제 끝나는지 생각해봐야하는문제

