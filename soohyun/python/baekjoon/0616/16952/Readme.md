# 문제의 핵심
- bfs
- 우선순위 큐
- visited를 변형하는 문제
# 알고리즘
- count, queue, visited 선언
- 큐에 세가지 말을 heappush해서 넣음
- 큐는 빌때까지 아래를 반복함
    - 체스 숫자가 끝숫자에 도착했으면 count와 change_piece를 반환
    - 말만 바꾸는 경우
        - 말을 바꾼 경우에대해서 아직 방문하지 않았다면
        - (3가지 경우)에대해서 말바꿈 count 를 하나 더하고 큐에 저장
    - 말을 바꾸지 않는경우
        - 나이트인경우
            alpha값 없이 8군데진행
        - 나이트가아닌경우
            alpha값과 함께 4군데 진행 비숍 - 대각선 룩- 직진
        - 위의 두가지에대해서 범위체크후, 아직 방문하지 않았다면
            - 방문 표시한후에
            - 다음 목적지로 도착한경우
                - 숫자를 하나 더하고 진행
            - 다음 목적지로 도착하지 않은경우
                - count만 더하고 진행
# 자료구조
- visited: 4차원 dict
```python
   visited = {말:{숫자:(좌표)}}
   visited = {0:{1:(1,2)}, 1:{2:(1,2)}....}
```
- ChessInfo: 큐에넣을 노드객체
- 현재 말, 바꾼 말갯수, 현재위치, 현재 목적지까지의 걸린시간, 현재 말아래있는 숫자
```python
    def __init__(self, piece, change_piece_count,loc, count, number):
        self.piece = piece
        self.change_piece = change_piece_count
        self.loc = loc
        self.count = count
        self.number = number
    
```
# Code Snippet
```python
    def __lt__(self, other):
        if self.count <  other.count:
            return True
        elif self.count == other.count:
            return self.change_piece < other.change_piece
        else:
            return False
```
# 시간복잡도
- O((N * N) * Nlog(N)): 
    - 말판의 1~부터 N*N까지 반복하는 횟수 
    - Nlog(N) 우선순위 큐 push. pop 횟수
# 다른 코드
- comparable 이없는 코드
# 복기할것
- __lt__덕분에 어렵지 않게 풀 수 있었음
- comparable을 지원하지 않으면 어떻게 풀었을지 궁금함
- 여전히 나누는경우는 왜안되는지 궁금함..