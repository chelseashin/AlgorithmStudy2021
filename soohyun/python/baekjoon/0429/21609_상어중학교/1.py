# 시작시간: 12시 2분
# 문제를 해석한시간: 12시 13분
# 12시 50분
# 시작: 2시 24분
# 코딩시간:4시
# 디버깅시간: 30분 + a

''' 알아야할것
 1. 블록: 검은색(-1)/무지개(0)/일반(1~M)
 2. 블록 그룹: 블록색이 모두 같은 블록들
    - 일반블록이 적어도 하나 포함되어야함
    - 검은색플록포함 x
    - 무지개는 상관 x
    - 블록 >= 2
    - 모든칸이 이동가능해야함
    - 기준블록: 행렬이 모두 작은것
'''
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


def print_board(board):
    print("==print board start==")
    for i in range(len(board)):
        print(*board[i])
    print("==print board end==")


def start_game(board, N, M):
    # 중력 그룹이 제거될때까지 반복
    # 블록 그룹찾기
    '''
    1. 크기가장큰 블록그룹
    2. 무지개 블록이 많은것
    3. 기준 블록의 행렬이 큰것
    '''
    '''
    자료구조: 블록그룹 저장할것
    '''
    score = 0
    while True:
        block_groups = dict()
        # block_groups[(start,end)] = {'num':12, 'blocks':{(0,1):True, (0,2):True, (0,3):True}}
        # 블록 그룹찾기
        for row in range(N):
            for col in range(N):
                if board[row][col] <= 0:
                    continue
                if is_in_block_group(block_groups, row, col):
                    continue

                block_color = board[row][col]
                start_block = (row, col)
                queue = [start_block]
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
                if len(group.keys()) >= 2:
                    block_groups[(start_block)] = {"num":len(group.keys()), "blocks":group, "rainbow":rainbow_block}
     
        if len(block_groups) == 0:
            break

        # 가장큰 블록 그룹 찾기
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
        '''print("==max_block_list==")
        print(max_rainbow_list)
        print("==max_block_listend==")'''
        # 블록 그룹 제거
        removed_row, removed_col, removed_group = max_rainbow_list.pop()
        round_score = 0
        for key in list(removed_group.keys()):
            round_score += 1
            board[key[0]][key[1]] = -2
        score += round_score * round_score
        '''print("SCORE", score, "ROUNDSCORE", round_score)
        print("remove start")
        print_board(board)
        print("remove end")'''
        # 중력
        # 맨끝 행부터 처음이 될때까지
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
                    
        '''print("gravity start")
        print_board(board)
        print("gravity end")'''
        # 90 회전
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
        '''print("rotation start")
        print_board(board)
        print("rotation end")'''
        # 중력
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
        '''print("gravity start")
        print_board(board)
        print("gravity end")'''
    return score


def main():
    N, M = map(int, input().rstrip().split(" "))
    board = list()
    for _ in range(N):
        board.append(list(map(int, input().rstrip().split(" "))))
    print(start_game(board, N, M))


if __name__ == "__main__":
    main()
