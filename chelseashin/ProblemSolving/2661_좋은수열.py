# 15:00 start
# 16:12 틀렸습니다..
# 16:22 pass
# 1시간 22분 소요
# Backtracking
# 길이 1보다 큰 temp에 대해(depth > 1)에 대해 부분수열이 동일한 것이 있다면 가지치기
# 길이가 N까지 처음으로 다다랐을 때, 값 출력하고 전역변수 flag를 True로 바꿈
# flag가 이미 True라면 더이상 볼 필요 없으므로 가지치기

def backtracking(depth, temp):
    global flag
    if flag:
        return
    if depth > 1:
        for length in range(depth//2):
            if temp[depth-2*length-2:depth-length-1] == temp[depth-length-1:depth+1]:
                return
    if depth == N:
        flag = True
        print(int(temp))
        return
    for num in "123":
        backtracking(depth+1, temp + num)

N = int(input())
flag = False
backtracking(0, "")