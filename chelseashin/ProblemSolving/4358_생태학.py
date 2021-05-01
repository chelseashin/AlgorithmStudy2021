from sys import stdin
input = stdin.readline

# 풀이 1 - Set 사용 X
# nameInfo = dict()   # 나무 이름 등장 횟수
# cnt = 0
# while True:
#     name = input().strip()
#     if not name:
#         break
#     cnt += 1
#     if name not in nameInfo.keys():
#         nameInfo[name] = 1
#     else: nameInfo[name] += 1

# nameLst = sorted(list(nameInfo.keys()))     # 사전 순으로 정렬
# for name in nameLst:
#     if not name:
#         continue
#     print("%s %.4f"%(name, nameInfo[name] / cnt * 100))     # 소수 넷째 자리까지

# 풀이 2 - Set 사용
nameInfo = dict()   # 나무 이름 등장 횟수
nameSet = set()     # 중복 없앤 이름 리스트
cnt = 0
while True:
    name = input().strip()
    if not name:
        break
    if name not in nameInfo.keys():
        nameInfo[name] = 1
        nameSet.add(name)
    else: nameInfo[name] += 1
    cnt += 1

nameLst = sorted(list(nameSet))
for name in nameLst:
    print("%s %.4f"%(name, nameInfo[name] / cnt * 100))