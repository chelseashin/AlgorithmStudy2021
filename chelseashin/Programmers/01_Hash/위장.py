clothes = [["yellow_hat", "headgear"],
           ["blue_sunglasses", "eyewear"],
           ["green_turban", "headgear"]]

def solution(clothes):
    D = {}
    for name, kind in clothes:
        if kind not in D.keys():
            D[kind] = 1
        else:
            D[kind] += 1
    # print(D)
    temp = 1
    for v in D.values():
        temp *= (v+1)
    # 아예 아무것도 입지 않은 경우도 포함돼있기 때문에 -1 해줌
    return temp-1

print(solution(clothes))