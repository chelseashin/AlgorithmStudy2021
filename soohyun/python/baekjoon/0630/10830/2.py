# 걸린시간 2시간 10분
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
   

def matrix_pow(dp):
    def matrix_pow(matrix, count):
        if count == 0: return dp[0]
        elif count == 1: return dp[1]
        if dp.get(count, None) is not None: return dp[count]
        if count % 2 == 0:
            dp[count] = matmul(matrix_pow(matrix, count//2), matrix_pow(matrix, count//2))
        else:
            dp[count] = matmul(matrix, matrix_pow(matrix, count-1))
        return dp[count]
    return matrix_pow


def mod_int(num):
    return int(num) % 1000


def input_values():
    N, count = map(int, input().rstrip().split(" "))
    matrix = [list(map(mod_int, input().rstrip().split(" "))) for _ in range(N)]
    return matrix, count


def print_mat(matrix):
    for row in matrix:
        print(*row)


def make_dp(matrix):
    dp = dict()
    dp[0] = unit_matrix(len(matrix))
    dp[1] = matrix
    return dp


def main():
    matrix, count = input_values()
    dp = make_dp(matrix)
    result = matrix_pow(dp)
    print_mat(result(matrix, count))
    
    
if __name__ == "__main__":
    main()
