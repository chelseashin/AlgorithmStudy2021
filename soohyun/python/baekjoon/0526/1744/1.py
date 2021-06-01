    def main():
        N = int(input())
        minus = list()
        plus = list()
        for _ in range(N):
            num = int(input())
            minus.append(num) if num <= 0 else plus.append(num)
        minus = sorted(minus, reverse=True)
        plus.sort()
        sum_result = 0
        while len(plus) >= 2 or len(minus) >= 2:
            if len(plus) >= 2:
                num_1 = plus.pop()
                num_2 = plus.pop()
                if num_1 + num_2 > num_1 * num_2:
                    sum_result += num_1 + num_2
                else:
                    sum_result += num_1 * num_2
            if len(minus) >= 2:
                sum_result += minus.pop() * minus.pop()
        if len(plus) > 0:
            sum_result += plus.pop()
        if len(minus) > 0:
            sum_result += minus.pop()
        print(sum_result)
        




    if __name__ == "__main__":
        main()