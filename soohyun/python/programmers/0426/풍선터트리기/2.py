def solution(a):
    if len(a) >= 3:
        answer = 2
        last = len(a)
        for i in range(1, last-1):
            if a[i] <= min(a[0:i]) or a[i] <= min(a[i+1:last+1]):
                answer += 1
        return answer
    else:
        return len(a)