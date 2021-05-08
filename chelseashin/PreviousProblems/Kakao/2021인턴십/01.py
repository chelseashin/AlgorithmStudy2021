# 14:13 pass

def solution(s):
    answer = ""
    digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    numbers = {"zero":"0", "one":"1", "two":"2", "three":"3",
                "four":"4", "five":"5", "six":"6", 
                "seven":"7", "eight":"8", "nine":"9"}
    idx = 0
    temp = ""
    while idx < len(s):
        if s[idx] in digits:
            answer += str(s[idx])
            idx += 1
        else:
            temp += s[idx]
            idx += 1
            if temp in numbers.keys():
                answer += numbers[temp]
                temp = ""
    return int(answer)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))