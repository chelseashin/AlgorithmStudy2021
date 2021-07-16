# 푼시간 40분
import sys
input = sys.stdin.readline
def start_assembly(lego, width):
    start = 0
    end = len(lego) - 1
    nano_width = width * (10**7)
    result = [-1, -1]
    while start < end:
        if lego[start] + lego[end] == nano_width:
            if sum(result) >= 0:
                if abs(result[0] - result[1]) < abs(lego[start] - lego[end]):
                    result[0] = lego[start]
                    result[1] = lego[end]
            else:
                result[0] = lego[start]
                result[1] = lego[end]
            end -= 1
            start += 1
        if lego[start] + lego[end]  > nano_width:
            end = end - 1
        elif lego[start] + lego[end]  < nano_width:
            start = start + 1
    return result



def main():
    while True:
        value =  input().rstrip()
        if value == '':
            break
        width = int(value)
        N = int(input().rstrip())
        lego = [0 for _ in range(N)]
        for i in range(N):
            lego[i] = int(input().rstrip())
        lego.sort()
        result = start_assembly(lego, width)
        print("danger") if sum(result) < 0 else print(f"yes {result[0]} {result[1]}")

if __name__ == "__main__":
    main()