def dfs(N):
    def recursive(visited, start, end, left_visited):
        result = 0
        if left_visited == 0:
            print(start, end)
            return 1
        else:
            for nstart in range(start+1, N):
                for nend in range(nstart+1, N):
                    if nend - nstart > 0 and (nend - nstart) % 2 !=0:
                        if (start == -1 and end == -1) or (nend < end and nstart > start) or (nend < end and nstart < start):
                            print("before",visited)
                            if not visited[nstart] and not visited[nend]:
                                visited[nstart] = True
                                left_visited -= 1
                                visited[nend] = True
                                left_visited -= 1
                                print("going", nstart, nend)
                                result += recursive(visited, nstart, nend, left_visited)
                                print("after", visited)
                                visited[nstart] = False
                                left_visited += 1
                                visited[nend] = False
                                left_visited += 1
                                print("result", visited)
            return result
    return recursive



def main():
    N = int(input())
    result = dfs(N)
    visited = [False for _ in range(N)]
    start, end = 0, N-1
    print(result(visited, -1, -1, N))


if __name__ == "__main__":
    main()