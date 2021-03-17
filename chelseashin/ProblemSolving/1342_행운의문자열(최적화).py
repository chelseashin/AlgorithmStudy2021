from sys import stdin
input = stdin.readline

def dfs(depth, string):
    global N, ret, charSet, cntMap

    if depth == N:
        # print(string)
        ret += 1
        return

    for char in charSet:
        idx = ord(char) - ord('a')
        if cntMap[idx] == 0:
            continue

        if string and string[-1] == char:
            continue

        cntMap[idx] -= 1
        dfs(depth + 1, string + char)
        cntMap[idx] += 1


raw = input().strip()
cntMap = [0] * 26
N = len(raw)
ret = 0
charSet = set()

for char in raw:
    idx = ord(char) - ord('a')
    cntMap[idx] = cntMap[idx] + 1
    charSet.add(char)
# print(charSet, cntMap, cntSum)
dfs(0, '')
print(ret)