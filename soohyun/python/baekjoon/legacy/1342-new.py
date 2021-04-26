import sys
ALPHA = [0]*26

def dfs(before, pos, input_length):
    count = 0
    global ALPHA
    if pos == input_length:
        count +=1
    else:
        for i in range(26):
            if ALPHA[i] < 1 or ord('a') + i == before:
                continue
            ALPHA[i] -=1
            count += dfs(ord('a')+i, pos+1, input_length)
            ALPHA[i] += 1
    return count

def to_int(alpha):
    global ALPHA
    return int(ord(alpha))
    
def main():
    data = list(map(to_int, sys.stdin.readline().strip()))
    for alpha in data:
        ALPHA[alpha - ord('a')] += 1
    print(dfs(0, 0, len(data)))

if __name__ == "__main__":
    main()