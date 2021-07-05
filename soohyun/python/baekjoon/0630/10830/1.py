import sys
input = sys.stdin.readline

def matmul(A, B):
    count = len(A)
    matrix = [[0]* count for _ in range(count)]
    for i in range(count):
        for k in range(count):
            result = 0
            for j in range(count):
                result += A[i][j] * B[j][k]
            matrix[i][k] = result % 1000
    return matrix

def unit_matrix(count):
    return [[1 if i==j  else 0 for j in range(count)] for i in range(count)]
   

def matrix_pow(matrix, count, N):
    if count == 0:
        return unit_matrix(N)
    elif count == 1:
        return matrix
    if count % 2 == 0:
        result = matmul(matrix_pow(matrix, count//2, N), matrix_pow(matrix, count//2, N))
        #print(count, result)
        return result
    else:
        result = matmul(matrix, matrix_pow(matrix, count-1, N))
        #print(matrix, count, result)
        return result



def input_values():
    N, count = map(int, input().rstrip().split(" "))
    matrix = [ list(map(int, input().rstrip().split(" "))) for _ in range(N)]
    return matrix, count


def print_mat(matrix):
    for row in matrix:
        print(*row)


def main():
    matrix, count = input_values()
    print_mat(matrix_pow(matrix, count, len(matrix)))
    
    

if __name__ == "__main__":
    main()