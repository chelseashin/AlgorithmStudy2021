# start 1시 22분
# end 1시 24분
def solution(absolutes, signs):
    answer = 0
    for i, value in enumerate(absolutes):
        if signs[i]:
            answer += value
        else:
            answer -= value
            
    return answer