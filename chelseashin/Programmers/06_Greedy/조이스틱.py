def solution(name):
    # 상하 조정으로 알파벳 바꾸기 - 각 자리마다 빨리 목표 알파벳까지 도달하는 횟수
    info = [min(ord(n)-ord('A'), ord('Z')-ord(n)+1) for n in name]
    answer = 0
    # print(info)
    idx = 0         # 현재 커서 위치
    while True:
        answer += info[idx]
        info[idx] = 0
        if sum(info) == 0:
            return answer
        # print(info)
        # 좌우 이동방향 정하기- 더 가까운 쪽으로 선택
        left, right = 1, 1
        while info[idx-left] == 0:
            left += 1
        while info[idx+right] == 0:
            right += 1
        # 위치 인덱스 조정
        if left < right:
            answer += left
            idx += -left
        else:
            answer += right
            idx += right

print(solution("JEROEN"))
# print(solution("JAN"))
# print(solution("JAZZ"))


# def solution(name):
#     answer = 0
#     name = list(name)
#     N = len(name)
#     raw = ['A'] * N
#     idx = 0
#     while True:
#         right_idx = 1
#         left_idx = 1
#         if name[idx] != 'A':
#             if ord(name[idx]) - ord("A") >= 13:
#                 answer += 26-((ord(name[idx])) - ord("A"))
#             else:
#                 answer += ord(name[idx]) - ord("A")
#             name[idx] = "A"
#         if name == raw:
#             break
#         else:
#             for i in range(1, N):
#                 if name[idx+1] == "A":
#                     right_idx += 1
#                 else:
#                     break
#                 if name[idx-i] == "A":
#                     left_idx += 1
#                 else:
#                     break
#             if right_idx > left_idx:
#                 answer += left_idx
#                 idx -= left_idx
#             else:
#                 answer += right_idx
#                 idx += right_idx
#     return answer