# 문제의 핵심
- 시뮬레이션
- 얼마나 빠른시간내에 문제를 풀 수 있는가?
# 알고리즘
1. cloud 움직이기
2. 물복사하기
3. 새로운 비구름 만들기
# 사용 자료구조
1. grid: 2차원 배열
2. cloud: list 내 list ==> dict 내 튜플
# 자주사용한 Code Snippet
```python
def move_cloud(d, s, clouds, N):
    global grid
    new_clouds = dict()
    for x, y in list(clouds.keys()):
        # 다음으로 옮기기 
        first = (x + N + DR[d-1] * s) % N
        second = (y + N + DC[d-1] * s) % N
        new_clouds[(first, second)] = True
        grid[first][second] += 1
    return new_clouds
```
# 추정시간복잡도
- 시간복잡도: O(N^2*M) 순회시간 * M번 비바람이 부는시간
- 공간복잡도: O(N^2*cloud) board의 크기 * cloud크기
# 빠르게푼사람 코드
- list comprehension
```python
board = [list(map(int, input().split())) for _ in range(N)]
```
# 복기할 부분
- 시간초과나서 여러번 고쳤다..
- pythonic하게 만들줄알아야 성능을 높일 수 있을것같다..
- 리스트는 느리다. 웬만하면 set 혹은 dictionary로 접근한다.
- 잠깐 행복했던것같다... 문제를 다시 푸니 시간초과로 떨어질것같다. 