import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
def is_correct(made_bracket):
    stack = []

    if made_bracket[-1] == '(' or made_bracket[0] == ')':
        return False
    else:
        for bracket in made_bracket:
            if len(stack) == 0:
                stack.append(bracket)
            elif stack[-1] == '(' and bracket == ')':
                stack.pop()
            else:
                stack.append(bracket)
        if len(stack) == 0:
            return True
        else:

            return False

def recurse(num, made_bracket):
    made = set()
    answer = 0
    if len(made_bracket) == num:
        if is_correct(made_bracket):
            print(made_bracket, True)
            made.add(made_bracket)
            return 1
        return 0
    for bracket in ['(', ')']:
        if made_bracket + bracket in made:
            continue
        answer += recurse(num, made_bracket+bracket)
    return answer
        


def main():
    for i in range(int(input().rstrip())):
        num = int(input().rstrip())
        if num % 2 !=0:
            print(0)
        else:
            print("answer", recurse(num ,'') % 1000000007)


if __name__ == "__main__":
    main()