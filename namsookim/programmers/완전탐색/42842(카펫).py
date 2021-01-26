# https://programmers.co.kr/learn/courses/30/lessons/42842
# 6:00 시작
# 6:36 끝
"""
1. brown+yellow 개수가 총 칸의 개수가 된다.
2. 만들 수 있는 행,열의 모든 경우의 수를 구했다.
3. brown을 칠하면서 개수를 세주었다.
4. brown 개수와 칠한 brown 개수를 비교하여 같으면 True 반환, 다르면 False 반환

"""
def find(brown,yellow):
    pos = []
    total = brown+yellow
    #a ,b= 0,0
    for i in range(1,total+1):
        if total%i == 0:
            a = total//i
            b = i
            # a가 같거나 큼
            if a<b:
                break
            pos.append((a,b))

    #print(pos)
    return pos

def print_array(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j],end=' ')
        print()

def possible(a,b,brown,yellow):

    array = [[0]*b for _ in range(a)]

    # 갈색 색칠
    cnt = 0
    for i in range(len(array[0])):
        array[0][i] = 1 # 갈색은 1 # 위에 색칠
        array[len(array)-1][i] = 1  # 가장 아래 색칠
        cnt += 2

    for i in range(1,len(array)-1):
        array[i][0] = 1 # 첫째 열
        array[i][len(array[0])-1] = 1 # 마지막 열
        cnt += 2

    if cnt == brown:
        return True
    else:
        return False
    #print_array(array)

def solution(brown,yellow):

    # 10, 2 들어왔으면 총 12
    # a*b = 12가 되는 모든 경우의 수를 구하기
    find_ab=find(brown,yellow)

    # 경우의 수 돌리기
    for a,b in find_ab:
        #a*b 만들어서 보내기
        if possible(a,b,brown,yellow):
            return [a,b]

print(solution(24,24))