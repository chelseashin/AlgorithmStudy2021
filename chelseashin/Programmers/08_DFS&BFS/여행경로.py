# 21:30 start
# 22:00 제출 but, 2 pass 2 fail
# finish

# def dfs(start, check, tickets, answer, N):
#     # global answer
#     candidates = []
#     for idx, city in enumerate(tickets):
#         # print(idx, city)
#         if start == city[0]:
#             candidates.append((city[1], idx))
#     candidates.sort()
#     # print(sorted(candidates))
#     for n, i in candidates:
#         if check[i]:
#             continue
#         check[i] = 1
#         answer.append(n)
#         dfs(n, check, tickets, answer, N)
#
# def solution(tickets):
#     global answer
#     answer = ["ICN"]
#     N = len(tickets)
#     check = [0] * N
#     dfs("ICN", check, tickets, answer, N)
#     return answer

# 참고링크
# https://codingspooning.tistory.com/81
# https://jisun-rea.tistory.com/entry/python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level3-%EC%97%AC%ED%96%89%EA%B2%BD%EB%A1%9C-DFS
# https://copy-driven-dev.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-ProgrammersPython-%EC%97%AC%ED%96%89%EA%B2%BD%EB%A1%9C

def solution(tickets):
    path_info = dict()       # 티켓을 출발 - 도착 순으로 경로 딕셔너리 생성
    for start, destination in tickets:
        if start not in path_info.keys():
            path_info[start] = [destination]
        else:
            path_info[start].append(destination)

    for city in path_info.keys():
        path_info[city].sort(reverse=True)  # 알파벳 역순으로 정렬
    
    # 1번째 출발지는 "ICN"으로 고정
    stack = ["ICN"]
    answer = []
    while stack:
        start = stack[-1]
        # answer에 담겨질 때는 stack에 값이 꽉차고 path_info에 값이 없을 때이므로
        # answer에는 반대로 값이 들어가 있음
        if start not in path_info.keys() or not path_info[start]:
            answer.append(stack.pop())
        else:
            stack.append(path_info[start].pop())
        print(stack, answer)
    answer.reverse()
    return answer
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))