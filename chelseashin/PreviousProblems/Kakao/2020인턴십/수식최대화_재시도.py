from itertools import permutations

def calc(expression, priority):
    new_expression = []
    for exp in expression:
        print("exp", exp, exp.split(priority[1]))
        # try:
        #     new_expression.append(eval(exp.split(priority[1])))
        # except:
        #     new_expression.append(exp)
    print(expression, "new_expression", new_expression)
    return 100 

def solution(expression):
    answer = 0
    print(type(expression), expression)
    for priority in permutations("+-*", 3):
        print(priority)
        new_expression = expression.split(priority[-1])
        print("new_expression", new_expression)
        answer = max(answer, calc(new_expression, priority))
        print()
    return answer

print(solution("100-200*300-500+20"))
# print(solution("50*6-3*2"))