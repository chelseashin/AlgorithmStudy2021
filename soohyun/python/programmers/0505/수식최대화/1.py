num_list, op_list = list(), list()
ops = set()


def calc(num_1, num_2, op):
    if op == '-':
        return num_1 - num_2
    elif op == '*':
        return num_1 * num_2
    else:
        return num_1 + num_2
    
def make_post_prefix(pri_list):
    global ops, num_list, op_list
    
    priority = dict()
    result = []
    op_stack = []
    for idx, op in enumerate(ops):
        priority[op] = pri_list[idx]
    
    for idx, value in enumerate(num_list):
        result.append(value)
        # print(op_stack)
        if idx >= len(op_list):
            continue
        if len(op_stack) > 0:
            print(op_stack[-1], priority[op_stack[-1]], op_list[idx], priority[op_list[idx]])
        if len(op_stack) <= 0 or priority[op_stack[-1]] < priority[op_list[idx]]: 
            op_stack.append(op_list[idx])
        elif priority[op_stack[-1]] >= priority[op_list[idx]]:
            while len(op_stack) > 0 and priority[op_stack[-1]] >= priority[op_list[idx]]:
                result.append(op_stack.pop())
            op_stack.append(op_list[idx])
            
    while len(op_stack) > 0:
        result.append(op_stack.pop())
    return result


def make_number(pri_list):
    global ops, num_list, op_list

    stack = []
    post_prefix = make_post_prefix(pri_list)
    print(post_prefix)
    for value in post_prefix:
        #print(stack)
        if value in {'-', '+', '*'}:
            num_2 = int(stack.pop())
            num_1 = int(stack.pop())
            stack.append(calc(num_1, num_2, value))
        else:
            stack.append(value)
    #print(abs(stack[0]))
    return abs(stack[0])
    #return stack[0]
            

def dfs(pri_list, visited):
    global ops, num_list, op_list
    max_result = 0
    if len(pri_list) >= len(ops):
        result = make_number(pri_list)
        return result
    else:
        for i in range(len(ops)):
            if not visited.get(i, False):
                visited[i] = True
                pri_list.append(i)
                result = dfs(pri_list, visited)
                if max_result < result:
                    max_result = result
                pri_list.pop()
                visited.pop(i)
        return max_result

def solution(expression):
    global ops, num_list, op_list
    number_tmp = ''
    # 숫자 - 연산자 나누어 dict로 만들기
    for alpha in expression:
        if alpha in {'-', '*', '+'}:
            ops.add(alpha)
            num_list.append(int(number_tmp))
            op_list.append(alpha)
            number_tmp = ''
        else:
            number_tmp += alpha
    num_list.append(int(number_tmp))
    #print(num_list, op_list)
    # 숫자 조합 combination
    return dfs([], dict())
    # max값 찾기
    
    #return answer