import sys
input = sys.stdin.readline

def count_alpha(alpha_list):
    alpha_dict = dict()
    for word in alpha_list:
        size = len(word)
        for idx, value in enumerate(word):
            if alpha_dict.get(value, -1) < 0:
                alpha_dict[value] = 10 ** (size-(idx+1))
            else:
                alpha_dict[value] += 10 ** (size-(idx+1))
    return alpha_dict


def decide_number(alpha_dict):
    alpha_num = dict()
    salpha = dict(sorted(alpha_dict.items(), key=lambda item: item[1], reverse=True))
    number = 9
    for key in salpha.keys():
        alpha_num[key] = number
        number -= 1
    return alpha_num


def input_values():
    alpha_list = []
    N = int(input().rstrip())
    for _ in range(N):
        alpha_list.append(input().rstrip())
    return alpha_list


def calc(alpha_list, alpha_num):
    result = 0
    for word in alpha_list:
        multi = 10 ** (len(word)-1)
        number = 0
        for alpha in word:
            number += (alpha_num[alpha] * multi)
            multi //= 10
        result += number
    return result


def main():
    alpha_list = input_values()
    alpha_dict = count_alpha(alpha_list)
    alpha_num = decide_number(alpha_dict)
    print(calc(alpha_list, alpha_num))

if __name__ == "__main__":
    main()
