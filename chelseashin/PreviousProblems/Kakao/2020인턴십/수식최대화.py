from itertools import permutations

def calc2(op, num1, num2):
    print("op", op, num1, num2)
    return 999

def calc(expression, priority):
    print("priority", priority)
    stack = []
    idx = 0
    while idx < len(priority):
        op = priority[idx]
        print("op", op, stack)
        for ex in expression:
            print("ex", ex)
            if not stack:
                stack.append(ex)
            elif ex == "+" or ex =="-" or ex == "*":
                stack.append(ex)
            else:
                if stack and stack[-1] == op:
                    print("calc2 결과", calc2(stack.pop(), stack.pop(), ex))
        
        idx += 1

    return 100
    

def solution(expression):
    answer = 0
    operators = set()
    new_expression = []
    temp = ""
    for idx in range(len(expression)):
        if expression[idx] in {"+", "-", "*"} or idx == len(expression)-1:
            if idx == len(expression)-1:
                temp += expression[idx]
                new_expression.append(int(''.join(temp)))
            else:
                if temp:
                    new_expression.append(''.join(temp))
                operators.add(expression[idx])
                new_expression.append(expression[idx])
                temp = []
        else:
            temp += expression[idx]
    print("new_expression", new_expression)
    for priority in permutations(operators, len(operators)):
        answer = max(answer, calc(new_expression, priority))
    print()
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))