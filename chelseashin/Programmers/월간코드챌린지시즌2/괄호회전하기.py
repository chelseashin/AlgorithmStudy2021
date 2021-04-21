# 8분 소요
def solution(s):
    answer = 0
    for _ in range(len(s)):
        s = s[-1] + s[:-1]
        stack = []
        for x in s:
            if not stack:
                stack.append(x)
                continue
            if x == "]" and stack[-1] == "[":
                stack.pop()
            elif x == "}" and stack[-1] == "{":
                stack.pop()
            elif x == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(x)
        if not stack:
            answer += 1
    return answer

print(solution("[](){}"))