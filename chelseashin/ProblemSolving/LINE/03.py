# 21:10 start
# 22:02 finish

def dfs(depth, N, temp):
    global min_depth, min_value
    if depth > min_depth:       # 가지치기
        return

    if len(temp) == 1:
        # print(depth, temp)
        if min_depth > depth:   # 최소 depth 갱신
            min_depth = depth
            min_value = int(temp)
        return

    for i in range(1, N):
        if len(temp[i:]) > 1 and temp[i:][0] == "0":    # 맨 앞자리수가 0이면 넘기기
            continue
        left = int(temp[:i])
        right = int(temp[i:])
        result = str(left + right)
        # print(left, right, "==>", result)
        dfs(depth+1, len(result), result)

def solution(n):
    global min_depth, min_value
    if len(str(n)) == 1:
        return [0, n]
    else:
        min_depth = float('inf')
        min_value = float('inf')
        dfs(0, len(str(n)), str(n))
        return [min_depth, min_value]

print(solution(73425))
print(solution(10007))
print(solution(9))
print(solution(100000))
print(solution(1123456789))