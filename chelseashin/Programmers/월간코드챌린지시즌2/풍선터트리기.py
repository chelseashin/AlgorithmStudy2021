# 20분 소요
# 시간초과 실패 코드..
# def solution(a):
#     answer = 0
#     for i in range(len(a)):
#         num = a[i]
#         left = 0
#         for n in a[:i]:
#             if n < num:
#                 left += 1
#         right = 0
#         for n in a[i+1:]:
#             if n < num:
#                 right += 1
#         print(num, a[:i], a[i+1:], "left", left, "right", right)
#         if left and right:
#             continue
#         answer += 1
#    return answer

# 풀이 2
# 핵심은 자신을 기준으로 왼쪽, 오른쪽에서 각각 반대 방향으로 갈 때
# 최솟값을 갱신할 수 있다면 살아남을 수 있다는 뜻! 
# 참고 풀이  : https://velog.io/@eehwan/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%92%8D%EC%84%A0-%ED%84%B0%ED%8A%B8%EB%A6%AC%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# def solution(a):
#     result = [0] * len(a)
#     minFront, minRear = float('inf'), float('inf')
#     for i in range(len(a)):
#         if a[i] < minFront:
#             minFront = a[i]
#             result[i] = 1
#         if a[-1-i] < minRear:
#             minRear = a[-1-i]
#             result[-1-i] = 1
#         print(result)
#     return sum(result)

# 풀이 3 - 위 코드보다 조금씩 더 빠름. answer로 답을 구하기 때문
# 참고 풀이 : https://coding-lks.tistory.com/44
def solution(a):
    minFront, minRear = float('inf'), float('inf')
    answer = 0
    for i in range(len(a)):
        if a[i] < minFront:     # 작은 수로 갱신하고 answer += 1
            minFront = a[i]
            answer += 1
        if a[-1-i] < minRear:
            minRear = a[-1-i]
            answer += 1
        # print(answer, minFront, minRear)
    #가장 작은 수를 기준으로 하는 경우 answer에 2번 더해지므로 1은 빼줌
    return answer-1

print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))