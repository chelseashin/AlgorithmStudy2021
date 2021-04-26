import sys
WINE = list()
MAX_COUNT = 2
#점화식 
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
    WINE = [0]*(N+3)
    answer = 0
    drink_wine = list()

    for i in range(3, N+3):
        WINE[i] = int(sys.stdin.readline())
    drink_wine = [0]*len(WINE)
    for i in range(3, N+3):
        drink_wine[i] = max(
                            drink_wine[i-3] + WINE[i-1] + WINE[i],
                            drink_wine[i-2] + WINE[i])
        drink_wine[i] = max(
                            drink_wine[i-1],
                            drink_wine[i])
        answer = max(answer, drink_wine[i])
    print(answer)
                        

if __name__ == "__main__":
    main()