import heapq

def is_boundary(lp, rp, N):
    if lp >= 0 and lp < N and rp >= 0 and rp < N:
        return True
    #print("False", lp, rp, N)
    return False


def len_buy_gem(buy_gems, gem, rp):
    return buy_gems.get(gem, 0) + 1


def len_gem(lp, rp):
    return rp - lp

def solution(gems):
    answer = [0, 1000001]
    size = len(set(gems))
    buy_gems = {gems[0]:1}
    start, end = 0, 0
    
    while is_boundary(start, end, len(gems)):
        #print(start, end, buy_gems)
        if len(buy_gems) < size:
            end += 1
            buy_gems[gems[end]] = buy_gems.get(gems[end], 0) + 1
        else:
            buy_gems[gems[start]] -= 1
            #print(start, buy_gems, len(buy_gems), size)
            if buy_gems[gems[start]] <= 0:
                buy_gems.pop(gems[start])
            '''
            else:
                if answer[1] - answer[0] > end - start:
                    answer = [start, end]
                elif answer[1] - answer[0] == end - start and answer[0] > start:
                    answer = [start, end]    
            '''
            start += 1
    return answer
        
print(solution('["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]'))