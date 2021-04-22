# 문제 : https://programmers.co.kr/learn/courses/30/lessons/76503
# 아이디어 : https://prgms.tistory.com/47?category=882795
# 18개 중 11개 성공, 7개 실패..ㅠㅠ
# 그리디로 접근

# 시작 리프 노드, 교환 횟수, 간선 정보
def greedy(start, a):
    global visited, edge_info
    # print("시작노드", start, a[start], "도착노드", edge_info[start])
    temp = 0
    temp += abs(a[start])
    a[edge_info[start][0]] += a[start]
    a[start] = 0
    visited[start] = 1
    edge_info[edge_info[start][0]].remove(start)
    del edge_info[start]
    # print("지운 후 상태", edge_info, "===== a =====", a, visited)
    # print(temp)
    # print()
    return temp

def solution(a, edges):
    global visited, edge_info
    if sum(a) != 0:     # 불가능한 경우
        return -1
    answer = 0
    edge_info = dict()
    for s, e in edges:
        if s not in edge_info.keys():
            edge_info[s] = [e]
        else: edge_info[s].append(e)
        if e not in edge_info.keys():
            edge_info[e] = [s]
        else: edge_info[e].append(s)
    # print("edge_info", edge_info)

    visited = [0] * len(a)
    while a.count(0) != len(a):
        for s in range(len(a)):
            if s not in edge_info.keys():
                continue
            if visited[s]: continue     # 이미 방문했으면 넘기기
            if len(edge_info[s]) == 1:
                visited[s] = 1
                if a[s] == 0:
                    edge_info[edge_info[s][0]].remove(s)
                    del edge_info[s]
                    continue      # 이미 0이면 넘기기
                # print("지우기 전 edge_info", edge_info, "===== a =====", a, visited)
                # print()
                answer += greedy(s, a)
    
    return answer

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))
print(solution([0,1,0], [[0,1],[1,2]]))

# 참고해보자
# https://sinawi.tistory.com/262?category=649580
# https://bladejun.tistory.com/120