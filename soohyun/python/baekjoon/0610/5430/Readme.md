# 문제
-  https://www.acmicpc.net/problem/5430
# 걸린시간
- 40분
# 문제의 핵심
- 구현
- reverse를 하라해서 실제로 하면 안되는 문제
# Code Snippet
```python
# 정규표현식
    pattern = re.compile('([0-9]+)')
    result = pattern.findall(raw_str)
```
```python
# 거꾸로 출력
    arr = list(arr)
    if is_forward:
        return '['+','.join(arr)+']'
    return '['+','.join(arr[::-1])+']'
```
# 복기할것 & 실수한것
- reverse를 그대로함
- 거꾸로 출력하는 거 답 참고함
- pop(0)가 시간복잡도 O(n)이였다. 앞으로 deque를 써야겠다.