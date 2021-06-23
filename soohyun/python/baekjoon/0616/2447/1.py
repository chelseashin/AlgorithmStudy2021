import sys
input = sys.stdin.readline
print = sys.stdout.write

def print_default():
    pass


def print_recursive(row, col, N, result):
    if (row//N%3, col//N%3) == (1, 1):
        result.append(" ")
        #print(" ")
    else:
        if N // 3 == 0:
            result.append("*")
            #print("*")
        else:
            result = print_recursive(row, col, N/3, result) 
    return result  

def main(): 
    N = int(input())
    for i in range(0, N):
        for j in range(0, N):
            result = []
            result = print_recursive(i, j, N, result)
            print("".join(result))
        print("\n")

if __name__ == "__main__":
    main()