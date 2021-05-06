def bfs(phone, number, cur_loc):
    row, col = cur_loc
    count = 0
    queue = [(row, col, 0)]
    visited = set()
    while len(queue) > 0:
        row, col, count = queue.pop(0)
        if phone.get((row,col)) == str(number):
            loc = (row, col)
            return count, loc
        for dr, dc in zip([-1 ,1 ,0, 0], [0, 0, -1, 1]):
            nr = row + dr
            nc = col + dc
            if 0 <= nr < 4 and 0 <= nc < 3:
                if (nr, nc) not in visited:
                    queue.append((nr, nc, count + 1))
                    visited.add((nr, nc))
    return count, cur_loc
                    
    
def make_phone():
    phone = dict()
    phone_book = dict()
    i = 1
    for row in range(3):
        for col in range(3):
            phone[str(i)] = (row, col)
            phone_book[(row, col)] = str(i)
            i += 1
    for col, value in enumerate(['*', '0', '#']):
        phone[value] = (3, col)
        phone_book[(3, col)] = value
        i += 1
    return phone, phone_book


def solution(numbers, hand):
    answer = ''
    left = (3, 0)
    right = (3, 2)
    phone, phone_book = make_phone()
    print(phone_book)
    for number in numbers:
        number = str(number)
        if number in {'1','4','7'}:
            left = phone[number]
            answer += 'L'
        elif number in {'3', '6', '9'}:
            right = phone[number]
            answer += 'R'
        else:
            left_count, left_loc = bfs(phone_book, number, left)
            right_count, right_loc = bfs(phone_book, number, right)
            if left_count < right_count:
                left = phone[number]
                answer += 'L'
            elif left_count > right_count:
                right = phone[number]
                answer += 'R'
            else:
                if hand == "left":
                    answer += 'L'
                    left = phone[number]
                elif hand == "right":
                    answer += 'R'
                    right = phone[number]
            
    return answer
                
                
                
            
        
        
