# 문제의 핵심
- 모든 경우의수 나열하기
- 재귀 사용

# 사용 자료구조
- 방문표시: set()
- 출력결과: visited, list()

# 알고리즘
- 현재 완성된 문자열과 목표 문자열이 동일하면
    - 조건에 만족하는지 체크한후 출력
    - 만족하는 조건:
        - 이미 만들어진 문자가 아니고
        - 자음이 반드시 포함되있고
        - 모음이 2개이상 포함되어있는경우
- 목표문자열 개수와 동알하지 않으면
    - 아직아무것도 만들어지지 않았거나, 만들어진 문자열의 마지막이 앞으로 들어갈 문자보다 작은경우만(오름차순이므로!)
        - 새롭게 문자를 추가한다.

# Code Snippet
1. 재귀
```python
def solution(numbers, len_words):
    visited = []
    is_visited = set()
    all_words = len(numbers)
    def recurse(visited_len, visited):
        if visited_len == len_words:
            visited.sort()
            result = ''.join(visited)
            if is_satisfy_condition(result, is_visited, visited):
                print(result)
            return
        else:
            for character in range(visited_len, all_words):
                if visited_len == 0:
                    visited.append(numbers[character])
                    recurse(visited_len+1, visited)
                    visited.pop()

                elif visited[-1] < numbers[character]:
                    visited.append(numbers[character])
                    recurse(visited_len+1, visited)
                    visited.pop()
    recurse(len(visited), visited)
```
2. 모음 두자이상
```python
def is_vowels(visited):
    count = 0
    for value in visited:
        if value not in consonant:
            count += 1
            if count >= 2:
                return True
    return False
```
# 시간복잡도
- 시간복잡도 O(nCr):
    - n개중 r개를 뽑는 경우의 수
    
# 복기할것
- 틀렸습니다: 문제를 잘읽어야함 모음 2자이상 표현
- 재귀 문자 제대로 돌아가는지 확인할것