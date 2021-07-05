import sys
from heapq import heappush, heappop
from collections import defaultdict

class Alpha():
    def __init__(self, word, appear):
        self.word = word
        self.appear = appear
        self.appear_size = len(appear)

    def __lt__(self, other):
        if self.appear > other.appear:
            
            return True
        elif self.appear == other.appear:
            if self.appear_size > other.appear_size:
                return True
            elif self.appear_size == other.appear_size:
                return self.word < other.word
        return False

    def __str__(self):
        return 'f{word} + f{appear} + f{appear_size}'


def count_alpha(word_list):
    alpha_dict = defaultdict(list)
    for word in word_list:
        size = len(word)
        for i in range(size-1, -1, -1):
            alpha_dict[word[i]].append((size-i))
    return alpha_dict


def decide_number(alpha_dict):
    alpha_num = dict()
    alpha_list = list()
    number = 9
    for key, value in alpha_dict.items():
        value = sorted(value)
        value.reverse()
        heappush(alpha_list, Alpha(key, value))

    while alpha_list:
        alpha = heappop(alpha_list)
        if alpha_num.get(alpha.word, -1) < 0:
            alpha_num[alpha.word] = number
        number -= 1

    return alpha_num


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


def input_values():
    alpha_list = []
    for _ in range(int(input().rstrip())):
        alpha_list.append(input())
    return alpha_list


def main():
    alpha_list = input_values()
    #print(alpha_list)
    alpha_dict = count_alpha(alpha_list)
    #print(alpha_dict)
    alpha_num = decide_number(alpha_dict)
    #print(alpha_num)
    print(calc(alpha_list, alpha_num))

if __name__ == "__main__":
    main()
