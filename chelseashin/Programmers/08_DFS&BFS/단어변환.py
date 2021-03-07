# 19:00 start
# 20:20 finish
# 50분 소요,, 혼자 고민하다가 다른 사람 풀이 보고 품
# dfs로 접근

# (시작 단어, 비교 단어, 단어의 길이)를 인자로 넣으면 두 단어의 다른 알파벳 갯수 리턴
def isDifferent(x, y, L):
    temp = 0
    for i in range(L):
        if y[i] != x[i]:
            temp += 1
            if temp > 1:    # 2개 이상 다르면 그냥 2 리턴
                return temp
    return 1

def dfs(begin, target, words, check, N, L):
    global answer
    stack = [begin]
    while stack:
        x = stack.pop()
        if x == target:     # 타겟 단어 만나면 depth 리턴
            return answer
        for next in range(N):
            # 조건 1. 한 개의 알파벳만 다른 경우
            y = words[next]
            if isDifferent(x, y, L) == 1:
                if check[next]:
                    continue
                check[next] = 1
                stack.append(y)
        answer += 1    # depth 개념

def solution(begin, target, words):
    global answer
    # 조건 2. words에 있는 단어로만 변환 가능
    if target not in words:
        return 0
    answer = 0
    N = len(words)
    L = len(begin)
    check = [0] * N
    dfs(begin, target, words, check, N, L)
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))