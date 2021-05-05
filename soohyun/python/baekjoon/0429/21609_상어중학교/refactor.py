import sys
input = sys.stdin.readline

DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]


def is_in_boundary(nr, nc, N):
    if nr >= 0 and nr < N:
        if nc >= 0 and nc < N:
            return True
    return False


def is_in_block_group(blocks, row, col):
    if len(blocks) <= 0:
        return False
    for key, value in blocks.items():
        if key == (row, col):
            return True
        if value['blocks'].get((row, col), False):
            return True
    return False


def single_block_group(row, col, N):
    global board
    block_color = board[row][col]
    queue = [(row, col)]
    group = dict()
    rainbow_block = 0
    while len(queue) > 0:
        srow, scol = queue.pop(0)
        if not group.get((srow, scol), False):
            group[(srow, scol)] = True
        for dr, dc in zip(DR, DC):
            nr = srow + dr
            nc = scol + dc
            if is_in_boundary(nr, nc, N):
                color = board[nr][nc]
                if group.get((nr, nc), False):
                    continue
                if color == block_color or color == 0:
                    if color == 0:
                        rainbow_block += 1
                    queue.append((nr, nc))
                    group[(nr, nc)] = True
    return group, rainbow_block


def find_block_groups(board, N, M):
    global board
    block_groups = dict()
    for row in range(N):
        for col in range(N):
            if board[row][col] <= 0:
                continue
            if is_in_block_group(block_groups, row, col):
                continue
            group, rainbow_block = single_block_group(row, col) 
            if len(group.keys()) >= 2:
                block_groups[(start_block)] = {"num":len(group.keys()), "blocks":group, "rainbow":rainbow_block}
            if len(block_groups) == 0:
                break
    return block_groups


def find_max_block_group(block_groups):
    global board
    max_blocks = 0
    max_block_list = list()
    for key, block_group in block_groups.items():
        if block_group["num"] == max_blocks:
            max_block_list.append((key[0], key[1], block_group["blocks"], block_group["rainbow"]))
        if block_group["num"] > max_blocks:
            del max_block_list
            max_blocks = block_group["num"]
            max_block_list = [(key[0], key[1], block_group["blocks"], block_group["rainbow"])]

    max_rainbow = 0
    max_rainbow_list = list()
    for block in max_block_list:
        if block[3] == max_rainbow:
            max_rainbow_list.append((block[0], block[1], block[2]))
        if block[3] > max_rainbow:
            del max_rainbow_list
            max_rainbow = block[3]
            max_rainbow_list = [(block[0], block[1], block[2])]

    max_block_list = sorted(max_rainbow_list, key=lambda blocks: blocks[1])
    max_block_list = sorted(max_rainbow_list, key=lambda blocks: blocks[0])

    return max_block_list.pop()


 def remove_blocks(max_block):
    global board
    removed_row, removed_col, removed_group = max_block
    round_score = 0
    score = 0
    for key in list(removed_group.keys()):
        round_score += 1
        board[key[0]][key[1]] = -2
    score += round_score * round_score   
    return score


def gravity(N):
    global board
    for row in range(N-2, -1, -1):
        for col in range(N):
            if board[row][col] >= 0:
                input_row = row
                for nrow in range(row+1, N):
                    if board[nrow][col] < -1:
                        input_row += 1
                    else:
                        break
                if input_row != row:
                    board[input_row][col] = board[row][col]
                    board[row][col] = -2

def rotation(N):
    global board
    board_copy = list()
    for i in range(N):
        arr = list()
        for j in range(N):
            arr.append(board[i][j]) 
        board_copy.append(arr)

    for col in range(N-1, -1, -1):
        for row in range(0, N):
            board[N-1-col][row] = board_copy[row][col]
            i += 1


def start_game(board, N, M):
    score = 0
    while True:
        block_groups = find_block_groups(N)
        max_block = find_max_block_group(block_groups)
        score += remove_blocks(max_block, score)
        gravity(N)
        rotation(N)
        gravity(N)
    return score
        

def main():
    N, M = map(int, input().rstrip().split(" "))
    board = list()
    for _ in range(N):
        board.append(list(map(int, input().rstrip().split(" "))))
    print(start_game(board, N, M))


if __name__ == "__main__":
    main()