#시작 09시
import sys
input = sys.stdin.readline
grid = list()

DR = [(0, -1), (1, 0), (0, 1), (-1, 0)]
ATTACKDR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def make_blizzard(N):
    srow, scol = N//2, N//2
    d_idx, idx = 0, 0
    blizzard = dict()
    for k in range(2, N+1):
        direct = DR[d_idx % 4]
        d_idx += 1
        nr, nc = 0, 0  

        for i in range(k):
            if srow == N//2 and scol == N//2 and i == 0:
                continue
            nr = srow + direct[0] * i
            nc = scol + direct[1] * i
            if blizzard.get((nr, nc), -1) < 0:
                blizzard[(nr, nc)] = idx
                idx += 1
        direct = DR[d_idx % 4]
        d_idx += 1
        srow, scol = nr, nc

        for j in range(k):
            nr = srow + direct[0] * j
            nc = scol + direct[1] * j
            if blizzard.get((nr, nc), -1) < 0:
                blizzard[(nr, nc)] = idx
                idx += 1
        srow, scol = nr, nc


    while nc >= 0:
        if blizzard.get((nr, nc), -1) < 0:
            blizzard[(nr, nc)] = idx
            idx += 1
        nc -= 1
    return blizzard


def start_game(N, M, marbles, blizzard):
    srow, scol = N//2, N//2
    score = 0
    #print("start marbles", marbles)
    for _ in range(M):
        d, s = map(int, input().rstrip().split(" "))
        
        # attack
        for i in range(1, s+1):
            dr, dc = ATTACKDR[d-1]
            arow, acol = srow + dr * i, scol + dc * i
            if arow >= 0 and arow < N and acol >= 0 and acol < N and blizzard[(arow, acol)] < len(marbles):  
                del marbles[blizzard[(arow, acol)] - (i-1)]

        if len(marbles) == 0:
            break
        # 더이상 폭발할게 없을때까지 bomb
        while True:
            new_marbles = list()
            prev = 0
            continuous_marble = [marbles[prev]]
            is_change = False
            for i in range(1, len(marbles)):
                if marbles[prev] == marbles[i]:
                    continuous_marble.append(marbles[i])
                else:
                    if len(continuous_marble) >= 4:
                        score += len(continuous_marble) * continuous_marble[0]
                        is_change = True
                    else:
                        new_marbles.extend(continuous_marble)
                    continuous_marble = [marbles[i]]
                prev = i
            if len(continuous_marble) >= 4:
                score += len(continuous_marble) * continuous_marble[0]
                is_change = True
            else:
                new_marbles.extend(continuous_marble)
            if not is_change or len(new_marbles) == 0:
                break
            marbles = new_marbles
        marbles = new_marbles
        
        # 분화
        new_marbles = list()
        idx, start, count = 0, 0, 0
        while idx < len(marbles):
            if marbles[idx] == marbles[start]:
                count += 1
            else:
                if len(new_marbles) < N*N-1:
                    new_marbles.append(count)
                if len(new_marbles) < N*N-1:
                    new_marbles.append(marbles[start])
                start = idx
                count = 1
            idx += 1
        if start < idx:
            if len(new_marbles) < N*N-1:
                new_marbles.append(count)
            if len(new_marbles) < N*N-1:
                new_marbles.append(marbles[start])
        marbles = new_marbles
    return score

            

def main():
    global grid
    N, M = map(int, input().rstrip().split(" "))
    grid = [list(map(int, input().rstrip().split(" "))) for _ in range(N)]
    blizzard = make_blizzard(N)
    #print(blizzard)
    marbles = [grid[key[0]][key[1]] for key in blizzard.keys()]
    print(start_game(N, M, marbles, blizzard))

if __name__ == "__main__":
    main()