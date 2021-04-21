import sys

def main(m, k):
    key = list(k)
    result = ''
    for i in m:
        if len(key) > 0 and i == key[0]:
            key.pop(0)
        else:
            result += i
    return result


if __name__ == "__main__":
    print(main("kkaxbycyz", "abc"))
    print(main("acbbcdc", "abc"))