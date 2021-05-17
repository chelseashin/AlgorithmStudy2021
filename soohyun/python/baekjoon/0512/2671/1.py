import re

def main():
    code = input()
    pattern = re.compile('^(100+1+|01)+$')
    result = re.match(pattern, code)
    if result:
        print("SUBMARINE")
    else:
        print("NOISE")


if __name__ == "__main__":
    main()