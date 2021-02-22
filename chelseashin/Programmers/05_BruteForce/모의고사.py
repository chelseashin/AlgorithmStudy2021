# 19:55 start
# 20:09 finish
# 14m 소요
# Brute Force
# 패턴 파악 후 저장
# 정답 주어지면 길이만큼 돌리며 정답이면 temp 배열에 수포자별로 점수 +1 해줌
# 가장 높은 점수를 받은 수포자들 번호를 배열에 담아 출력

def solution(answers):
    pattern = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    temp = [0] * 3
    for i, ans in enumerate(answers):
        if ans == pattern[0][i % 5]:
            temp[0] += 1
        if ans == pattern[1][i % 8]:
            temp[1] += 1
        if ans == pattern[2][i % 10]:
            temp[2] += 1
    max_score = max(temp)
    return [j+1 for j in range(3) if temp[j] == max_score]

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))