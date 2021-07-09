import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def find_min(N, graph):
    visited = [False for _ in range(N)]
    DP =[[0, 0] for _ in range(N)]
    def recursive(parent):
        visited[parent] = True
        DP[parent][1] = 1
        DP[parent][0] = 0
        for child in graph[parent]:
            if not visited[child]:
                recursive(child)
                DP[parent][0] += DP[child][1]
                DP[parent][1] += min(DP[child][0], DP[child][1])
                print("parent:",parent, "child:",child, DP)
        return DP
    return recursive

def input_values():
    num_node = int(input().rstrip())
    graph = [[] for _ in range(num_node)]
    #for i in range(num_node):
    #    graph[i] = list()
    for _ in range(num_node-1):
        u, v = map(int, input().rstrip().split(" "))
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    return graph, num_node

def main():
    graph, num_node = input_values()
    print(graph)
    result = find_min(num_node, graph)
    DP = result(0)
    print(DP)
    print(min(DP[0][0], DP[0][1]))

    

if __name__ == "__main__":
    main()