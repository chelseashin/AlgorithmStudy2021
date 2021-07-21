import sys
input = sys.stdin.readline
def main():
    N = int(input().rstrip())
    tall_info = sorted(list(map(int, input().rstrip().split(" "))))
    data = [0] * N
    prev_idx = -1
    for idx, value in enumerate(tall_info):
        if idx == 0 and value > 0:
            return 0
        if prev_idx != -1 and abs(tall_info[prev_idx]-tall_info[idx]) > 1:
            return 0
        
        data[value] += 1
        if data[value] > 2:
            return 0

        prev_idx = idx
    
    prev_value = -1
    count_two, count_one = 0, 0 
    for value in data:
        if value == 0:
            break
        if prev_value != -1 and value > prev_value:
            return 0
        if value == 2:
            count_two += 1
        if value == 1:
            count_one += 1
        prev_value = value
    multiple = 1 if count_one == 0 else 2
    return 2**count_two * multiple

        
    




if __name__ == "__main__":
    print(main())