# 거의 1시간 반..? 소요ㅠㅠ

from itertools import permutations

def calc(expression, priority):
    for i in range(len(expression)):
        expression[i] = expression[i].split(priority[1])
    new_expression = []
    for i in range(len(expression)):
        temp = []
        for e in range(len(expression[i])):
            if priority[0] in expression[i][e]:
                temp.append(str(eval(expression[i][e])))
                continue
            temp.append(expression[i][e])
        new_expression.append(temp)

    expression = []
    for i in range(len(new_expression)):
        if len(new_expression[i]) > 1:
            expression.append(str(eval(priority[1].join(new_expression[i]))))
            continue
        expression.append(new_expression[i][0])
    return abs(eval(priority[-1].join(expression)))

def solution(expression):
    answer = 0
    for priority in permutations("+-*", 3):
        new_expression = expression.split(priority[-1])
        answer = max(answer, calc(new_expression, priority))
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))