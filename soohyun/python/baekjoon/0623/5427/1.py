import sys
from enum import Enum
from collections import deque
input = sys.stdin.readline

class PLACE(Enum):
    FIRE = 2
    PERSON = 1

def make_visited(fires, person, height, width):
    visited = [ [0]*width for _ in range(height)]
    visited[person[0]][person[1]] = PLACE.PERSON
    for row, col in fires:
        visited[row][col] = PLACE.FIRE
    return visited


def is_inrange(loc, height, width):
    row, col = loc
    if 0 <= row < height and 0 <= col < width:
        return True
    return False


def is_arrive(place, loc, height, width):
    row, col = loc
    if place == PLACE.PERSON:
        if row == 0 or row == height - 1 \
            or col == 0 or col == width - 1:
            return True
    return False
        

def is_firing(place, loc, maze, height, width):
    row, col = loc
    if place == PLACE.PERSON:
        for dr, dc, in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr, nc = row + dr, col + dc
            if is_inrange((nr, nc), height, width):
                if maze[nr][nc] == '*':
                    return True
    return False

def solution(maze, fires, person):
    height, width = len(maze), len(maze[0])
    queue = deque()
    visited = make_visited(fires, person, height, width)
    for fire in fires:
        queue.appendleft((PLACE.FIRE, fire, 0))
    queue.appendleft((PLACE.PERSON, person, 0))

    while queue:
        place, loc, count = queue.pop()
        if is_arrive(place, loc, height, width):
            return count
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr, nc = loc[0] + dr, loc[1] + dc
            if not is_inrange((nr, nc), height, width):
                continue
            if maze[nr][nc] == '#':
                continue

            if visited[nr][nc] == 0:
                visited[nr][nc] = place
                queue.appendleft((place, (nr, nc), count+1))
            if place == PLACE.FIRE and visited[nr][nc] == PLACE.PERSON:
                visited[nr][nc] = place
                queue.appendleft((place, (nr, nc), count+1))
    return -1


def input_values():
    N = int(input())
    for _ in range(N):
        maze = list()
        fires = list()
        person = tuple()
        _, height = map(int, input().rstrip().split(" "))
        for h in range(height):
            row = list(input().rstrip())
            for w, value in enumerate(row):
                if value == '*':
                    fires.append((h, w))
                elif value == '@':
                    person = (h, w)
            maze.append(row)
        yield maze, fires, person
        

def main():
    for maze, fires, person in input_values():
        result = solution(maze, fires, person)
        print(result+1) if result >= 0 else print("IMPOSSIBLE")

if __name__ == "__main__":
    main()