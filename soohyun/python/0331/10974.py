import sys
def permutation(data, N, visited):
    if len(data) == N:
        print(*data)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            data.append(i+1)
            permutation(data, N, visited)
            data.pop()
            visited[i] = False
        
def main():
    N = int(sys.stdin.readline())
    visited = [False] * N
    permutation([], N, visited)

if __name__ == "__main__":
    main()