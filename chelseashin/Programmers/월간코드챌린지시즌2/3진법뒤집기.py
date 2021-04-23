def solution(n):
    result = ""
    while n:
        result += str(n % 3)    # 나머지
        n //= 3                 # 몫
    # print(result)
    
    # answer = 0
    # for i in range(len(result)):
        # answer += int(result[len(result)-1-i]) * 3**i
    # return answer

    return int(result, 3)   # 3진법 함수 사용한 한 줄 리턴

print(solution(45))
print(solution(125))