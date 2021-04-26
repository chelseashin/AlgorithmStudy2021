import sys
ARR = []
PRIME = dict()
MAXLENGTH = 2000000
def calc_prime(max_prime):
    global ARR
    global PRIME
    ARR = [True]*(MAXLENGTH)
    prime_num = 2
    ARR[0] = False
    ARR[1] = False
    for i in range(2, MAXLENGTH):
        if ARR[i]:
            PRIME[i] = True
            for j in range(i+i, MAXLENGTH, i):
                ARR[j] = False

def is_prime(num):
    global PRIME
    if num < MAXLENGTH:
        return ARR[num]
    else:
        for prime in list(PRIME.keys()):
            if num % prime == 0:
                return False
        return True
                
def is_couple(num):
    if num < 4:
        return "NO"
    elif num % 2 == 0:
        return "YES"
    else:
        if is_prime(num-2):
            return "YES"
    return "NO"


def main():
    T = int(sys.stdin.readline())
    max_thread = 0
    thread_list = list()
    for i in range(T):
        thread = list(map(int, sys.stdin.readline().split(" ")))
        thread_sum = thread[0] + thread[1]
        thread_list.append(thread_sum)
        if max_thread < thread_sum:
            max_thread = thread_sum
    calc_prime(max_thread)
    for thread in thread_list:
        print(is_couple(thread))
        
        
if __name__ == "__main__":
    main()