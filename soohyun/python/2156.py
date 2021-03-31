import sys
WINE = list()
MAX_COUNT = 2
#걸린시간 1시간
def drink_wine(wine_idx, continuous_count):
    amount_of_wine = 0
    if wine_idx >= len(WINE):
        return 
    for i in range(wine_idx, len(WINE)):
        if continuous_count > MAX_COUNT:
            continuous_count = 0
            continue
        amout_of_wine += max(drink_wine(i+1, continuous_count+1),
                             drink_wine(i+2, continuous_count))
    return amount_of_wine

def main():
    N = int(sys.stdin.readline())
    WINE = list()
    for i in range(N):
        WINE.append(int(sys.stdin.readline()))
    print(drink_wine(0, 0))

if __name__ == "__main__":
    main()