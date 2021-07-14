A, B, C = map(int, input().split())
ls = [0] * 21
for _ in range(int(input())):
    i, e = map(int, input().split())
    ls[i] = e

cnt, res = 0, 0
for i in range(20, -1, -1):
    cnt <<= 3
    tmp = (A >> i) * (B >> i) * (C >> i) - cnt
    res += min(ls[i], tmp)
    cnt += min(ls[i], tmp)
if cnt == A * B * C:
    print(res)
else:
    print(-1)