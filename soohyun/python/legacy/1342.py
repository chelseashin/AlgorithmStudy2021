import sys

def is_lucky(data):
    if len(data) == 1:
        return True
    for idx in range(0, len(data)-1):
        if data[idx] == data[idx+1]:
            return False
    return True

def dfs(string, str_size, data):
    result = set()
    if len(string) == str_size:
        print(string)
        return string
    for alpha in data.keys():
        if is_lucky(string+alpha):
            if data[alpha] > 0:
                data[alpha] -= 1
                string += alpha
                result.add(dfs(string, str_size, data))
                string = string[:-1]
                data[alpha] += 1   
    return len(result)

def main():
    data = sys.stdin.readline().strip()
    alpha_set  = dict()
    for alpha in data:
        if alpha_set.get(alpha) == None:
            alpha_set[alpha] = 0
        alpha_set[alpha] += 1
    str_len = len(data)
    print(dfs("", str_len, alpha_set))
    

if __name__ == "__main__":
    main()