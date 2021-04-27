# 시작 1시 24분
# 끝 1시 45분
def is_correct(s):
    stack = list()
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        else:
            if len(stack) > 0:
                if i == ')' and stack[-1] != '(':
                    return False
                if i == '}' and stack[-1] != '{':
                    return False
                if i == ']' and stack[-1] != '[':
                    return False
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    return False


def solution(s):
    answer = 0
    list_s = list(s)
    for i in range(len(s)):
        if is_correct(list_s):
            answer += 1
        arr = list_s.pop(0)
        list_s.append(arr)
    return answer