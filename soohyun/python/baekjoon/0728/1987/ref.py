import sys 
sys.setrecursionlimit(10000) 
def dfs(x, y, cnt): 
    #print(x, y, cnt)
    dx = [1, -1, 0, 0] 
    dy = [0, 0, 1, -1] 
    now = (x, y) 
    global ans 
    ans = max(ans, cnt) 
    for i in range(4): 
        nx = now[0] + dx[i] 
        ny = now[1] + dy[i] 
        if(0 <= nx < R) and (0 <= ny < C): 
            if(done[strings[nx][ny]] == 0): 
                done[strings[nx][ny]] = 1 # print(done) 
                dfs(nx, ny, cnt+1) 
                done[strings[nx][ny]] = 0 #백트래킹 
R, C = map(int, input().split()) 
strings = [list(map(lambda x: ord(x)-65, input())) 
for _ in range(R)] # 아스키 코드로 바꿔줌 
done = [0]*26 # 알파벳 26개만큼 배열설정 
done[strings[0][0]] = 1 
ans = 1 
dfs(0, 0, ans) 
print(ans)

