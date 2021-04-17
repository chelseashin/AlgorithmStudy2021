# 14:00 start
# 14:09 pass

def solve(m, k):
    result = ""
    idx1, idx2 = 0, 0       # 각 문자열에 대해 인덱스로 제어
    while idx1 <= len(m):
        if m[idx1] == k[idx2]:      # 같은 문자이면
            idx1 += 1
            idx2 += 1
            if idx2 == len(k):      # k문자열 끝에 다다르면
                result += m[idx1:]  # 남은 m 문자열 붙이고
                break               # 검사 종료
        else:           # 다른 문자이면
            result += m[idx1]
            idx1 += 1
        # print(result)
    return result

print(solve("kkaxbycyz", "abc"))
print(solve("acbbcdc", "abc"))
# kkxyyz
# cbdc