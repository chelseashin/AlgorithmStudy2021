# 걸린시간 1시간
import sys
import re
from collections import deque
input = sys.stdin.readline

OPERATOR_PRIORITY = {'/':2, '*':2, '+':1, '-':1}

def eval(num1, num2, operator):
    if operator == '/':
        return int(num1 / num2)
    elif operator == '*':
        return num1 * num2
    elif operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    return None


def last_remove(numbers, op, result):
    numbers.pop()
    numbers.pop()
    op.pop()
    numbers.append(result)


def first_remove(numbers, op, result):
    numbers.popleft()
    numbers.popleft()
    op.popleft()
    numbers.appendleft(result)
    

def calc(numbers, op):
    while len(numbers) > 1:
        #print(numbers, op)
        f_num1, f_num2 = numbers[0], numbers[1]
        l_num1, l_num2 = numbers[-2], numbers[-1]
        f_op = op[0]
        l_op = op[-1] 
        f_result = eval(f_num1, f_num2, f_op)
        l_result = eval(l_num1, l_num2, l_op)
        if OPERATOR_PRIORITY[f_op] == OPERATOR_PRIORITY[l_op]:
            if f_result < l_result:
                last_remove(numbers, op, l_result)
            else:
                first_remove(numbers, op, f_result)
        elif OPERATOR_PRIORITY[f_op] > OPERATOR_PRIORITY[l_op]:
            first_remove(numbers, op, f_result)
        else:
            last_remove(numbers, op, l_result)
    return numbers.pop()


def input_values():
    raw_str = input().rstrip()
    operator = deque(re.compile('(\/|\*|-|\+)').findall(raw_str))
    numbers = deque(list(map(int, 
                    re.compile('(^-*[0-9]+|[0-9]+)').findall(raw_str))))
    return numbers, operator


def main():
    numbers, operator = input_values()
    result = calc(numbers, operator)
    print(result)

if __name__ == "__main__":
    main()