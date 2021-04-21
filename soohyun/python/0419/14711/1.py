import sys
input = sys.stdin.readline

def is_go(nr, nc, N):
    if nr >= 0 and nc >= 0 and nr < N and nc < N:
        return True
    return False


def start_game(visited, tile):
    for i in range(len(tile)-1):
        for j in range(len(tile)):
            if tile[i][j] == '#':
                for dr, dc in zip([1, 0, 0], [0, -1, 1]):
                    nr, nc = i + dr, j + dc
                    if is_go(nr, nc, len(tile)):
                        visited[nr][nc] ^= 1
                #print("==debug start==", i , j)
                #debug(tile, "tile")
                #debug(visited, "visited")
                #print("==debug end==")

        for j in range(len(tile)):
            if visited[i][j] == 1:
                tile[i+1][j] = "#"
            else:
                tile[i+1][j] = '.'
    print_tile(tile)
            

def print_tile(tile):
    for i in range(len(tile)):
        for j in range(len(tile)):
            print(tile[i][j], end="")
        print()


def debug(tile, name):
    print("==start {0}==".format(name))
    for i in range(len(tile)):
        for j in range(len(tile)):
            print(tile[i][j], end="")
        print()
    print("==end  {0}==".format(name))


def main():
    tile = list()
    visited = list()
    N = int(input().rstrip())
    first_tiles = input().rstrip()

    for i in range(N):
        visited.append([0]*N)
        if i == 0:
            tile.append(list(first_tiles))
        else:
            tile.append(['.']*N)
    
    start_game(visited, tile)

if __name__ == "__main__":
    main()