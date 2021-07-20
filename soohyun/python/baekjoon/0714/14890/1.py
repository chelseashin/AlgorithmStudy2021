
# 걸린시간 1시간 20분
import sys
input = sys.stdin.readline

def count_slope_col(N, L, stairs):
    answer = 0
    for row in range(N):
        count = 1
        left = 101
        previous = -1
        is_slope = True
        for col in range(N):
            current = stairs[row][col]
            #print(f"|{stairs[row][col]} previous:{previous}, current: {current}|", end=" ")
            #print(left, count)
            if previous != -1:
                if abs(previous - current) == 1:
                    if left != 101 and left > 0:
                        #print("Not enough min number", f"|{stairs[row][col]} previous:{previous}, current: {current}|")
                        is_slope = False
                        break

                    if previous > current:
                        left = L
                        left -= 1
                        count = 0
                    else:
                        if count < L:
                            #print("count < L", count, f"|{stairs[row][col]} previous:{previous}, current: {current}|")
                            is_slope = False
                            break
                        count = 1
                elif abs(previous - current) == 0:
                    if left != 101 and left > 0:
                        left -= 1
                    else:
                        count += 1
                else:
                    #print("abs(previous - current) > 0", f"|{stairs[row][col]} previous:{previous}, current: {current}|")
                    is_slope = False
                    break
            previous = current
        if left != 101 and left > 0:
            is_slope = False
        if is_slope:
            #print(col, answer)
            answer += 1
    return answer



def count_slope_row(N, L, stairs):
    answer = 0
    for col in range(N):
        count = 1
        left = 101
        previous = -1
        is_slope = True
        for row in range(N):
            current = stairs[row][col]
            #print(f"|{stairs[row][col]} previous:{previous}, current: {current}|", end=" ")
            #print(left, count)
            if previous != -1:
                if abs(previous - current) == 1:
                    if left != 101 and left > 0:
                        #print("Not enough min number", f"|{stairs[row][col]} previous:{previous}, current: {current}|")
                        is_slope = False
                        break

                    if previous > current:
                        left = L
                        left -= 1
                        count = 0
                    else:
                        if count < L:
                            #print("count < L", count, f"|{stairs[row][col]} previous:{previous}, current: {current}|")
                            is_slope = False
                            break
                        count = 1
                elif abs(previous - current) == 0:
                    if left != 101 and left > 0:
                        left -= 1
                    else:
                        count += 1
                else:
                    #print("abs(previous - current) > 0", f"|{stairs[row][col]} previous:{previous}, current: {current}|")
                    is_slope = False
                    break
            previous = current
        if left != 101 and left > 0:
            is_slope = False
        if is_slope:
            #print(col, answer)
            answer += 1
    return answer
                    

            


def main():
    N, L = map(int, input().rstrip().split(" "))
    stairs = [list(map(int, input().rstrip().split(" "))) for _ in range(N)]
    print(count_slope_row(N, L, stairs) + count_slope_col(N, L, stairs))


if __name__ == "__main__":
    main()