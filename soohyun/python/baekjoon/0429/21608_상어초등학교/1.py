# 시작시간: 5시15분
# 문제를 해석한시간: 5시 36분
# 시작 10:00분
# 알고리즘 생각한시간:10시 4분
# 코딩시간:10시 53분
# 디버깅시간: 11시 35분
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


def solution(seats, N, student_list):
    # 친한친구가 가장 많은것 계산
    maps = make_maps(N)
    
    for stud in student_list:
        prefer_seat = list()
        student = stud
        prefer = seats[stud]
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
                
        # 작은자리 계산
        row, col = zero_seat.pop(0)
        # 자리 선정
        maps[row][col] = stud

    # 만족도 조사
    satisfy = 0
    for row in range(N):
        for col in range(N):
            student = maps[row][col]
            prefer = seats[student]
            count_prefer_student = 0
            for dr, dc in zip(DR, DC):
                arow = row + dr
                acol = col + dc
                if is_in_boundary(arow, acol, N):
                    if prefer.get(maps[arow][acol], False):
                        count_prefer_student += 1
            if count_prefer_student == 1:
                satisfy += 1
            if count_prefer_student == 2:
                satisfy += 10
            if count_prefer_student == 3:
                satisfy += 100
            if count_prefer_student == 4:
                satisfy += 1000
    return satisfy


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