def dfs(count, start):
    result = list()
    if len(count) == 7:
        print(count)
        result.append(sum(count))
        return result
    else:
        for i in range(start, 25):
            if len(count) <= 0 or count[-1] < i:
                count.append(i)
                result.extend(dfs(count,start+1))
                #print("result", result)
                count.pop()
        return result
print(dfs([], 0))
