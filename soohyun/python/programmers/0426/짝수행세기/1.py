combi = list()
MOD = 10**7 + 19

def get_combination(n, r):
    global combi
    if n < r: 
        return 0
    ret = combi[n][r]
    if ret != -1:
        return ret
    if n == r or r == 0:
        return 1
    ret = (get_combination(n-1, r-1) + get_combination(n-1, r)) % MOD
    return ret


def solution(a):
    global combi
    answer = -1
    n = len(a)
    m = len(a[0])
    
    one_count = dict()
    for col in range(len(a[0])):
        for row in range(len(a)):
            if a[row][col] == 1:
                if one_count.get(col+1, 0) == 0:
                    one_count[col+1] = 1
                else:
                    one_count[col+1] += 1

    print(one_count)
        

    combi = [ [-1] * 301 for _ in range(301)]
    dp = [[0]*(n+1) for _ in range(m+1)]
    # 1열에서 0이 있는 경우에수
    dp[1][n-one_count[1]] = get_combination(n, one_count[1])
    print(dp)
    print(combi)
    for column in range(1, m+1):
        one_count_num = one_count[column]
        for num in range(0, n+1):
            for k in range(0, one_count_num+1):
                will_set_odd_row = one_count_num - k
                will_be_even_row_cnt = (num - k) + will_set_odd_row
                if will_set_odd_row < 0 or will_be_even_row_cnt > n or will_be_even_row_cnt < 0:
                    continue
                num_of_case = (get_combination(num, k) * get_combination(n - num, one_count_num - k)) % MOD
                dp[column][will_be_even_row_cnt] += dp[column-1][num] * num_of_case * MOD
                dp[column][will_be_even_row_cnt] %= MOD
    return dp[m][n]

print(solution([[0,1,0],[1,1,1],[1,1,0],[0,1,1]]))
#print(solution([[1,0,0],[1,0,0]]))
#print(solution([[1,0,0,1,1],[0,0,0,0,0],[1,1,0,0,0],[0,0,0,0,1]]))
    