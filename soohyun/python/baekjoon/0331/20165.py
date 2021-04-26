import sys
from collections import deque
#시작 11시 38분
DOMINO = list()
DOMINO_STATUS = list()
DIRECTION = {'E':(0, 1), 'S':(1, 0),
             'W':(0, -1), 'N':(-1, 0)}

def input_data(attack=False):
    if attack:
        result = sys.stdin.readline().rstrip().split(" ")
        return int(result[0]), int(result[1]), result[2]
    else:
        return map(int, sys.stdin.readline().rstrip().split(" "))

def attack():
    score = 0
    global DOMINO_STATUS
    falling_dominos = deque()
    attack_x, attack_y, direction = input_data(True)
    #list index 맞춰주기
    attack_x = attack_x - 1
    attack_y = attack_y - 1
    if DOMINO_STATUS[attack_x][attack_y] == "F":
        return
    falling_dominos.appendleft((attack_x, attack_y, direction))
    while len(falling_dominos) > 0:
        x, y, direction = falling_dominos.popleft()
        K = DOMINO[x][y]
        for i in range(K):
            next_x = x + DIRECTION[direction][0]*i
            next_y = y + DIRECTION[direction][1]*i
            if is_stop(next_x, next_y):
                break
            if DOMINO_STATUS[next_x][next_y] == "S":
                falling_dominos.appendleft((next_x, next_y, direction))
                score += 1
            DOMINO_STATUS[next_x][next_y] = "F"
    return score

def defence():
    global DOMINO_STATUS
    defense_x, defense_y = input_data()
    #리스트 인덱스 맞춰주기
    defense_x = defense_x - 1
    defense_y = defense_y - 1
    DOMINO_STATUS[defense_x][defense_y] = "S"

def is_stop(x, y):
    if x < 0 or y < 0:
        return True
    if x >= len(DOMINO) or y >= len(DOMINO[0]):
        return True
    return False

def start_game(game_round):
    score = 0
    for r in range(game_round):
        score += attack()
        defence()
    return score

def print_domino(N):
    for i in range(N):
        print(*DOMINO_STATUS[i])

def main():
    #도미노 상태 받기
    global DOMINO_STATUS
    global DOMINO
    N, M, Round = input_data()
    for i in range(N):
        DOMINO.append(list(input_data()))
        DOMINO_STATUS.append(["S"]*M)

    #게임시작
    score = start_game(Round)
    #결과 출력
    print(score)
    print_domino(N)
 
if __name__ == "__main__":
    main()
