def solution(a):
    answer = -1
    one_count = dict()
    for col in range(len(a[0])):
        for row in range(len(a)):
            if a[row][col] == 1:
                if one_count.get(col, 0) == 0:
                    one_count[col] = 1
                else:
                    one_count[col] += 1
    print(one_count)
            
            
    return answer