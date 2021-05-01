# 문제의 핵심
- 구현 문제
- 조건에 따라 얼마나 정확하고 빠르게 문제를 해결하는가?
- 걸린 시간: 2시간
# 알고리즘
1. 친한 친구가 가장 많은것계산
2. 빈자리가 많은것을 계산
3. 만족도 계산
# 사용 자료구조
1. 학생들 좌석: 2차원 배열
2. 학생정보와 선호도: dict내 dict ```{student:{1:True}}```
# 자주사용한 Code Snippet
```python
 for dr, dc in zip(DR, DC):
    arow = row + dr
    acol = col + dc
    if is_in_boundary(arow, acol, N) and maps[arow][acol] == 0:
        zero_count += 1
if max_zero_seat == zero_count:
    zero_seat.append((row, col))    
elif max_zero_seat < zero_count:
    max_zero_seat = zero_count
    del zero_seat
    zero_seat = [(row, col)]
```
# 추정 복잡도
1. 시간복잡도: O(8N^4)
    - 실제시간: 276ms
    - O(N^2): 행렬을 모두 순회함
    - O(2N^2): 입력된 학생수(N*N) 만큼 순회함
    - O(4N): 상하좌우 순회
2. 공간복잡도: O(2N^4)
    - 실제시간: 28776 kB
    - O(N^2): 학생들좌석
    - O(N^2): 학생 선호도
# 빠르게 푼사람 코드
# 복기할 부분
1. 왜 2시간이나 소요되었나?
    - 사용 자료구조를 계속 바꿈
        - searchs: list, list => searchs: list, dict, => searchs: dict, dict
    - 실수많이 함
1. 실수한부분
    - max_prefer_student, prefer_seat이 반복문 밖에있었음
        - global한 prefer_student가 계속 저장되어 반복문내 preferstudent가 반복되지 않음!
    - 이미 자리채워진부분은 넘어가야함
2. 비효율적인 부분을 어떻게 처리할것인가?