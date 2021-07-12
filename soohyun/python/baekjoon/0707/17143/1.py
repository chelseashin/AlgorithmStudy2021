import sys
input = sys.stdin.readline

class Shark():
    def __init__(self, speed, direction, size):
        self.speed = speed
        self.direction = direction
        self.size = size
    def __str__(self):
        return f'{self.speed}, {self.direction}, {self.size}'


def print_dict(shark):
    for key, value in shark.items():
        print(key, value)


def out_of_range(nr, nc, row, col):
    if nr < 0 or nr >= row or nc < 0 or nc >= col:
        return True
    return False
    


def start_fishing(row, col, sharks, fishman):
    catch = 0
    shark_dict = sharks

    for c in range(col):
        # 낚시
        if fishman[0] < row:
            catch += shark_dict[fishman].size
            shark_dict.pop((fishman))
        # shark 움직임
        fishman = (row, c+1)
        new_shark = dict()
        for loc, shark in shark_dict.items():
            nr = loc[0]
            nc = loc[1]
            for _ in range(shark.speed):
                nr += shark.direction[0]
                nc +=  shark.direction[1]
                # 범위 밖으로 나가는 경우 방향 바꿈
                if out_of_range(nr, nc, row, col):
                    shark.direction = (-shark.direction[0], -shark.direction[1])
                    nr += shark.direction[0]
                    nc += shark.direction[1]
                    nr += shark.direction[0]
                    nc += shark.direction[1]
            # 다음 방향 계산
            # 똑같은 칸이 존재하는경우
            if new_shark.get((nr, nc), None) is not None:
                if new_shark[(nr, nc)].size < shark.size:
                    new_shark[(nr, nc)] = shark
            else:
                new_shark[(nr, nc)] = shark

            # 낚시꾼 잡을 고기 위치 확인
            if nc == fishman[1]:
                fishman = (nr, c+1) if fishman[0] > nr else fishman
            shark_dict = new_shark
    return catch

            
def main():
    sharks = dict()
    row, col, shark_count = map(int, input().rstrip().split(" "))
    direction =  {1:(-1, 0), 2: (1, 0), 3:(0, 1), 4:(0, -1)}
    fishman = (row, 0)
    for _ in range(shark_count):
        r, c, s, d, z = map(int, input().rstrip().split(" "))
        if d == 1 or d == 2:
            s %= ((row-1) * 2)
        if d == 3 or d == 4:
            s %= ((col-1) * 2)
        sharks[(r-1, c-1)] = Shark(s, direction[d], z)  
        if c-1 == fishman[1]:
            fishman = (r-1, c-1) if fishman[0] > r-1 else fishman
    print(start_fishing(row, col, sharks, fishman))

if __name__ == "__main__":
    main()