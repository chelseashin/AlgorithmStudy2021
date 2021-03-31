# 12:00 start
# 13:00 95%에서 틀렸습니다..?

from sys import stdin
input = stdin.readline
from itertools import combinations

N, K = map(int, input().split())
if K < 5:
    print(0)

elif K == 5:
    MAX = 0
    for _ in range(N):
        word = input().rstrip()
        if len(word) == 8:
            MAX += 1
    print(MAX)

elif K == 26:   # 모든 단어 읽을 수 있음
    print(N)

else:
    alphabet = [0] * 26
    for char in "acint":
        alphabet[ord(char) - ord("a")] = 1
    check = 5
    words = []
    checkSet = set()
    for _ in range(N):
        word = input().rstrip()[4:-4]
        remain = set()
        for w in word:
            if alphabet[ord(w) - ord("a")]:
                continue
            remain.add(w)
            checkSet.add(w)
        words.append(remain)
    # print(words, K-check)
    if not checkSet:        # 검사할 단어 없으면 모든 단어 읽을 수 있음
        print(N)
    else:
        MAX = 0
        for pick in range(K-check, 0, -1):
            # print("pick", pick)
            for comb in combinations(checkSet, pick):
                # print(comb, "comb")
                comb = set(comb)
                result = 0
                for idx in range(N):
                    if not (words[idx] - comb):      # 단어 다 읽으면
                        result += 1
                MAX = max(MAX, result)
                # print(comb, "뽑을 때 읽은 단어", result)
            if MAX:         # 갱신된 적 있으면
                break
        print(MAX)