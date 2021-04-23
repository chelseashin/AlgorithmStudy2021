def solution(s):
    time, zero = 0, 0
    while s != "1":
        x = s.count("1")        # 0 제거 후 길이
        zero += len(s) - x      # 제거한 0의 갯수
        s = bin(x)[2:]          # 다시 이진수로 변환
        time += 1
    return [time, zero]

print(solution("0111010"))
print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))