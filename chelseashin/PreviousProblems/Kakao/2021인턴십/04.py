def dfs(cur, start, end, check, time, traps, curInfo):
    check[start] = 1
    # for nx in curInfo[cur]:
    #     if check[nx]:

def solution(n, start, end, roads, traps):
    answer = 0
    disInfo = dict()
    connectInfo = dict()
    reverseInfo = dict()
    for p, q, s in roads:
        if (p, q) not in disInfo.keys():
            disInfo[(p, q)] = s
        else:
            if disInfo[(p, q)] > s:
                disInfo[(p, q)] = s
        if (q, p) not in disInfo.keys():
            disInfo[(q, p)] = s
        else:
            if disInfo[(q, p)] > s:
                disInfo[(q, p)] = s
        if p not in connectInfo.keys():
            connectInfo[p] = [q]
        else: connectInfo[p].append(q)
        if q not in reverseInfo.keys():
            reverseInfo[q] = [p]
        else: reverseInfo[q].append(p)

    print("disInfo", disInfo)
    print("connectInfo", connectInfo)
    print("reverseInfo", reverseInfo)
    check = [0] * n
    min_time = float('inf')
    dfs(start, start, end, check, 0, set(traps), connectInfo)
    return answer

print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))