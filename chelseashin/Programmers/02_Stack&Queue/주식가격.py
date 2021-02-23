def solution(prices):
    answer = []
    N = len(prices)
    for i in range(N):
        temp = 0
        for j in range(i+1, N):
            temp += 1
            if prices[i] > prices[j]:   # 주식 가격 떨어지면 break
                break
        answer.append(temp)
    return answer

print(solution([1, 2, 3, 2, 3]))