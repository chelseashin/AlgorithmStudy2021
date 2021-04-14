# 1. 핵심
전형적인 bfs 문제
3차원으로 변형한것
# 2. 걸린시간: 2시간 18분
 * 문제 해석 시간: 3분
 * 계획 시간: 18분
 * 코딩 시간: 43분
 * 디버깅 시간: 15분
 * 수정 제출 시간: 59분 


# 3.  알고리즘
## 3.1 시퀀스
```python
    while True:
        building = input()
        bfs(building)
```
## 3.2 bfs에서 필요한것
```
- input
    - 3차원 배열필요 l,r,c
    - 시작위치 저장필요
    - 끝위치 저장필요
- visited
    - 따로 visited로 만들지 않고 'T'문자로 바꿈
- maze
    - 동서남북, 위, 아래
    - 방문했는지 검사, 벽이 있는지 검사
- queue
    - 현재좌표, 현재까지 최단거리 저장
    - E에 도달했으면 break
```

## 3.3 code snippet
### 3.3.1 is_go
```python
def is_go(building, next_loc):
    level, r, c = next_loc
    if level < 0 or r < 0 or c < 0:
        return False
    if level >= len(building) or \
       r >= len(building[0]) or \
       c >= len(building[0][0]):
        return False
    if building[level][r][c] == '#':
        return False
    if building[level][r][c] == 'T':
        return False
    return True
```
### 3.3.2 regex로 start, end찾기
```python
def find_start_end_loc(row, letter):
    result = re.search(letter, row)
    if result is not None:
        return result.start()
    return -1
def start_end(row, letter):
    result = find_start_end_loc(row, letter)
    if result != -1:
        return result
    return None
```
### 3.3.3 bfs
```python
def bfs(building, start_end_loc):
    queue = [(start_end_loc['start'], 0)]  
    dist = -1
    while len(queue) > 0:
        loc, dist = queue.pop(0)
        l, r, c = loc
        if loc == start_end_loc['end']:  # 도착한경우
            return dist        
        for dl, dr, dc in zip(DL, DR, DC):  # 6방향 순회
            next_loc = l + dl, r + dr, c + dc
            if is_go(building, next_loc):
                queue.append((next_loc, dist+1))  # 큐넣기
                building[l+dl][r+dr][c+dc] = 'T'  # 방문체크
    return -1
```
# 3. 추측 시간 복잡도 및 공간 복잡도
- 실측 시간 및 메모리
    - 메모리: 134004 KB
    - 시간: 332 ms
- 시간복잡도: O(6 * n)
    -  O(n): bfs가 start에서 end까지의 시간
    -  O(6*n): 동, 서, 남, 북, 좌, 우를 돌면서 탐색하는시간
- 공간복잡도: O(n^3)
    - building이 3차원이므로
    
# 4. 효율성증가를 위한 방법
# 5. 실수한것 & 복기할것
```
1. start, end계산
    - 한줄에 start와 end가 동시에 나오는경우를 생각못함
2. visit위치
    - queue에서 pop한후 넣으면 하나씩 방문체크되기때문에 시간이 오래걸림
    - 다음위치 계산할때 visit을 넣어야함
```