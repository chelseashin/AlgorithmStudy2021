import sys
MAP = list()


class Robot:
    def __init__(self, id, loc, direction):
        self.id = id
        self.loc = loc
        self.direction = direction

        self.dl = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.dr = [(0, 1), (-1, 0), (0, 1), (-1, 0)]
  
    
    def change_right(self, count):
        #print("before_change", self.direction, self.dl[self.direction])
        
        self.direction = (4 +(self.direction - (count % 4))) % 4
        #print("after_change", self.direction, self.dl[self.direction])

        return self.dl[self.direction]

    def change_left(self, count):
        #print("before_change", self.direction, self.dl[self.direction])
        self.direction = (self.direction + (count % 4)) % 4
        #print("after_change", self.direction, self.dl[self.direction])
        return self.dl[self.direction]

    def move_robot(self):
        #print("before", self.dl[self.direction], self.loc)

        self.loc[0] = self.loc[0] + self.dl[self.direction][0]
        self.loc[1] = self.loc[1] + self.dl[self.direction][1] 
        #print("after", self.dl[self.direction], self.loc)

        return self.loc[0], self.loc[1]


def print_map():
    for i in range(len(MAP)):
        print(*MAP[i])


def move_robot(robot, count):
    global MAP
    for i in range(count):
        x, y = robot.move_robot()
        #MAP[x][y] = 1
        #print_map()
        #print()
        #MAP[x][y] = 0
        
        if x < 0 or y < 0:
            return -2, x, y
        if x >= len(MAP) or y >= len(MAP[0]):
            return -2, x, y
        if MAP[x][y] > 0:
            #print(MAP[x][y])
            return -1, x, y
    return 0, x, y
        

def start_simulation(M, robots):
    global MAP
    for _ in range(M):
        inputs = sys.stdin.readline().rstrip().split(" ")
        rid, cmd, count = int(inputs[0]), inputs[1], int(inputs[2]) 
        x, y = tuple(robots[rid-1].loc)
        MAP[x][y] = 0

        if cmd == "F":
            result = move_robot(robots[rid-1], count)
            if result[0] == -2:
                print("Robot {0} crashes into the wall".format(rid))
                return 2
            if result[0] == -1:
                print("Robot {0} crashes into robot {1}".format(rid, MAP[result[1]][result[2]]))
                return 1
            MAP[result[1]][result[2]] = robots[rid-1].id
        if cmd == "L":
            robots[rid-1].change_left(count)
            MAP[robots[rid-1].loc[0]][robots[rid-1].loc[1]] = robots[rid-1].id
        if cmd == "R":
            robots[rid-1].change_right(count)
            MAP[robots[rid-1].loc[0]][robots[rid-1].loc[1]] = robots[rid-1].id
        #print_map()
    return 0


def main():
    '''
    로봇 객체를 받을 배열 필요
    로봇의 위치를 저장할 지도 필요
    1. 로봇의 순서가 오면 로봇을 움직인다.
    2. F인경우 자신이 온위치부터 현재까지
       순차적으로 움직인다.
    3. 만나면 출력
    로봇이 가져야할것
      로봇 번호 현재위치
    지도가 가져야할것
       로봇 위치
    생각 해야할것 (회전) ==> 인덱스만알면됨
    '''
    global MAP
    robots = list()

    A, B = map(int, sys.stdin.readline().rstrip().split(" "))
    N, M = map(int, sys.stdin.readline().rstrip().split(" "))
    direct = {'E': 0, 'S': 1, 'W': 2, 'N': 3}
    for i in range(B):
        MAP.append([0]*A)

    for i in range(N):
        inputs = sys.stdin.readline().rstrip().split(" ")
        x, y, direction = int(inputs[0]), int(inputs[1]), inputs[2]
        robots.append(Robot(i+1, [y-1, x-1], direct[direction]))
        MAP[y-1][x-1] = i+1
        #print_map()
    result = start_simulation(M, robots)
    if result == 0:
        print("OK")


if __name__ == "__main__":
    main()