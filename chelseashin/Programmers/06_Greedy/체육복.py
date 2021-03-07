# 16:00 start

def solution(n, lost, reserve):
    reserve_ = [r for r in reserve if r not in lost]
    lost_ = [l for l in lost if l not in reserve]
    for num in reserve_:
        if num+1 in lost_:
            lost_.remove(num+1)
        elif num-1 in lost_:
            lost_.remove(num-1)
    return n-len(lost_)


# 위와 같은 로직으로 Set으로 풀었는데 테케 1개 틀림.. 왜인지 아직도 이유 모르겠다.
# def solution(n, lost, reserve):
#     reserve_ = set(reserve) - set(lost)
#     lost_ = set(lost) - set(reserve)
#     for num in reserve_:
#         if num+1 in lost_:
#             lost_.discard(num+1)
#         elif num-1 in lost_:
#             lost_.discard(num-1)
#     return n-len(lost_)

print(solution(5, [2, 4], [1, 3, 5]))   # 5
print(solution(5, [2, 4], [3]))         # 4
print(solution(3, [3], [1]))            # 2
print(solution(5, [2, 3, 4], [1, 2, 3]))  # 4
print(solution(5, [1, 2, 3], [2, 3, 4]))  # 4
print(solution(5, [3, 1], [2, 3]))        # 5