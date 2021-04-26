import sys
#시작 8시 25분
#끝 9시 49분
# 점화식
# v[i][0] = min(v[i-1][j+1]+v[i][0], v[i-1][j+2]+v[i][0])
# v[i][1] = min(v[i-1][j-1]+v[i][1], v[i-1][j+1]+v[i][1])
# v[i][2] = min(v[i-1][j-2]+v[i][2], v[i-1][j-1]+v[i][2])
def main():
    N = int(sys.stdin.readline())
    road = list()
    for idx in range(N):
        road.append(list(map(int, sys.stdin.readline().split(" "))))
    
    for i in range(1, N):
        road[i][0] = min(road[i-1][1]+road[i][0], road[i-1][2]+road[i][0])
        road[i][1] = min(road[i-1][2]+road[i][1], road[i-1][0]+road[i][1])
        road[i][2] = min(road[i-1][0]+road[i][2], road[i-1][1]+road[i][2])
    print(min(road[N-1]))

if __name__ == "__main__":
    main()