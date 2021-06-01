import sys

def is_adjacement(count):
    #print(count)

    first_num = count[0]
    count_set = set(count)
    compare_set = {first_num}
    queue = [first_num]
    while queue:
        num = queue.pop(0)
        row, col = num // 5, num % 5
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr, nc = row + dr, col + dc
            if 0 <= nr < 5 and 0 <= nc < 5:
                num = nr * 5 + nc
                if num in count_set:
                    if num in compare_set:
                        continue
                    compare_set.add(num)
                    queue.append(num)
    if len(compare_set) == len(count_set):
        #print(compare_set, count_set)
        return True
    return False


def is_over_four(seats, student_list):
    count = 0

    for num in student_list:
        row, col = num // 5 , num % 5
        if seats[row][col] == 'S':
            count += 1
    if count >= 4:
        #print("four", student_list)
        return True
    return False


def dfs(seats, count, start):
    result = 0
    if len(count) == 7:
        if is_over_four(seats, count) and is_adjacement(count):
            return 1
        else:
            return 0
    else:
        for i in range(start, 25):
            if len(count) <= 0 or count[-1] < i:
                count.append(i)
                result += dfs(seats, count, start+1)
                #print("result", result)
                count.pop()
        return result


def main():
    seats = [input().rstrip() for _ in range(5)]
    print(dfs(seats, [], 0))
    


if __name__ == "__main__":
    main()