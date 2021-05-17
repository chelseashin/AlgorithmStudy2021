import sys
from collections import deque
input = sys.stdin.readline


def solution(arr, str_A, str_B):
    max_x, max_y, value = 0, 0, 0
    for i in range(1, len(str_A)+1):
        for j in range(1, len(str_B)+1):
            if str_A[i-1] == str_B[j-1]:
                arr[i][j] = 1 + arr[i-1][j]
            else:
                #print(i, j, i-1, j)
                #print(arr[i-1][j])
                #print(arr[i][j-1])
                if arr[i-1][j] > arr[i][j-1]:
                    arr[i][j] = arr[i-1][j]
                else:
                    arr[i][j] = arr[i][j-1] 
                    
            if arr[i][j] > value:
                max_x, max_y, value = i, j, arr[i][j] 
    return arr, value


'''
def solution(arr, str_A, str_B):
    max_x, max_y, value = -1, -1, 0
    for i in range(1, len(str_A)+1):
        for j in range(1, len(str_B)+1):
            if str_A[i-1] == str_B[j-1]:
                arr[i][j] = 1 + arr[i-1][j-1]
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])
                    
            if arr[i][j] > value:
                max_x, max_y, value = i, j, arr[i][j] 
    return arr, value
'''
def get_word_seq(arr, row, col):
    word = deque()
    #print(arr)
    while arr[row][col] > 0:
        #print(row, col)
        if row > 0 and col > 0:
            if arr[row-1][col] == arr[row][col]:
                row, col = row-1, col
            elif arr[row][col-1] == arr[row][col]:
                row, col = row, col-1
            else:
                word.appendleft((row, col))
                row, col = row-1, col-1
    return word


def get_word(result, str_A):
    word = ''
    #print(result)
    while len(result) > 0:
        row, _ = result.popleft()
        word += str_A[row-1]
    return word


def print_value(arr, str_A, str_B):
    print(" ",*list(str_B))
    for i in range(1, len(arr)):
        print(str_A[i-1],*arr[i][1:])

def main():
    str_A = input().rstrip()
    str_B = input().rstrip()

    arr = [[0]*(len(str_B)+1) for _ in range(len(str_A)+1)]
    #print(arr[0][2])
    #print(arr,str_A, str_B)
    arr, value = solution(arr, str_A, str_B)
    print_value(arr, str_A, str_B)
    print(value)
    #result = get_word_seq(arr, row, col)
    #print(len(result))
    #word = get_word(result, str_A)
    #print(word)

if __name__ == "__main__":
    main()