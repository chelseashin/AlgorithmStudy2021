# https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3

"""
1. 정렬 시간복잡도: O(NlogN)
2. 정렬하면 문자열 기준으로 '123' , '1234' , '5', '567' 이런식으로 정렬된다.
3. 값 2개 있을 때 만약 접두사가 가능하다면 무조건 뒤에쪽 문자열이 더 길다.
4. 앞뒤 비교해가면서 값이 있으면 False 리턴, 조건만족 안하면 True 리턴
"""

def solution(phone_book):
    answer = True
    phone_book.sort()
    #print(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            answer = False
            return answer

    return answer


phone = list(input().split())

print(solution(phone))

# 119 97674223 1195524421