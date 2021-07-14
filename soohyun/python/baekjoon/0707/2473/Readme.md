# 문제의 핵심
- 3개 포인터 다루는 법

# 알고리즘
- 1개는 고정하고
- 나머지 2개를 투포인터 돌린다

# Code Snippet
- 투포인터 
```python
def find_min(idx, liquid, N):
    s_value = liquid[idx]
    # 시작은 고정한 포인터 다음값, 끝은 마지막 인덱스
    end = N-1
    start = idx+1
    min_sum = math.inf
    min_value = [0, 0, 0]
    # 시작이 무조건 앞에 있어야함
    while start < end:
        # 전체 계산후
        lsum = s_value + liquid[start] + liquid[end]
        # min_sum 보정
        if min_sum > abs(lsum):
            min_sum = abs(lsum)
            min_value[0] = liquid[idx]
            min_value[1] = liquid[start]
            min_value[2] = liquid[end]
        # lsum이 양수라면 
        if lsum > 0:
            # 양수를 하나 줄여서 0과 가깝게 만들어줌
            end -= 1
        else:
            # lsum이 음수라면 음수를 하나 줄여서 0과 가깝게 만들어줌
            start += 1
    if min_value[0] == 0 and min_value[1] == 0 and min_value[0] == 0:
        return [-1, -1 ,-1]
    return min_value
```

- 세포인터
```python
 for idx, _ in enumerate(liquid):
        min_value = find_min(idx, liquid, N) # 처음포인터가 움직임
        if min_value[0] == min_value[1] == min_value[2] == -1:
            continue
        if min_diff > abs(sum(min_value)):
            min_diff = abs(sum(min_value))
            min_liquid = min_value
```
- 기억할것
    - 두번째 포인터는 무조건 첫번째 포인터 다음
        - 왜? 어차피 첫번째 포인터 이전인덱스는 첫번째 포인터 넣는것과 중복될테니까
# 시간복잡도
- O(n*n)

# 복기할것
- 포인터를 한번 더 봐야할듯하다.