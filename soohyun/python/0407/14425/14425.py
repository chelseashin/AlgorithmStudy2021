import sys

def main():
    str_dict = dict()
    count = 0
    dictionary, check_word = map(int,
                                 sys.stdin.readline().strip().split())
    for _ in range(dictionary):
        str_dict[sys.stdin.readline().rstrip()] = 0
    for _ in range(check_word):
        word = sys.stdin.readline().rstrip()
        if str_dict.get(word) is not None:
            count += 1
    print(count)
if __name__ == "__main__":
    main()