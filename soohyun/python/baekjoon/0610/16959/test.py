import sys
import math
import temp


def make_table(arr, N):
    table = dict()
    for i, value in enumerate(arr):
        table[value+1] = (i // N, i % N)
    return table


def print_table(table, num):
    print("")
    for key, value in table.items():
        print(key, end=' ')
        if value[1] == num-1:
            print("")
    print("")



def dfs(num, cur_num, data, visited):
    if num == cur_num:
        print("==start==")
        table = make_table(data, int(math.sqrt(num)))
        print_table(table, int(math.sqrt(num)))
        temp.game(int(math.sqrt(num)), table)
        print("==end==")

    else:
        for i in range(0, num):
            if not visited.get(i, False):
                visited[i] = True
                data.append(i)
                cur_num += 1
                dfs(num, cur_num, data, visited)
                visited[i] = False
                cur_num -= 1
                data.pop()



def main():
    N = int(input())
    visited = dict()
    dfs(N*N, 0, [], visited)


if __name__ == "__main__":
    main()