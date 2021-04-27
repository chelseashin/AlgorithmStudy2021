def get_result(semi_result, result):
    for i in list(semi_result.keys()):
        result[i] = result.get(i, 0) + 1
    return result


def is_go(i, length):
    if i < 0:
        return False
    if i >= length:
        return False
    return True


def is_left_balloon(value, a, is_max):
    result = dict()
    if len(a) <= 1:
        if a[0] == value:
            result[True] = 1
        else:
            result[False] = 1
        #print(a, result)
        return result
    
    for i in range(len(a)):
        for di in [-1, 1]:
            next_i = i + di
            if not is_go(next_i, len(a)):
                continue
            if a[next_i] >= a[i]:
                removed_value = a[next_i]
                del a[next_i]
                semi_result = is_left_balloon(value, a, is_max)
                result = get_result(semi_result, result)
                
                a.insert(next_i, removed_value)   
            if not is_max and a[next_i] < a[i]:
                is_max = True
                removed_value = a[next_i]
                del a[next_i]
                semi_result = is_left_balloon(value, a, is_max)
                result = get_result(semi_result, result)
                a.insert(next_i, removed_value)
                is_max = False
    return result
                

def solution(a):
    answer = 0
    for i, value in enumerate(a):
        result = is_left_balloon(value, a, False)
        if result[True] > 0:
            answer += 1
        #set_result = set(result)
        #print(set_result)
        #if True in set_result:
        #    answer += 1
    return answer