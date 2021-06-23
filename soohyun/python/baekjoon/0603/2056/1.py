def solution(num ,percent):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    stack = list()
    visitied = list()
    stack.append((0,0,num,1,[(0,0)]))
    visitied.append((0,0))
    answer=0
    while stack:
        x,y,count,per, path = stack.pop()
        if count == 0:
            answer+=per
            continue
        for i in range(4):
            mx = x+dx[i] ; my = y+dy[i]
            if (mx,my) not in path:
                stack.append((mx,my,count-1,per*percent[i],path+[(mx,my)]))
    return answer
def main():
    NUM, PE, PW, PS, PN = map(int,input().split())
    percent = [PE/100, PW/100, PS/100, PN/100]
    if NUM == 0:
        print(1)
    else:
        print(solution(NUM, percent))

main()