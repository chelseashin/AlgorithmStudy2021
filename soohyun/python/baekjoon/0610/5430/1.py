import re
import sys
from collections import deque

input = sys.stdin.readline

def get_num(raw_str):
    pattern = re.compile('([0-9]+)')
    result = pattern.findall(raw_str)
    return deque(result)
    

def make_format(is_forward, arr):
    arr = list(arr)
    if is_forward:
        return '['+','.join(arr)+']'
    return '['+','.join(arr[::-1])+']'


def execute_command(command, arr, num_of_number):
    is_forward = True
    for cmd in command:
        if cmd == 'R':
            is_forward = not is_forward
        elif cmd == 'D':
            if num_of_number > 0:
                if is_forward:
                    arr.popleft()
                else:
                    arr.pop()
                num_of_number -= 1
            else:
                return 'error'
    return make_format(is_forward, arr)
        

def main():
    TC = int(input().rstrip())
    for _ in range(TC):
        command = input().rstrip()
        num_of_number = int(input().rstrip())
        arr = get_num(input())
        print(execute_command(command, arr, num_of_number))

if __name__ == "__main__":
    main()