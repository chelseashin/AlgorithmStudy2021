import sys
input = sys.stdin.readline

PLAYER = []
NUM_PLAYER = 11
def choose_player(visited, players):
    global PLAYER
    max_line_up = 0
    if len(players) >= 11:
        result_sum = 0
        for i, player in enumerate(players):
            if PLAYER[i][player] == 0:
                return -1
            result_sum += PLAYER[i][player]
        return result_sum
    else:
        line_up = 0
        for j in range(11):
            if not visited[j]:
                visited[j] = True
                players.append(j)
                if PLAYER[len(players)-1][j] != 0:
                    line_up = choose_player(visited, players)
                players.pop()
                visited[j] = False
                if max_line_up < line_up:
                    max_line_up = line_up
        return max_line_up


def input_player_info():
    global PLAYER
    PLAYER = []
    for _ in range(NUM_PLAYER):
        rows = list(map(int, input().rstrip().split(" ")))
        PLAYER.append(rows)


def main():
    N = int(input())
    for _ in range(N):
        input_player_info()
        visited = [False] * NUM_PLAYER
        players = []
        print(choose_player(visited, players))


if __name__ == "__main__":
    main()


