# 11:37 시작
# 12:50 종료
"""
dictionary와 경우의수.

1. 먼저, dictionary를 만들어서 현재 dictionary에 해당 종류가 없으면 추가하고, 종류가 있으면 개수를 1 더해주었다.

2. dictionary에 값들을 하나씩 가져와서 1을 더해주고 계속 곱했다.
    2.1. 1을 더해주는 이유 = 옷을 안입는 경우를 포함
    2.2  마지막 결과값에 1을 빼주는 이유 = 모두 안입는 경우가 포함되니 -1

"""
def solution(clothes):

    dic = dict()

    for item, kind in clothes:
        if kind not in dic:
            dic[kind] = 1
        else:
            dic[kind] += 1
    answer = 1
    for value in dic.values():
        answer *= (value + 1) # 안입는 경우까지 +1

    return answer-1 # 모두 안입었을 경우는 경우의 수에서 제외

#print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"], ["crow_", "dark"], ["cro4", "dark"]]))
# [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
# [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"], ["crow_", "dark"], ["cro4", "dark"]]