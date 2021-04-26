#시작 19시 24분
#끝 20시 23분 
MAX = 6
K = 0
import sys
def DFS(start, length, K, new_arr, raw_data):
    if(length == MAX):
        for i in range(0, 6):
            print(new_arr[i], end=" ")
        print()
        return
    else:
        for i in range(start, K):
            new_arr[length] = raw_data[i]
            DFS(i + 1, length + 1, K, new_arr, raw_data)

def main():
    while True:  
        raw_data = sys.stdin.readline().split()
        K = int(raw_data[0])
        if raw_data[0] == "0":
            break
        all_data = list(map(int, raw_data[1:]))
        DFS(0, 0, K, [0]*len(all_data), all_data)
        print()
if __name__=="__main__":
    main()