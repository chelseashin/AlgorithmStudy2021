# 1. 문제의 핵심
- 깊이우선 탐색
- 백트래킹
# 2. 풀이 알고리즘
1. 깊이우선탐색을 통해 25개의 숫자중 7개를 뽑는 모든 경우의 수를 나열한다.
2. 나열된 숫자중 S가 4개이상이고, 7개가 모두 인접한 경우의 수를 count한다.

## 2.0 사용 자료구조
- 좌석: 2차원 배열
- 학생: 리스트

## 2.2 Code Snippet
- dfs 코드
```python
def dfs(seats, count, start):
    result = 0
    if len(count) == 7:
        if is_over_four(seats, count) and is_adjacement(count):
            # 4이상이거나 인접한경우는 
            return 1 # 갯수를 세고
        else: 
            return 0 # 그렇지 않은경우 0으로 반환
    else:
        for i in range(start, 25): # 시작부터 25까지 반복
            if len(count) <= 0 or count[-1] < i: 
                # 모아진 학생수(count)가 비어있거나
                # 모아진 학생수의 마지막 숫자가 현재보다 작다면(왜?)
                # 1 2 3 4 5 6 7, 1 2 3 4 5 6 8 식으로 넘어가므로
                count.append(i) # 학생수 추가함
                result += dfs(seats, count, start+1) 
                # dfs는 시작을 하나 더해주고 (정렬식이므로) 다음으로 넘어간다.
                count.pop() # 학생수를 빼주고 다음으로 넘어감
        return result
```

```python
def is_adjacement(count): # 7개가 인접한경우를 보는것
    first_num = count[0]
    count_set = set(count)
    compare_set = {first_num}
    queue = [first_num]
    while queue:
        num = queue.pop(0)
        row, col = num // 5, num % 5 # 숫자를 좌표로 바꾸는 방법
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr, nc = row + dr, col + dc
            if 0 <= nr < 5 and 0 <= nc < 5:
                num = nr * 5 + nc
                if num in count_set:
                    if num in compare_set:
                        continue
                    compare_set.add(num)
                    queue.append(num)
    if len(compare_set) == len(count_set):
        # bfs를통해서 인접한것을 모두 찾은결과
        return True # True를 반환
    return False # 그렇지 않으면 False를 반환
```



```python
def is_over_four(seats, student_list): # S가 4개 이상인경우
    count = 0
    for num in student_list: # 학생리스트 중에서
        row, col = num // 5 , num % 5 # 좌표가
        if seats[row][col] == 'S': # S인경우를 센다.
            count += 1
    if count >= 4: # 4이상이면
        return True # True 반환
    return False

```
# 3. 시간 복잡도
- O(n * n * C(25, 7)): 정렬 + 2개씩 뽑는 경우의 수 
    - O(n): 인접한지 뽑는경우 여기서 n은 7
    - O(n): 4개이상 뽑는경우 여기서 n은 7
    - C(25,7): 25개중 7개를 dfs 돌리는경우의수
# 4. 빨리푼사람 코드 및 복기할것
- 처음에는 반대로 풀었다. S가 7개 이상이고 인접한 Y를 찾는 코드를 만들었는데, 경로 진행상 똑같은 경우가 반복될수밖에없어서 포기
- 답을 조금 참고해서 풀었다 (아이디어를 얻음).
- 숫자를 좌표로 바꾸는 방법을 배움! 
```python
row, col = num // 5, num % 5 # 숫자를 좌표로 바꾸는 방법
```
