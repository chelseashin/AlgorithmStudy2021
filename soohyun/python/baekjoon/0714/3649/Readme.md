# **문제의 핵심**
- 투포인터
- 입력받기

# **알고리즘**
1. 블록 면적과 동일하게 맞아떨어지는경우
    - 만약 저장된것이 있으면 |l1 - l2| 값비교
    - 저장된것이 없으면 그대로 temp에 값을 저장
2. 숫자가 크면 start를 옮김
3. 숫자가 작으면 end로 옮김

# **Code Snippet**
1. **투 포인터**

```python
 while start < end:
        if lego[start] + lego[end] == nano_width:
            # 면적이 동일한경우
            # 저장된 값이 있으면
            if sum(result) >= 0:
                # 값비교 후 갱신
                if abs(result[0] - result[1]) < abs(lego[start] - lego[end]):
                    result[0] = lego[start]
                    result[1] = lego[end]
            else:
                # 단순 저장
                result[0] = lego[start]
                result[1] = lego[end]
            end -= 1
            start += 1
        # 면적이 동일하지 않은경우
        # 포인터를 옮김
        if lego[start] + lego[end]  > nano_width:
            end = end - 1
        elif lego[start] + lego[end]  < nano_width:
            start = start + 1
```

2. **EOF까지 입력받기**

    1.1) **read 사용하기** -> 메모리초과
    ```python
    inputs = sys.stdin.read().split("\n")
    while idx < len(inputs)
        value =  inputs[idx]
        if value == '':
            break
        width = int(inputs[idx].rstrip())
        idx += 1
       ...
    ```
    1.2) **readline 사용하기**
    
    ```python
    while True:
        value =  input().rstrip()
        if value == '':
            break
        width = int(value)
        ...
    ```

    1.3) **try except 문사용하기**
    ```python
    while True:
        try:
            width =  int(input().rstrip())
            ...
        except:
            break
    ```
# **복기할것**
- 테스트케이스가 하나의 입력안에 여러번 들어올것이라 생각하지 못했음
- 두개의 블록이 구멍의 너비와 동일한경우에도 투포인터를 옮겨주어야한다. 

<detail>
<details>
<summary>전체 코드</summary>
<div markdown="1">

# **소스코드**


</detail>