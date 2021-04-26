# 20시
import sys


def main():
    count = 0
    broken_num = [False]*10
    channel = sys.stdin.readline().strip()
    broken_key_num = int(sys.stdin.readline().strip())
    broken_keys = list(map(int, sys.stdin.readline().strip().split(" ")))
    for i, key in enumerate(broken_keys):
        broken_num[key] = True
    complete_num = ''
    if channel == "100":
        return 0
    for num in channel:
        start = int(num)
        i = 0
        j = 0
        left = start - i
        right = start + j
        end = 0
        while True:
            if not broken_num[left] or not broken_num[right]:
                if not broken_num[left] and broken_num[right]:
                    end = left
                elif broken_num[left] and not broken_num[right]:
                    end = right
                else:
                    if abs(start-left) > abs(start-right):
                        end = right
                    else:
                        end = left
                #print(left, right, end)

                break
            if left > 0:
                left = start - i
                i += 1
            if right < broken_key_num - 1:
                right = start + j
                j += 1
            #print(complete_num, i, j, end)

        complete_num += str(end)
        count += 1
    #print(complete_num)
    count += abs(int(complete_num) - int(channel))
    return count

if __name__ == "__main__":
    print(main())