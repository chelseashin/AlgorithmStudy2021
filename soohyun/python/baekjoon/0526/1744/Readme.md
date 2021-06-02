# 1. 문제의 핵심
- 그리디 알고리즘
- 가장 최적의 알고리즘을 구할 수 있는가?
    -  0과 음수는 곱해야 최대값
    -  양수는 곱해서 최대가 되지 않을 수 있음
        - ex) 1+1 vs 1*1
# 2. 풀이 알고리즘
- 음수와 0 리스트 입력받아 역순 정렬 (minus)
- 양수는 리스트 입력받아 정렬 (plus)
   - 곱하는거면 제일 큰수부터 입력받아야  크므로
- 양수/음수리스트 각각 두개씩뽑아 곱함
- 두개씩 안뽑히는건 더하기로 마무리

## 2.0 사용 자료구조
1. 양/음수리스트: 리스트

## 2.2 Code Snippet
```python
while len(plus) >= 2 or len(minus) >= 2:
    if len(plus) >= 2:
        num_1 = plus.pop()
        num_2 = plus.pop()
        if num_1 + num_2 > num_1 * num_2:
            sum_result += num_1 + num_2
        else:
            sum_result += num_1 * num_2
        if len(minus) >= 2:
            sum_result += minus.pop() * minus.pop()
```
```python
minus = sorted(minus, reverse=True)
```
# 3. 시간 복잡도
- O(nlong + n/2): 정렬 + 2개씩 뽑는 경우의 수 
# 4. 빨리푼사람 코드 및 복기할것
- 처음에 감이 안잡혀서 답을 좀 참고함
- 더하기가 곱하기보다 빠른경우가 있었음

