import sys
import re
input = sys.stdin.readline

def print_visit(visited):
    print("========")
    for i in range(5):
        print(*visited[i])
    print("=======")

def seven_recursive(visited, seats, line, cur_loc):
    count = 0
    visit_list = dict()

    if len(line) == 7:
        # print("LINE", line)
        print("VISITED", print_visit(visited))
        if len(re.findall('(S)', line)) >= 4:
            return 1
        return 0
    else:
        for dr, dc in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
            nr, nc = dr + cur_loc[0], dc + cur_loc[1]
            if 0 <= nr < 5 and 0 <= nc < 5 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                line += seats[nr][nc]
                
                count += seven_recursive(visited, seats, line, (nr, nc))
                line = line[0:-1]
                visited[nr][nc] = 0
        return count
    

def make_seven_princess(visited, seats, startS):
    count = 0
    while len(startS) > 0:
        i, j = startS.pop()
        visited[i][j] = 1
        line = 'S'
        cur_loc = (i, j)
        count += seven_recursive(visited, seats, line, cur_loc)
        visited[i][j] = 0
    return count


def main():
    # S가 있는 위치 찾기
    # pop한후 visited에 표시하기
    # 방문하나씩 돌리기
    startS = set()
    seats = [input().rstrip() for _ in range(5)]
    visited = [[0] * 5 for _ in range(5)]

    for i in range(5):
        for j in range(5):
            if seats[i][j] == 'S':
                startS.add((i, j))
    
    return make_seven_princess(visited, seats, startS)




if __name__ == "__main__":
    print(main())