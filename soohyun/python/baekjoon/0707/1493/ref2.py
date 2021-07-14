import sys
input = sys.stdin.readline

l, w, h = map(int, input().split())

n = int(input())
cube = [0] * 21
for _ in range(n) :
    i, cnt = map(int, input().split())
    if i > 20 : continue
    cube[i] = cnt

best = [0] * 21
best[0] = l * w * h
for bi in range(1, len(best)) :
    sz = 2 ** bi
    best[bi] = (l // sz) * (w // sz) * (h // sz)
    if best[bi] == 0 :
        bi -= 1
        break
    best[bi - 1] -= best[bi] * 8

ci = bi

ans = 0
while bi >= 0 and ci >= 0 :
    if bi > ci :
        best[bi - 1] += best[bi] * 8
        bi -= 1
    else :
        if best[bi] > cube[ci] :
            ans += cube[ci]
            best[bi] -= cube[ci]
        else :
            ans += best[bi]
            best[bi] = 0
            bi -= 1
        ci -= 1

print(ans if best[0] == 0 else -1)
