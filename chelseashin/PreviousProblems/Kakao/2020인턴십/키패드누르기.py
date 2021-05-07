# 13:40 start
# 14:01 finish
def solution(numbers, hand):
    answer = ''
    left = {1:(0, 0), 4:(1, 0), 7:(2, 0)}
    right = {3:(0, 2), 6:(1, 2), 9:(2, 2)}
    middle = {2: (0, 1), 5:(1, 1), 8:(2, 1), 0:(3, 1)}
    lr, lc, rr, rc = 3, 0, 3, 2

    for num in numbers:
        if num in left.keys():
            answer += "L"
            lr, lc = left[num]
        elif num in right.keys():
            answer += "R"
            rr, rc = right[num]
        else:
            mr, mc = middle[num]
            ldis = abs(lr-mr)+abs(lc-mc)
            rdis = abs(rr-mr)+abs(rc-mc)
            if ldis > rdis:
                answer += "R"
                rr, rc = mr, mc
            elif ldis  < rdis:
                answer += "L"
                lr, lc = mr, mc
            else:                
                if hand == "left":
                    answer += "L"
                    lr, lc = mr, mc
                elif hand == "right":
                    answer += "R"
                    rr, rc = mr, mc
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))