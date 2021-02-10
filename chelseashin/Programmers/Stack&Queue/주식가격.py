prices = [1, 2, 3, 2, 3]

def solution(prices):
    answer = []
    N = len(prices)
    for i in range(N):
        temp = 0
        for j in range(i+1, N):
            if prices[i] > prices[j]:
                temp += 1
                break
            temp += 1
        answer.append(temp)
    return answer

print(solution(prices))