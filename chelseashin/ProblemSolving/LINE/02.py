# 20:00 start
# 21:00 finish

from collections import deque
def solution(ball, order):
    result = []
    ball = deque(ball)
    pq = deque()
    for num in order:
        # 현재 값과 ball의 맨앞, 맨뒤 값 비교
        if ball[-1] == num:
            result.append(ball.pop())
        elif ball[0] == num:
            result.append(ball.popleft())
        else:
            pq.append(num)

        # 매 번호 비교 끝날 때마다 우선순위 큐 탐색하며 맨앞, 맨뒤 값 비교
        while pq and ball:
            qlen = len(pq)
            flag = False
            for _ in range(qlen):
                x = pq[0]
                if ball[-1] == x:
                    result.append(ball.pop())
                    flag = True
                elif ball[0] == x:
                    result.append(ball.popleft())
                    flag = True
                else:
                    pq.append(pq.popleft())
            if not flag:    # 같은 값 없으면 반복문 나가기
                break

    return result

print(solution([1, 2, 3, 4, 5, 6], [6, 2, 5, 1, 4, 3]))
print(solution([11, 2, 9, 13, 24], [9, 2, 13, 24, 11]))