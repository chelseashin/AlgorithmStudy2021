# 11:30 start
# 12:00 시간초과,,

from sys import stdin
input = stdin.readline

# 내 최초 풀이 - 시간초과,,
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     scores = [list(map(int, input().split())) for _ in range(N)]
#     result = N          # 합격자
#     for i in range(N):
#         for j in range(i+1, N):
#             if i == j:  # 자기 자신이면 비교 X
#                 continue
#             print((i, j))
#             if scores[i][0] > scores[j][0] and scores[i][1] > scores[j][1]:   # 둘다 서류, 면접 점수가 낮으면
#                 result -= 1
#                 # print((i, j), scores[i], scores[j])
#                 print(i, "지원자 탈락")
#                 # break 
#             if scores[i][0] < scores[j][0] and scores[i][1] < scores[j][1]:
#                 result += 1
#     print(result, "==========================================")
#     break

# 참고 : https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%801946%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%8B%A0%EC%9E%85-%EC%82%AC%EC%9B%90
# 참고 2 : https://velog.io/@sch804/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-1946%EB%B2%88-%EC%8B%A0%EC%9E%85-%EC%82%AC%EC%9B%90

T = int(input())
for _ in range(T):
    N = int(input())
    scores = [0] * (N)
    for _ in range(N):
        a, b = map(int, input().split())
        scores[a-1] = b           # 서류 점수 기준으로 오름차순 정렬
    # print("서류 점수 기준으로 정렬", scores)
    minScore = scores[0]        # 서류 1등의 면접 등수
    result = 1                  # 합격자
    for i in range(1, N):        # 서류 1등인 사람은 무조건 합격이므로 2등부터 확인
        if minScore > scores[i]:   # 더 높은 등수라면 갱신
            minScore = scores[i]
            result += 1            # 면접 등수가 이전의 최대 순위보다 높다면 합격 
            # print(i, "번 합격")
    print(result)