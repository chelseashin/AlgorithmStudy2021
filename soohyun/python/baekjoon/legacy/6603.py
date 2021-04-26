#시작 19시 24분
#끝 20t시 34분
import sys
def print_S(S):
    element_list = list(S.keys())
    element_list.sort()
    for idx in range(0, len(element_list)-1):
        print(element_list[idx], end=" ")
    print(element_list[len(element_list)-1])

def get_case(k, S):
    if len(S) == 6:
        print_S(S)
        return
    element_list = list(S.keys())
    for idx in range(len(element_list)-1, -1, -1):
         S.pop(element_list[idx])
         get_case(k, S)
         S[element_list[idx]] = 0

def make_dataset(data):
    S = dict()
    for element in data:
        S[element] = 0
    return S

def main():
    while True:  
        raw_data = sys.stdin.readline().split()
        if raw_data[0] == "0":
            break
        all_data = list(map(int, raw_data))
        k = all_data[0]
        S = make_dataset(all_data[1:])
        get_case(k, S)
        print()
if __name__=="__main__":
    main()