# 1. 핵심
# 2. 걸린시간
 * 문제 해석 시간: 1시간 30분
 * 계획 시간: 1시 40분 ~ 2시 40분 1시간
 * 코딩 시간: 1시간
 * 디버깅 시간: 2시간
 * 수정 제출 시간: 

# 3.  알고리즘


## 3.1 can_shoot
```python
    global DIED
    diclist = [] # 죽은 적들
    for i in range(row-1, 0, -1):
        for j in range(mapcol): # col이 0부터 
            if map[i][j] == 1:  # 살아있다면
                length = attack_len(row, col, i, j) # 공격가능 거리인지 체크
                if length <= attack_dist: # 공격가능거리라면
                    diclist.append((length, j, i)) #죽이는애들 모두 넣음
    if diclist: # 죽이는애들이 있다면
        diclist.sort() # 정렬해서
        DIED.append((diclist[0][2], diclist[0][1])) #죽임
        return True
    return False
```
## 1.2 start_game
```python
   ef start_game(row, col, attack_dist):
    global MAP
    global DIED
    archers = [i for i in range(0, col)] 
    archer_case = list(combinations(archers, 3)) #archer 조합
    shoot_count = 0
    result = 0
    max_result = 0
    for item in archer_case: #archer의 모든 경우에수
        result = 0
        maps = deepcopy(MAP)
        for archer_row in range(row+1, 1, -1): # 범위까지
            for archer_col in item:  # 세명이 동시에 적에 화살을 쏜다.
                if shoot_count < 3:
                    # 쏠 수 있으면
                    if can_shoot(maps, archer_row, archer_col, attack_dist, col):
                        # shoot count를 하나 증가시킨다.
                        shoot_count += 1

            shoot_count = 0
            for enemy in DIED: # shoot하면서 죽인애들을
                if maps[enemy[0]][enemy[1]] == 1: # 왼쪽에서 하나씩 감소시킨다.
                    result += 1
                    maps[enemy[0]][enemy[1]] = 0
            DIED = []
            if max_result < result: #최대로 죽은애들이 result보다 작다면
                max_result = result
    return max_result #최대로 죽인애들을 반환한다.

```
### 1.2.1 거리별로 공격
```python
def attack_len(r1, c1, r2, c2): # 맨하탄거리
    return abs(r1-r2) + abs(c1-c2)

```

# 3. 추측 시간 복잡도 및 공간 복잡도
```
1. 시간복잡도: O(n^+nlogn)
    - O(n + logn): combination 만큼 반복
    - O(n): 행개수 만큼 반복
2. 공간복잡도: On(n^2)
    - O(n^2): 가장 큰 공간을 차지하는것은 MAP으로 간주
```
# 4. 실수한것 & 복기할것
```
1. 왼쪽지우는것을 너무 어렵게 생각했다. 
    - 확인은안되지만 heapq에서 가장 작은 적을 지우는것이 틀릴것이라 예상
2. 함수별로 쪼개서 좀더 **쉽게** 문제를 해결하는 법을 키워야한다.
```