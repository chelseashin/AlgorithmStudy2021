import sys
input = sys.stdin.readline
DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]

def make_maps(num):
    maps = list()
    for _ in range(num):
        maps.append([0]*num)
    return maps


def is_in_boundary(arow, acol, N):
    if arow >= 0 and arow < N:
        if acol >= 0 and acol < N:
            return True
    return False

def find_seats(maps, N, student, seats):
    prefer_seat = list()
    prefer = seats[student]
    max_prefer_student = 0
    for row in range(N):
        for col in range(N):
            if maps[row][col] != 0:
                continue
            count_prefer_student = 0
            for dr, dc in zip(DR, DC):
                # 인접 학생 찾기
                arow = row + dr
                acol = col + dc
                if is_in_boundary(arow, acol, N):
                    if prefer.get(maps[arow][acol], False):
                        count_prefer_student += 1
            if max_prefer_student == count_prefer_student:
                prefer_seat.append((row, col))
            elif max_prefer_student < count_prefer_student:
                del prefer_seat
                prefer_seat = [(row, col)]
                max_prefer_student = count_prefer_student
    return prefer_seat


def find_zero_seats(prefer_seat):
    # 빈자리가 가장 많은것을 계산
    zero_seat = list()
    max_zero_seat = 0
    for row, col in prefer_seat:
        zero_count = 0
        if maps[row][col] != 0:
                continue
        for dr, dc in zip(DR, DC):
            # 빈자리 찾기
            arow = row + dr
            acol = col + dc
            if is_in_boundary(arow, acol, N) and maps[arow][acol] == 0:
                zero_count += 1
        if max_zero_seat == zero_count:
            zero_seat.append((row, col))    
        elif max_zero_seat < zero_count:
            max_zero_seat = zero_count
            del zero_seat
            zero_seat = [(row, col)]
    return zero_seat


def soltuion(seats, N, student_list):
    maps = make_maps(N)
    for stud in student_list:
        prefer_seat = find_seats(maps, N, student_list, seats)
        zero_seat = find_zero_seats(prefer_seat)
        maps[zero_seat[0]][zero_seat[1]] = stud
    calc_staisfy(N, maps)


def main():
    N = int(input().rstrip())
    seats = dict()
    student = list()
    for _ in range(N*N):
        seat = list(map(int, input().rstrip().split(" ")))
        prefer = dict()
        student.append(seat[0])
        for prefer_student in seat[1:]:
            prefer[prefer_student] = True
        seats[seat[0]] = prefer
    print(solution(seats, N, student))


if __name__ == "__main__":
    main()