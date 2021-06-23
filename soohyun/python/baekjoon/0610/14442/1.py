from collections import deque
import sys
input = sys.stdin.readline

class PersonLoc():
    def __init__(self, loc, count, left_broken_chance):
        self.loc = loc
        self.count = count
        self.left_broken_chance = left_broken_chance

    def __str__(self):
        return f"loc: {self.loc}  count: {self.count} lbc: {self.left_broken_chance}"


def make_visited(broken_chance):
    dic = dict()
    for i in range(0, broken_chance+1):
        dic[i] = set()
    return dic


def bfs(maze, width, height, broken_chance):
    visited = make_visited(broken_chance)
    visited[0].add((0,0))
    queue =deque([PersonLoc((0, 0), 1, broken_chance)])
    while queue:
        cur_personloc = queue.popleft()
        #print(cur_personloc)
        
        if cur_personloc.loc == (height-1, width-1):
            return cur_personloc.count
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            row, col = cur_personloc.loc
            cur_row, cur_col = row + dr, col + dc
            if 0 <= cur_row < height and 0 <= cur_col < width:
                if maze[cur_row][cur_col] == '0':
                    if (cur_row, cur_col) not in visited[cur_personloc.left_broken_chance]:
                        visited[cur_personloc.left_broken_chance].add((cur_row, cur_col))
                        queue.append(PersonLoc(
                            (cur_row, cur_col),
                            cur_personloc.count + 1,
                            cur_personloc.left_broken_chance
                            ))
                if maze[cur_row][cur_col] == '1':
                    if cur_personloc.left_broken_chance > 0:
                        if (cur_row, cur_col) not in visited[cur_personloc.left_broken_chance-1]:
                                visited[cur_personloc.left_broken_chance-1].add((cur_row, cur_col))
                                queue.append(PersonLoc(
                                (cur_row, cur_col),
                                cur_personloc.count + 1,
                                cur_personloc.left_broken_chance - 1
                                ))

    return -1


def main():
    height, width, broken_chance = map(int, input().rstrip().split(" "))
    maze = [list(input().rstrip()) for _ in range(height)]
    print(bfs(maze, width, height, broken_chance))


if __name__ == "__main__":
    main()
