#시작:  1시 36분
#끝: 2시 19분
def check_wait(wait, ball, result, index_order):
    if index_order == 1:
        start_index = 0
    else:
        start_index = index_order
    while len(wait) > 0 and wait.get(ball[start_index]) == True:
        result.append(ball[start_index])
        wait.pop(ball[start_index])
        start_index += index_order
    return wait, result


def solution(ball, order):
    result = list()
    wait = dict()
    for index, order_ball in enumerate(order):
        if ball[0] == order_ball:
            result.append(ball.pop(0))
            wait, result = check_wait(wait, ball, result, 1)
        elif ball[-1] == order_ball:
            result.append(ball.pop())
            wait, result = check_wait(wait, ball, result, -1)
        else:
            wait[order_ball] = True
    return result

print(solution([1, 2, 3, 4, 5, 6], [6, 2, 5, 1, 4, 3]))
print(solution([11, 2, 9, 13, 24],	[9, 2, 13, 24, 11]))