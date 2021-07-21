import sys
input = sys.stdin.readline

def start_game(tall_info, N):
    data = [0] * N
    prev_idx = -1
    for idx, value in enumerate(tall_info):
        data[value] += 1
        if idx == 0 and value > 0: # 숫자가 0보다 큰수에서 시작하면
            return 0 # 말이 안되므로 0을 반환
        # 숫자가 연속되지 않으면 
        if prev_idx != -1 and abs(tall_info[prev_idx]-tall_info[idx]) > 1:
            return 0
        # 숫자가 2보다크면  0 을 반환
        if data[value] > 2:
            return 0
        prev_idx = idx
    
    prev_value = -1
    count_two, count_one = 0, 0 
    for value in data:
        # 키카작은 동물의수가 더 많을경우
        if prev_value != -1 and value > prev_value:
            return 0
        # 2인경우 갯수셈
        if value == 2:
            count_two += 1
        # 1이 존재하는경우 갯수셈
        if value == 1:
            count_one += 1
        prev_value = value
        
    # 계산
    multiple = 1 if count_one == 0 else 2
    return 2**count_two * multiple

def main():
    N = int(input().rstrip())
    tall_info = sorted(list(map(int, input().rstrip().split(" "))))
    print(start_game(tall_info, N))
   

if __name__ == "__main__":
    print(main())